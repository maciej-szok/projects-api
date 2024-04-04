General README showcasing how to do every day tasks.

# Migrations
Export env variables:
```bash
export $(grep -v '^#' .env | xargs)
```

Create a new migration:
```bash
alembic revision --autogenerate -m "message"
```

Apply migrations:
```bash
alembic upgrade head
```

# Starting the project locally
1. Create `venv` and install dependencies
2. Start PostgreSQL using `docker compose up`
3. Start the app in reload mode using `./start_reload.sh` script
