from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import sqlite3

app = FastAPI()

templates_directory = os.path.join(os.getcwd(), "templates")
static_directory = os.path.join(os.getcwd(), "static")
database_directory = os.path.join(os.getcwd(), "db")
templates = Jinja2Templates(directory=templates_directory)

if not os.path.exists(database_directory):
    os.makedirs(database_directory)

database_url = os.path.join(database_directory, "fastapi.db")

def get_db(request: Request):
    return request.state.db

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = None
    try:
        request.state.db = sqlite3.connect(database_url)
        response = await call_next(request)
    finally:
        if hasattr(request.state, 'db'):
            request.state.db.close()
    return response

def get_user(db, username: str):
    cursor = db.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE username = ?
    ''', (username,))
    
    row = cursor.fetchone()
    if row:
        return {
            "id": row[0],
            "username": row[1],
            "password": row[2]
        }
    return None

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    db = get_db(request)
    user = get_user(db, username)
    
    if user is not None and user["password"] == password:
        return templates.TemplateResponse("index.html", {"request": request, "user": user})
    else:
        return templates.TemplateResponse("dashboard.html", {"request": request, "error": "Incorrect username or password"})

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse) 
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, username: str = Form(...), password: str = Form(...)):
    db = get_db(request)
    
    if get_user(db, username):
        raise HTTPException(status_code=400, detail="Username already exists")
    
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO users(username, password) VALUES (?, ?)
    ''', (username, password))
    db.commit()
    return templates.TemplateResponse("login.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
