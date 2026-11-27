# AI-Powered Nutrition & Fitness Management System

A web-based nutrition and fitness management application that combines data tracking, data analysis, and an AI-powered assistant to help users monitor their health and fitness goals.

## Project Overview

The system allows users to:

- Create personal profiles and define fitness goals.
- Track meals and nutritional intake.
- Record physical activities and exercises.
- Interact with an AI Agent using natural language.
- Receive personalized general recommendations.
- Visualize nutritional statistics and fitness progress.

The AI Agent interprets user inputs, interacts with structured application data, and provides contextual feedback based on recorded information.

## Current Development Status

The initial Django project foundation has been implemented as part of P03.

- Django project initialized.
- All five Django applications created and registered.
- Environment-based settings configured.
- SQLite configured for local development.
- Initial URL routing configured.
- Template and static directories configured.
- Basic development homepage implemented.
- Six automated tests successfully passed.

Authentication, database models, nutrition tracking, fitness tracking,
AI integration, and analytics will be implemented in subsequent phases.

The current homepage is a temporary development page and does not
represent the final user interface.

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap, JavaScript |
| Database | SQLite (local development), PostgreSQL (planned) |
| AI Integration | Python, LLM API |
| Data Analysis | Pandas |
| Charts | Chart.js |

## Project Structure

```text
AI-Nutrition-Fitness-Management-System/
|-- config/
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   |-- tests.py
|   |-- asgi.py
|   `-- wsgi.py
|-- accounts/
|-- nutrition/
|-- fitness/
|-- ai_agent/
|-- analytics/
|-- templates/
|   `-- home.html
|-- static/
|   |-- css/
|   |   `-- style.css
|   |-- images/
|   `-- js/
|-- docs/
|   `-- MVP_REQUIREMENTS.md
|-- .env.example
|-- .gitignore
|-- manage.py
|-- requirements.txt
`-- README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or a compatible version.
- Git.
- PostgreSQL will be required in a later development phase.

The initial setup has been tested with Python 3.13.4
and Django 5.2.19.

SQLite does not require a separate database server.

### 1. Clone the Repository

```bash
git clone https://github.com/Italoomoura/AI-Nutrition-Fitness-Management-System.git
cd AI-Nutrition-Fitness-Management-System
```

After P03 has been merged into the integration branch:

```bash
git switch develop
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Verify dependencies:

```bash
python -m pip check
```

### 5. Configure Environment Variables

Create a local `.env` file from `.env.example`.

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

Generate a unique Django secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Open the `.env` file and replace the SECRET_KEY placeholder
with the generated key.

Example configuration:

```dotenv
SECRET_KEY='your-generated-secret-key'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

PostgreSQL and AI provider variables are reserved for future
integration and are not required for the initial homepage.

Never commit the actual `.env` file.

### 6. Verify Django Configuration

```bash
python manage.py check
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in a web browser.

The initial project homepage should be displayed.

Press Ctrl+C to stop the server.

## Database Configuration

SQLite is currently used for local development.
PostgreSQL remains the planned database technology.

Initial database migrations are deferred until the team
confirms the user model strategy.

The homepage and initial automated tests can run without
applying database migrations.

An unapplied migration warning is expected during this phase.

Check migration status:

```bash
python manage.py showmigrations
```

Do not apply initial migrations until the user model
strategy has been confirmed.

## Testing

Run all automated tests:

```bash
python manage.py test
```

Run the initial project tests with detailed output:

```bash
python manage.py test config.tests -v 2
```

The initial test suite verifies:

- Homepage HTTP response status.
- Homepage template rendering.
- Homepage content.
- Display of application modules.
- Registration of all five Django applications.
- Static CSS file availability.

All six initial tests passed during P03 development.

Authentication and database operations are outside the
scope of these initial tests.

## Development Workflow

The project follows a branch-based development workflow.

- `main`: stable project version.
- `develop`: integration branch.
- `feature/<feature-name>`: individual feature development.
- `fix/<issue-name>`: bug fixes.

All changes must be submitted through Pull Requests targeting `develop`.

Direct commits to `main` are not allowed.

## Project Management

GitHub Projects is used to organize tasks and track development progress.

Team members should update their assigned tasks and follow the agreed Kanban workflow.

## Documentation

Project requirements and technical documentation are stored in the `docs/` directory.

## Security

- Never commit API keys or passwords.
- Never commit the `.env` file.
- Use environment variables for sensitive configuration.
- Do not share personal database credentials.
- Never commit the Django secret key.
- Do not commit the local SQLite database.
- Do not commit virtual environment folders.
- Do not commit generated static files.
- Enable DEBUG only for local development.
- Do not use the Django development server in production.

