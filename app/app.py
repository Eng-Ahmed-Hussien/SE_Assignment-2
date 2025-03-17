#!/usr/bin/env python3
"""
Full-Stack App with Custom Login Form and External CSS

This application implements a login system, registration, a dashboard with user management, 
a task explanation page, and now password editing functionality. It is built with Flask, uses SQLite 
as its database, and uses a custom HTML/CSS login form.

Coding standards applied:
- camelCase for variables and methods
- PascalCase for classes
- UPPER_CASE for constants
- PEP 257 docstrings for documentation
- try-except blocks for error handling

Feel free to push this code to GitHub using your preferred Git branching strategy.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # Change this for production!

# Database configuration using SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
dbPath = os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbPath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    """
    User model representing a registered user.

    Attributes:
        id (int): Unique identifier.
        username (str): The username.
        password (str): The user's password.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

def createTables():
    """
    Create database tables if they do not exist and add a default admin user.
    """
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        adminUser = User(username='admin', password='admin')  # In production, store hashed passwords!
        db.session.add(adminUser)
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Login route: Displays the custom login form and authenticates the user.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                session['user_id'] = user.id
                session['username'] = user.username
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials. Please try again.', 'danger')
        except Exception as error:
            flash(f'Error: {error}', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registration route: Displays the registration form and creates a new user.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            if User.query.filter_by(username=username).first():
                flash('Username already exists. Choose another.', 'danger')
            else:
                newUser = User(username=username, password=password)
                db.session.add(newUser)
                db.session.commit()
                flash('Registration successful! Please log in.', 'success')
                return redirect(url_for('login'))
        except Exception as error:
            flash(f'Registration error: {error}', 'danger')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """
    Dashboard route: Displays user management and task explanation options.
    """
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))
    users = User.query.all()
    return render_template('dashboard.html', users=users)

@app.route('/delete_user/<int:user_id>')
def deleteUser(user_id):
    """
    Delete a user from the database.
    """
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))
    try:
        userToDelete = User.query.get(user_id)
        # Prevent deletion of the admin user
        if userToDelete and userToDelete.username != 'admin':
            db.session.delete(userToDelete)
            db.session.commit()
            flash('User deleted successfully!', 'success')
        else:
            flash('Cannot delete admin or user not found.', 'danger')
    except Exception as error:
        flash(f'Error deleting user: {error}', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def editUser(user_id):
    """
    Edit user route: Allows editing of a user's password.
    """
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))
    userToEdit = User.query.get(user_id)
    if not userToEdit:
        flash('User not found.', 'danger')
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        new_password = request.form.get('password')
        try:
            userToEdit.password = new_password
            db.session.commit()
            flash('Password updated successfully!', 'success')
            return redirect(url_for('dashboard'))
        except Exception as error:
            flash(f'Error updating password: {error}', 'danger')
    return render_template('edit_user.html', user=userToEdit)

@app.route('/task_explanation')
def taskExplanation():
    """
    Task explanation page: Provides details about the application.
    """
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))
    explanation = (
        "This dashboard allows you to manage users by adding, editing, or deleting them, and provides a "
        "task explanation page detailing the application's functionality. The login system is built "
        "using Python (Flask) and uses SQLite as its database. Extend and style this application as needed!"
    )
    return render_template('task_explanation.html', explanation=explanation)

@app.route('/logout')
def logout():
    """
    Logout route: Clears the session and logs out the user.
    """
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Ensure tables are created within the application context
    with app.app_context():
         createTables()
    app.run(debug=True)
