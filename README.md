Employee Management System (EMS)
Overview

This project aims to develop a simple, scalable, and user-friendly Employee Management System (EMS) using Python and Django.
The application provides essential functionalities such as managing employee records with full CRUD operations, along with a clean and responsive UI built using HTML, CSS, and Bootstrap.

Requirements
1. Employees

CRUD Operations:

Create new employee records

Retrieve employee details

Update employee information

Delete employee records

Employee Details:

Employee Name

Email

Phone Number

Department

Designation

Salary (optional)

Search and Filter:

Search employees by name or department

Filter employees based on designation or department

2. Departments

Create and manage departments

Assign employees to departments

View employees under a specific department

3. User Interface

Responsive UI using Bootstrap

Simple and clean forms

Employee listing with table view

4. Miscellaneous

Validation:

Server-side validation using Django forms/models

Prevent invalid or empty inputs

Error Handling:

Proper error messages

User-friendly validation feedback

Security:

Django ORM to prevent SQL Injection

CSRF protection enabled

Secure form handling : under Process

Documentation:

Well-structured README documentation

Clear setup instructions

Testing:

Basic unit testing for models and views (optional)

Manual testing through UI

API / Application Endpoints
Employees

GET /employees/ – Retrieve all employees

GET /employees/<id>/ – Retrieve employee by ID

POST /employees/add/ – Add a new employee

PUT /employees/edit/<id>/ – Update employee details

DELETE /employees/delete/<id>/ – Delete an employee

Departments: under Process

GET /departments/ – Retrieve all departments

POST /departments/add/ – Add a new department

Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

Version Control: Git & GitHub
