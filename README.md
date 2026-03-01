# Library_management (Docker + PostgreSQL Setup)

## Prerequisites

- Docker installed
- Docker Compose installed

Verify installation:

docker --version
docker compose version

---

## Project Setup

Make sure you have a .env file in the root directory with the following:

- DB_NAME=librarydb
- DB_USER=admin
- DB_PASSWORD=admin123
- DB_HOST=db
- DB_PORT=5432

---

## Start the Application

Build and start all services:

docker compose up --build

Run in detached mode (background):

docker compose up -d

---

## Access URLs

- Application URL : http://localhost:8000/
- Library URL     : http://localhost:8000/library
- Admin URL       : http://localhost:8000/admin/

---

## Apply Migrations (First Time Setup)

In a new terminal:

docker compose exec web python manage.py migrate

---

## Create Superuser (Optional)

docker compose exec web python manage.py createsuperuser

---

## Stop the Application

docker compose down

---

## Stop and Remove Database Volume (Deletes all DB data)

docker compose down -v
