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
```

The app will be available at `http://127.0.0.1:5000/`.

## Project Structure

```
school_catering/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── utils.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── meal_distribution.py
│   │   └── parents.py
│   └── templates/
│       ├── dashboard.html
│       └── meal_distribution.html
├── migrations/
│   └── ...
├── requirements.txt
└── run.py
```

### Routes

- **Auth Routes (`app/routes/auth.py`)**: Handles user signup and email verification.
- **Dashboard Routes (`app/routes/dashboard.py`)**: Handles the manager's dashboard.
- **Meal Distribution Routes (`app/routes/meal_distribution.py`)**: Handles meal distribution.
- **Parent Routes (`app/routes/parents.py`)**: Handles parents' functionalities.

## Testing

To test the application using Postman:

1. Start the Flask application by running `flask run`.
2. Use Postman to send requests to the following endpoints:

    - **Sign up**: `POST /signup`
        - **Required Parameters**:
            - `name` (string): The name of the parent.
            - `email` (string): The email address of the parent.
            - `password` (string): The password for the account.
    
    - **Verify Email**: `GET /verify/<token>`
        - **Required Parameters**:
            - `token` (string): The verification token sent to the email.

    - **Report Absence**: `POST /absence`
        - **Required Parameters**:
            - `student_id` (integer): The ID of the student.
            - `date` (string): The date of absence in YYYY-MM-DD format.
    
    - **Dashboard**: `GET /dashboard`
        - **Query Parameters**:
            - `date` (string, optional): The date for the dashboard view in YYYY-MM-DD format. Defaults to today.

    - **Meal Distribution**: `GET /meal_distribution`
        - **Query Parameters**:
            - `date` (string, optional): The date for meal distribution in YYYY-MM-DD format. Defaults to today.
    
      `POST /meal_distribution`
        - **Required Parameters**:
            - `class_id` (integer): The ID of the class.
            - `student_meal_status` (array of objects):
                - `student_id` (integer): The ID of the student.
                - `status` (string): The meal status ('Given', 'Away', 'Did not get the meal').


For example, to sign up a user:

- URL: `http://127.0.0.1:5000/signup`
- Method: `POST`
- Body (JSON):
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "Password123!"
    }
    ```

## License

This project is licensed under the MIT License.
