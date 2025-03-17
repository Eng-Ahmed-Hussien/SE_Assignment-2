# ADVANCED SOFTWARE ENGINEERING

## Assignment No. 2  

**Software Implementation and Coding Standards**  
*(From my understanding of the fourth lecture)*

### Submitted To

- Assoc. Prof. Ahmed Moustafa Elmahalawy  
- Dr. Mervat

### Submitted By

- **Name:** Ahmed Hussien El-Sayed Abd El Hamid  
- **Academic ID:** 15210408

---

## Full-Stack Flask App with SE Guidelines

This repository contains a full‑stack application built with Flask and SQLite. The project demonstrates key software engineering best practices and coding standards:

- **Naming Conventions:**  
  - camelCase for variables and methods  
  - PascalCase for classes  
  - UPPER_CASE for constants

- **Documentation Style:**  
  - Follows PEP 257 (Python) docstrings

- **Error Handling:**  
  - Uses `try-except` blocks for robust error management

- **Version Control:**  
  - Managed with Git and follows GitFlow branching strategy

## Features

- **User Authentication**: Login and registration system  
- **Dashboard**: View, edit (password), and delete users (with admin safeguards)  
- **Task Explanation**: Page detailing how the app follows SE best practices  
- **Creative Design**: Dark-themed UI with custom CSS animations and gradients

## Project Structure

```plaintext
SE_ASSIGNMENT-2
 ├── app
 │ ├── static
 │ │ └── styles.css
 │ ├── templates
 │ │ ├── dashboard.html
 │ │ ├── edit_user.html
 │ │ ├── login.html
 │ │ ├── register.html
 │ │ └── task_explanation.html
 │ ├── app.db
 │ └── app.py
 ├── requirements.txt
 └── README.md
 ```

## Getting Started

1. **Clone the repository** :

   ```bash
   git clone https://github.com/Eng-Ahmed-Hussien/SE_Assignment-2
   ```

2. **Install dependencies** :

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application** :

    ```bash
    cd app
    python app.py
    ```

4. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the app.

## Usage

- **Login:** Use the default `admin` / `admin` or register a new user.
- **Dashboard:** Manage users (view, edit password, or delete) except that admin cannot be deleted.
- **Task Explanation:** Learn how this app follows software engineering guidelines.
- **Logout:** Clears the session and returns to the login page.

## Contributing

Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss the proposed changes.
