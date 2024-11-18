Telegram bot template for Aiogram 3 + SQLAlchemy
This project is a comprehensive template for the development of scalable Telegram bots using the Aiogram 3 framework, SQLAlchemy for working with the database and Alembic for migration management.

The convenient logo ru library is used for logging. Thanks to this, the logs are beautifully highlighted in the console and recorded in the log file in the background.

Technology stack
Telegram API: Aiogram 3
ORM: SQLAlchemy with aiosqlite
Database: SQLite
Migration system: Alembic
Architecture Overview
The project follows an architecture inspired by microservices and FastAPI best practices. Each functional component of the bot is organized as a mini-service, which ensures modularity of development and maintenance.

Project structure
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

Environment variables
Create a file.env at the root of the project:

BOT_TOKEN=your_bot_token_here
ADMIN_IDS=[12345,344334]
POSTGRES_USER=postgres_container
POSTGRES_PASSWORD=postgres_container
POSTGRES_HOST=172.18.0.2
POSTGRES_PORT=5432
POSTGRES_DB=postgres
