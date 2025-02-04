# Task Manager

## Objective
A simple Task Management App using **Django, DRF, and JWT Authentication**.


## Setup Instructions
1. Create a virtual environment:\
    `python -m venv venv`\
    `source venv/bin/activate  # On Windows: venv\Scripts\activate`
2. Install dependencies:\
    `pip install -r requirements.txt`
3. Apply migrations:\
    `python manage.py migrate`  
4. Run seed data - contains test user and associated tasks:\
    `python manage.py seed`  \
    `username: user, password: user123` 
5. Run the server:\
    `python manage.py runserver` 
6. To run the tests:
   `pytest`


## Git branching strategy 

For this task manager project, I adopted a simple Git branching strategy.
Each feature or task was developed in its own branch, and once completed,
I created a pull request (PR) to merge the changes into the main branch. 
I regularly pulled updates from the main branch to keep my feature branches 
in sync with the latest changes. and after finishing the basic requirements
that mentioned in the attached file, I needed some branches for refactoring 
and for the bonus tasks.

