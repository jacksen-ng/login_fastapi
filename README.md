# Function of Login wiht FastAPI

## Index

- In this file I will use FastAPI to create a login form function with FastAPI

## About the **app** Folder

1. This folder contains six main components: *db*, *templates*, *main.py*, and *requirements.txt*.

2. The **db** folder contains the database settings.

5. The **templates** folder stores HTML files.

6. The **main.py** file is the main entry point of the FastAPI application.

7. The **requirements.txt** file lists all the dependencies required to run the project.

## Installation

>[!NOTE]
>Please use MacOS environment to proceed.

1. First, download the **app** folder and follow the process below:
    ```bash
    cd
    cd app
    ```

2. Create a Python virtual environment and activate it:
    ```bash
    python -m venv fastapivenv
    ```

    ```bash
    source fastapivenv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. After installed, please run the following command:
    ```bash
    cd db
    ```

    ```bash
    python database.py
    ```

5. Finally, start the FastAPI server:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```


## Launching the Application

Upon starting the server, navigate to the initial login page:

- **Access with this link** *http://0.0.0.0:8000/*

- **Login Page**: [login.html](https://github.com/jacksen-ng/login_fastapi/blob/main/app/templates/login.html)

You should see the following interface:

![Login Page](https://github.com/jacksen-ng/login_fastapi/blob/main/app/image/loginimage.png)

- I already create the user, you can use the following user to login:

**Username:** *admin*

**Password:** *admin*