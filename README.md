# AI Health Tracking Platform

An **AI-powered health tracking backend** that allows users to log health metrics, track fitness goals, generate personalized diet plans, and automatically sync activity data from Google Fit.

This project demonstrates a **production-style backend architecture** using modern backend technologies, background task processing, AI integration, and containerized infrastructure.

The system simulates the backend of a **health-tech application similar to modern fitness platforms** that combine wearable data, analytics, and AI-driven health recommendations.

---

# System Architecture


User
│
▼
FastAPI Backend
│
├── Authentication Service
├── Health Metrics Service
├── Goal Tracking Service
├── Analytics Engine
├── AI Diet Planner (LangGraph)
└── Google Fit Integration
│
▼
PostgreSQL Database
│
▼
Redis Queue
│
▼
Celery Workers
│
▼
Google Fit API


---

# Tech Stack

## Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

## Authentication
- JWT Tokens
- OAuth2
- bcrypt password hashing

## AI Layer
- LangGraph
- LLM-based diet generation

## Background Processing
- Celery
- Redis

## External APIs
- Google Fit API

## Infrastructure
- Docker
- Docker Compose

---

# Features

## Authentication System

Secure user authentication and authorization using JWT tokens.

Features:
- User registration
- Login authentication
- Password hashing
- Protected routes

Endpoints:


POST /auth/signup
POST /auth/login
GET /auth/me


---

# Health Metrics Tracking

Users can manually log daily health metrics including:

- Weight
- Steps
- Sleep
- Calories
- Water intake

Endpoints:


POST /health/log
GET /health/history
GET /health/today


Health records are stored per user and per day.

---

# Goal Tracking

Users can define personal fitness goals.

Examples:
- Target weight
- Daily calorie target
- Fitness goal type

Endpoints:


POST /goal/set
GET /goal/current


These goals are used by the analytics engine and diet planner.

---

# Analytics Engine

The system analyzes user health data and generates insights such as:

- Weekly progress
- Weight trends
- Step averages
- Estimated calorie deficit

Endpoint:


GET /analytics/progress


This endpoint aggregates health metrics to produce meaningful analytics.

---

# AI Diet Planner

The application includes an **AI-powered diet recommendation system**.

It uses **LangGraph agents** to generate personalized diet plans based on:

- User goals
- Health metrics
- Calorie targets
- Activity levels

Endpoint:


POST /diet/generate


Example response:


{
"breakfast": "Oatmeal with fruits",
"lunch": "Grilled chicken with quinoa",
"dinner": "Vegetable stir fry with brown rice",
"snacks": "Greek yogurt with nuts"
}


---

# Google Fit Integration

Users can connect their Google Fit account to automatically sync activity data.

The system retrieves step counts and other activity metrics.

Endpoints:


GET /google/connect
GET /google/callback
POST /google/sync


The backend uses OAuth to authenticate with Google Fit and fetch health data.

---

# Background Health Sync

The application uses **Celery workers and Redis queues** to automatically sync health data.

Features:
- Periodic data ingestion
- Background job processing
- Automatic Google Fit data sync

Health metrics from Google Fit are inserted into the database and used by analytics and AI modules.

---

# Dockerized Infrastructure

The project uses **Docker Compose** to run all services together.

Services include:

- FastAPI backend
- PostgreSQL database
- Redis server
- Celery worker
- Celery beat scheduler

Start the entire system with:


docker-compose up --build


---

# Project Structure


backend
│
├── app
│ ├── api
│ │ └── routes
│ │
│ ├── core
│ │ ├── config.py
│ │ └── security.py
│ │
│ ├── db
│ │ └── session.py
│ │
│ ├── models
│ │ ├── user.py
│ │ ├── health_metric.py
│ │ └── goal.py
│ │
│ ├── services
│ │ ├── analytics_service.py
│ │ ├── diet_service.py
│ │ └── google_fit_service.py
│ │
│ ├── workers
│ │ ├── celery_app.py
│ │ └── health_tasks.py
│ │
│ └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

# Installation

## Clone Repository


git clone https://github.com/yourusername/health-tracking-platform.git

cd health-tracking-platform/backend


---

## Install Dependencies


pip install -r requirements.txt


---

## Run Server


uvicorn app.main:app --reload


Access API documentation:


http://localhost:8000/docs


---

# Running with Docker

Start all services using Docker Compose.


docker-compose up --build


This will launch:

- FastAPI server
- PostgreSQL database
- Redis server
- Celery worker
- Celery scheduler

---

# API Documentation

Once the server is running, interactive API documentation is available at:


http://localhost:8000/docs


The documentation allows you to test all endpoints directly from the browser.

---

# Future Improvements

Potential improvements for the project:

- Frontend dashboard using React or Next.js
- Advanced analytics visualizations
- Real-time notifications
- More wearable integrations
- Mobile app integration
- Improved AI health coaching features

---

# Learning Outcomes

This project demonstrates knowledge of:

- Backend API design
- Authentication and security
- Database modeling
- Background task processing
- External API integration
- AI agent workflows
- Containerized deployment
- Production-style backend architecture

---

# License

This project is open-source and available under the MIT License.
