# ORLY: School Catering Management App

## Overview
ORLY is an application designed to manage school catering efficiently. It provides functionalities for both managers and parents to handle meal distribution, track absences, and manage meal preferences.

## Features

### For Managers:
- **Sign Up Families:** Manually sign up family names, kids, and grades.
- **Approve Parents' Sign Up:** Approve or reject parent sign-ups.
- **Meal Management:**
  - **Show Meals:** Display available meals and their details.
  - **Add Meals:** Add new meal options.
  - **Show Regular Menu:** View regular menu options for specific days.
  - **Edit Regular Menu:** Modify the regular menu to select meals for each day.
  - **Show Week Menu:** View the week's menu and check for special meals.
  - **Add Special Meals:** Add special meal options for specific dates.
- **Meal Giveout Management:**
  - **Give Out Meals:** Mark students as having received their meals.
  - **Delete Giveout Records:** Remove a meal giveout record if marked incorrectly.
  - **Check Meal Status:** Verify if a student received their meal on a specific date.
- **Dashboard:**
  - **View Meal Availability:** See available meals for today.
  - **Track Meal Distribution:** Check how many kids should receive meals today, how many are absent, and how many received their meal.
  - **Manage Absences and Giveout Records:** Update meal distribution and absence information.

### For Parents:
- **Sign Up:** Register and get approval to use the system.
- **Meal Preferences:** Choose meal preferences for each day of the week.
- **Report Absences:** Inform the system if a child is not in school.
- **View Budget and Consumption:** Track the monthly meal consumption and budget.

## Installation

### Requirements
- Python 3.x
- Flask
- SQLAlchemy
- PyJWT
- SQLite (or other SQL database)

### Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd school_catering
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application
1. Set environment variables for Flask:
   ```
   export FLASK_APP=app
   export FLASK_ENV=development
   ```
2. Initialize the database (if needed):
   ```
   flask db upgrade
   ```
3. Run the application:
   ```
   flask run
   ```
   The app will be available at http://127.0.0.1:5000/.

## API Endpoints

### Authentication
- **POST /auth/signup:** Register a new user.
- **POST /auth/login:** Authenticate and get a JWT token.

### Parents
- **POST /parents/report_absence:** Report an absence for a student.
- **POST /parents/add_child:** Add a child to a family (manager only).

### Menu
- **GET /menu/show_meals:** Display available meals.
- **POST /menu/add_meals:** Add a new meal.
- **GET /menu/show_regular_menu:** Show the regular menu.
- **POST /menu/edit_regular_menu:** Edit the regular menu.
- **GET /menu/show_week_menu:** View the week’s menu.
- **POST /menu/add_special_meal:** Add special meal options for specific dates.

### Meal Giveout
- **POST /meal_giveout:** Mark students as having received their meals.
- **DELETE /meal_giveout:** Remove a meal giveout record.
- **GET /meal_giveout/check_if_got:** Check if a student received their meal on a specific date.

### Testing
- **GET /test/tables:** List all tables in the database.
- **GET /test/tables/<table_number>:** Show the latest 10 records from a specific table.

## Notes
- Ensure that the `config.py` file is properly configured with your environment settings.
- For email functionality, the configuration needs to be updated with valid SMTP settings.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
