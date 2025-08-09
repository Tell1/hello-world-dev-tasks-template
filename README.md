# Hello World Dev Tasks Template

A lightweight Django "Hello World" application built following KISS principles and modern Python best practices.

## Project Description

This is a minimal Django web application that demonstrates:

- **KISS Philosophy**: Simple, clean architecture without unnecessary complexity
- **Modern Python**: Uses Python 3.12+ with comprehensive type hints
- **UV Package Management**: Fast dependency management and virtual environments
- **Code Quality**: Ruff formatting, linting, and comprehensive testing
- **Pydantic Integration**: Settings validation with Pydantic v2
- **Vertical Slice Architecture**: Tests alongside code for better organization

## Features

- Single "Hello World" view with HTML template
- Comprehensive test suite with pytest and pytest-django
- Type-safe configuration with Pydantic settings
- Proper error handling and logging setup
- Security best practices (environment variables, input validation)
- AI development task management workflows

## Tech Stack

- **Python**: 3.12+
- **Framework**: Django 5.2.5
- **Package Manager**: UV
- **Testing**: pytest, pytest-django
- **Linting/Formatting**: Ruff
- **Type Checking**: mypy with django-stubs
- **Settings**: Pydantic v2 with pydantic-settings

## Usage

### Prerequisites

- Python 3.12 or higher
- UV package manager ([installation guide](https://github.com/astral-sh/uv))

### Setup

1. **Clone and navigate to the project:**
   ```bash
   cd hello-world-dev-tasks
   ```

2. **Create virtual environment:**
   ```bash
   uv venv
   ```

3. **Install dependencies:**
   ```bash
   uv sync --dev
   ```

### Development Commands

```bash
# Run the development server
uv run python src/hello_world/manage.py runserver

# Run all tests
uv run pytest src/hello_world/web/tests/ -v

# Format code
uv run ruff format .

# Check linting
uv run ruff check .

# Fix linting issues
uv run ruff check --fix .

# Type checking (if mypy is installed)
uv run mypy src/

# Run tests with coverage
uv run pytest --cov=src --cov-report=html
```

### Adding Dependencies

**Never edit `pyproject.toml` directly.** Always use UV commands:

```bash
# Add production dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Remove dependency
uv remove package-name
```

## Project Structure

```
hello-world-dev-tasks/
├── README.md                   # This file
├── CLAUDE.md                   # Development guidelines and best practices
├── pyproject.toml             # Project configuration and dependencies
├── .gitignore                 # Git ignore patterns
├── ai-dev-tasks/              # AI workflow definitions
│   ├── create-prd.md          # PRD generation workflow
│   ├── generate-tasks.md      # Task breakdown workflow
│   └── process-task-list.md   # Task execution guidelines
└── src/
    └── hello_world/           # Django project
        ├── manage.py          # Django management script
        ├── __init__.py
        ├── settings.py        # Django settings with Pydantic
        ├── urls.py            # URL routing
        ├── wsgi.py            # WSGI application
        ├── web/               # Web application module
        │   ├── __init__.py
        │   ├── views.py       # Hello World view
        │   ├── urls.py        # Web URL patterns
        │   └── tests/         # Tests alongside code
        │       ├── __init__.py
        │       └── test_views.py
        └── templates/
            └── web/
                └── hello.html # Hello World template
```

## Best Practices

### Code Quality

- **Functions under 50 lines** with single responsibility
- **Classes under 100 lines** representing single concepts
- **Files under 500 lines** - refactor by splitting into modules
- **Line length maximum 100 characters** (configured in Ruff)
- **Always use type hints** for function signatures and class attributes

### Testing

- **Test-Driven Development (TDD)** - write tests first
- **Descriptive test names** explaining what they test
- **Tests next to code** following vertical slice architecture
- **Use pytest fixtures** for test setup
- **Aim for 80%+ coverage** focusing on critical paths

### Documentation

- **Google-style docstrings** for all public functions and classes
- **Module docstrings** explaining purpose
- **Inline comments** for complex logic with `# Reason:` prefix
- **Keep README updated** with setup and usage instructions

### Security

- **Never commit secrets** - use environment variables
- **Validate input** with Pydantic models
- **Use parameterized queries** for database operations
- **Keep dependencies updated** with UV
- **Environment file (.env)** for local configuration (gitignored)

### Git Workflow

- **Conventional commits**: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`
- **Branch naming**: `feature/`, `fix/`, `docs/`, `refactor/`, `test/`
- **Small, focused commits** with descriptive messages
- **Never include AI generation notes** in commit messages

### Development Environment

- **Use UV exclusively** for package management
- **Run linting/formatting** before commits
- **Test locally** before pushing changes
- **Use virtual environments** (`.venv` directory)
- **Environment variables** in `.env` file (never committed)

## AI Development Workflows

This project includes structured AI development workflows in `ai-dev-tasks/`:

- **PRD Creation**: Generate Product Requirements Documents from user prompts
- **Task Generation**: Break PRDs into actionable development tasks
- **Task Management**: Execute and track implementation progress

These workflows enable systematic feature development with AI assistance while maintaining code quality and project standards.

## Contributing

1. Follow the coding guidelines in `CLAUDE.md`
2. Write tests for new functionality
3. Run linting and formatting before committing
4. Use conventional commit messages
5. Keep functions, classes, and files within size limits
6. Add proper documentation with Google-style docstrings

## License

This project is for educational and demonstration purposes.