# Contact Management System

## Project Description
This project is a simple Django application that allows users to manage their contacts. Users can perform CRUD operations on contacts via RESTful APIs.

## Setup and Run Instructions

1. Clone the repository:
    ```bash
    git clone <https://github.com/roger9696/contact-management.git>
    cd contact_management
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create and apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

6. Access the project in your web browser:
    - API Documentation: `http://127.0.0.1:8000/swagger/`
    - Contact Endpoints: `http://127.0.0.1:8000/api/contacts/`

7. Testing
   `python manage.py test`


## API Endpoints
Create a Contact: POST `/api/contacts/`
Retrieve Contacts: GET `/api/contacts/`
Retrieve a Contact: GET `/api/contacts/<id>/`
Update a Contact: PUT `/api/contacts/<id>/`
Delete a Contact: DELETE `/api/contacts/<id>/`

## Additional Notes
- Ensure you have Python and Django installed.
- The project follows the standard Django project structure.
- The `Contact` model is defined in `contacts/models.py`.

## License Information
This project is licensed under the MIT License.
