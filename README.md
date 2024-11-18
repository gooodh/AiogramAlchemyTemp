# Telegram Bot Template for Aiogram 3 + SQLAlchemy

This project is a comprehensive template for the development of scalable Telegram bots using the Aiogram 3 framework, SQLAlchemy for working with the database, and Alembic for migration management.

The convenient `loguru` library is used for logging. Thanks to this, the logs are beautifully highlighted in the console and recorded in the log file in the background.

## Technology Stack

- **Telegram API**: Aiogram 3
- **ORM**: SQLAlchemy with aiosqlite
- **Database**: SQLite
- **Migration System**: Alembic

## Architecture Overview

The project follows an architecture inspired by microservices and FastAPI best practices. Each functional component of the bot is organized as a mini-service, which ensures modularity of development and maintenance.

## Project Structure

├── bot/
│   ├── migration/
│   │   ├── versions
│   │   ├── env.py
│   ├── dao/
│   │   ├── base.py
│   ├── users/
│   │   ├── keyboards/
│   │   │ ├── inline_kb.py
│   │   │ ├── markup_kb.py
│   │   ├── models.py
│   │   ├── utils.py
│   │   └── router.py
│   ├── database.py
│   ├── log.txt
│   ├── main.py
│   └── config.py
├── data/
│   ├── db.sqlite3
├── alembic.ini
├── .env
├── docker-compose.yml
└── requirements.txt


## Environment Variables

Create a file named `.env` at the root of the project with the following content:

