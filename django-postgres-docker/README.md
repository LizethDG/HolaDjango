# Django PostgreSQL Docker Setup

This project is a Dockerized setup for a Django application using PostgreSQL as the database. Below are the instructions for setting up and running the project.

## Project Structure

```
django-postgres-docker
├── app                 # Your Django app(s)
│   ├── migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── project_name        # Your Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── README.md
└── requirements.txt
```

## Prerequisites

- Docker and Docker Compose installed on your machine.

## Setup Instructions

1. **Clone the Repository**: Clone this repository to your local machine.

2. **Navigate to the Project Directory**:
   ```bash
   cd django-postgres-docker
   ```

3. **Build the Docker Containers**:
   ```bash
   docker-compose build
   ```

4. **Run the Docker Containers**:
   ```bash
   docker-compose up
   ```

5. **Migrate the Database**:
   In a new terminal, run the following command to apply migrations:
   ```bash
   docker-compose run web python manage.py migrate
   ```

6. **Create a Superuser** (optional):
   You can create a superuser to access the Django admin:
   ```bash
   docker-compose run web python manage.py createsuperuser
   ```

7. **Access the Application**:
   Open your web browser and go to `http://localhost:8000` to see your Django application running.

## Usage

- To stop the containers, press `CTRL+C` in the terminal where the containers are running.
- To run tests, use:
  ```bash
  docker-compose run web python manage.py test
  ```

## Notes

- Ensure that you have configured your `settings.py` file to connect to the PostgreSQL database.
- Update the `requirements.txt` file with any additional dependencies your project may need.

## License

This project is licensed under the MIT License.