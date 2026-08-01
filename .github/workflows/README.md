# FixAI DevOps

## Project Overview
FixAI is an AI-powered DevOps issue management system.

## Tech Stack
- Node.js
- Express.js
- PostgreSQL
- Supabase
- Docker
- GitHub Actions
- Render
- OpenAI API

## Project Structure
```
.
├── database/
├── .github/workflows/
├── Dockerfile
├── docker-compose.yml
├── index.js
├── package.json
└── README.md
```

## Setup

### Install dependencies
```bash
npm install
```

### Run locally
```bash
npm start
```

### Docker
```bash
docker-compose up --build
```

## Environment Variables

Create a `.env` file using `.env.example`.

Required variables:

- PORT
- SUPABASE_URL
- SUPABASE_PUBLISHABLE_KEY
- OPENAI_API_KEY

## Deployment

Application is deployed on Render.

CI/CD is configured using GitHub Actions.

## Database

- PostgreSQL
- Supabase
- Indexes
- RLS Policies
- Authentication SQL

## Author

DevOps Team
## Firebase Setup

1. Create a Firebase Project.
2. Generate a Firebase Service Account Key.
3. Add FIREBASE_PROJECT_ID, FIREBASE_CLIENT_EMAIL and FIREBASE_PRIVATE_KEY to the .env file.
4. Restart the application after updating the environment variables.