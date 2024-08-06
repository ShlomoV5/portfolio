# ORLY: School Catering Management App

This is a School Catering Management App that helps manage meal distributions for school students. It has functionalities for both managers and parents.

## Features

### Manager Functions:
- Manually sign up family name, kids, grades.
- Approve parents' sign up.
- Choose food available for each day, and make temporary changes such as "no school today" or "today only this meal type is available".
- Lunch give out screen: select class, see meal selections by student, tick out kids who got lunch, or choose "not in school today".
- See archived and current month meal consumption and budget by family and by student.
- Add discount for mistakes, problems, etc to subtract from month total.

### Parent Functions:
- Sign up.
- Choose weekly food for each day (Sun-Thu excluding Tue) by Saturday midnight. If not chosen, the default meal is charged.
- Report "child not in school today" by 7 AM each day.
- See archived and current month meal consumption and budget by child.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-Mail
- PyJWT

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/school_catering.git
    cd school_catering
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables (you can also use a `.env` file):

    ```bash
    export FLASK_APP=run.py
    export FLASK_ENV=development
    export SECRET_KEY='your_secret_key'
    export MAIL_SERVER='smtp.example.com'
    export MAIL_PORT=587
    export MAIL_USERNAME='your_email@example.com'
    export MAIL_PASSWORD='your_password'
    ```

5. Initialize the database:

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

### Running the Application

To run the application, use:

```bash
flask run
