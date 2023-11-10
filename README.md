# job_tracker
~~~
/job_tracker_app/
│
├── /app/                      # Application specific components
│   ├── /api/                  # Endpoints and API specific logic
│   │   ├── /v1/               # Version 1 of our API
│   │   │   ├── /endpoints/    # Different endpoints of our API
│   │   │   │   ├── job_application.py  # Job application CRUD operations
│   │   │   │   ├── company.py          # Company profile operations
│   │   │   │   └── auth.py             # Authentication operations
│   │   │   ├── __init__.py   # Initialize the v1 module
│   │   │   └── deps.py       # Dependencies for routes (e.g., get_db, get_current_user)
│   │   └── __init__.py       # Initialize the api module
│   │
│   ├── /core/                 # Application configuration, startup events, logging
│   │   ├── config.py          # Configuration settings and environment variables
│   │   └── events.py          # Startup and shutdown events
│   │
│   ├── /models/               # Database models
│   │   ├── job_application.py # Job application model
│   │   ├── user.py            # User model
│   │   └── __init__.py        # Initialize the models module
│   │
│   ├── /schemas/              # Pydantic models for request and response data
│   │   ├── job_application.py # Schemas for job application
│   │   ├── user.py            # Schemas for user operations
│   │   └── __init__.py        # Initialize the schemas module
│   │
│   ├── /services/             # Services and business logic
│   │   ├── resume_generator.py # Service to generate resumes
│   │   └── __init__.py         # Initialize the services module
│   │
│   ├── /db/                   # Database related operations
│   │   ├── base.py            # Base class for database models
│   │   ├── session.py         # Database session management
│   │   └── init_db.py         # Database initialization
│   │
│   ├── /exceptions/           # Custom exception classes and error handling
│   │   └── handlers.py        # Error handler definitions
│   │
│   ├── main.py                # FastAPI application creation and configuration
│   │
│   └── /utils/                # Utility scripts and helper functions
│       └── common.py          # Common utility functions
│
├── /migrations/               # Database migration scripts
│
├── /tests/                    # Test suite
│   ├── /api/                  # API route tests
│   └── /unit/                 # Unit tests
│
├── requirements.txt           # Project dependencies
│
└── README.md                  # Project documentation
~~~