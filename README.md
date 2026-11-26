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

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap, JavaScript |
| Database | PostgreSQL |
| AI Integration | Python, LLM API |
| Data Analysis | Pandas |
| Charts | Chart.js |

## Project Structure

```text
ai-nutrition-fitness/
├── config/
├── accounts/
├── nutrition/
├── fitness/
├── ai_agent/
├── analytics/
├── templates/
├── static/
├── docs/
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or a compatible version.
- Git.
- PostgreSQL (required when database integration is implemented).

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Italoomoura/AI-Nutrition-Fitness-Management-System.git
cd AI-Nutrition-Fitness-Management-System
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Configure your local environment variables using `.env.example` as a reference.

6. Start the Django development server once the Django project has been initialized:

```bash
python manage.py runserver
```

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
