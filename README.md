#  Supportlytics AI Enterprise

> AI-Powered Multi-Agent Platform for Intelligent IT Operations

Supportlytics AI Enterprise is an AI-powered multi-agent platform designed to modernize enterprise IT support operations through intelligent automation, predictive analytics, and collaborative decision-making.

Developed as part of the **Kaggle 5-Day AI Agents Intensive Vibe Coding Course with Google**, the project demonstrates how multiple specialized AI agents collaborate to automate IT ticket management while maintaining Human-in-the-Loop (HITL) oversight for critical business decisions.

---

#  Table of Contents

- Project Overview
- Problem Statement
- Solution
- Features
- Multi-Agent Workflow
- System Architecture
- Tech Stack
- Folder Structure
- Installation
- Running the Project
- API Endpoints
- Screenshots
- Future Scope
- License

---

#  Project Overview

Enterprise IT teams receive hundreds of support requests every day. Manually processing these tickets is time-consuming, error-prone, and often results in delayed response times and missed SLAs.

Supportlytics AI Enterprise automates the IT support lifecycle using specialized AI agents that classify incidents, predict ticket priority, estimate risk, recommend actions, and provide analytics through an interactive enterprise dashboard.

---

#  Problem Statement

Traditional IT support systems rely heavily on manual decision-making.

Support engineers must:

- Classify incidents
- Assign priorities
- Estimate SLAs
- Assess risks
- Coordinate resolutions
- Monitor operational performance

These repetitive tasks reduce productivity and increase operational costs.

---

#  Solution

Supportlytics AI Enterprise introduces a collaborative multi-agent architecture that automates IT support workflows while ensuring human oversight for high-risk operations.

The platform combines:

- AI Predictions
- Business Analytics
- Traffic Simulation
- Dataset Ingestion
- Executive Dashboards
- Human-in-the-Loop Governance

into one intelligent enterprise platform.

---

#  Features

##  Executive Dashboard

- Real-time operational metrics
- AI System Health
- Live Activity Feed
- Executive KPIs
- Multi-Agent Workflow

---

##  Ticket Management

- Search Tickets
- Filter by Priority
- View Ticket Details
- AI Decision Trace

---

##  Analytics Dashboard

Interactive visualizations for:

- Ticket Status
- Priority Distribution
- Category Distribution
- Country Distribution
- Executive KPIs

---

##  AI Prediction Engine

Predicts:

- Ticket Priority
- Risk Level
- SLA
- Resolution Time

Generates intelligent recommendations for support engineers.

---

##  Traffic Simulator

Generate synthetic IT support tickets to test the system without affecting production data.

---

##  Dataset Upload

Import historical datasets.

Automatically updates:

- Analytics
- Predictions
- Dashboard

---

##  PDF Reporting

Generate professional reports for managers and executives.

---

#  Multi-Agent Workflow

Supportlytics consists of five specialized AI agents.

###  Ticket Ingestion Agent

- Receives incoming tickets
- Validates requests
- Creates ticket records

---

###  Classification Agent

Automatically categorizes incidents.

Examples:

- Hardware
- Software
- Network
- Access
- Other

---

###  Prediction Agent

Predicts:

- Priority
- Risk
- SLA
- Resolution Time

---

###  Recommendation Agent

Suggests operational actions such as:

- Escalation
- Assignment
- Immediate Investigation

---

###  Human-in-the-Loop Agent

Critical operations require human approval before execution.

---

#  System Architecture

```
                Users
                   │
                   ▼
        Ticket Ingestion Agent
                   │
                   ▼
        Classification Agent
                   │
                   ▼
          Prediction Agent
                   │
                   ▼
       Recommendation Agent
                   │
                   ▼
      Human-in-the-Loop Agent
                   │
                   ▼
           SQLite Database
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
 Analytics Engine      Dashboard
         ▼                   ▼
    Reports           Live Activity
```

---

#  Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite

### Frontend

- HTML
- CSS
- JavaScript
- Chart.js

### AI

- Multi-Agent Architecture
- Prediction Engine

### Communication

- WebSockets

### Development

- Antigravity

---

#  Project Structure

```
supportlytics-ai-enterprise/

│
├── backend/
│   ├── api/
│   ├── database/
│   ├── repositories/
│   ├── services/
│   ├── models/
│   ├── websocket/
│   └── simulator/
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── styles.css
│   └── assets/
│
├── datasets/
│
├── screenshots/
│
└── README.md
```

---

#  Installation

Clone the repository

```bash
git clone https://github.com/USERNAME/supportlytics-ai-enterprise.git

cd supportlytics-ai-enterprise
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

#  Running the Backend

```bash
uvicorn backend.main:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

#  Running the Frontend

Open the frontend using a local web server.

Example:

```bash
python -m http.server 5500
```

Then open:

```
http://127.0.0.1:5500
```

---

# 📡 API Endpoints

## Tickets

```
GET /tickets
POST /tickets
PUT /tickets/{id}
DELETE /tickets/{id}
```

---

## Dashboard

```
GET /dashboard
```

---

## Analytics

```
GET /analytics
```

---

## AI Prediction

```
GET /prediction/priority/{ticket_id}

GET /prediction/risk/{ticket_id}

GET /prediction/sla/{ticket_id}

GET /prediction/resolution/{ticket_id}
```

---

## Dataset Upload

```
POST /ingestion/upload
```

---

## Simulator

```
POST /simulator/start

POST /simulator/stop
```

---

#  Screenshots

Include screenshots of:

- Dashboard
- Ticket Management
- Analytics
- AI Prediction
- Traffic Simulator
- Dataset Upload
- PDF Report

---

#  Future Scope

Future enhancements include:

- Large Language Model Integration
- Model Context Protocol (MCP)
- Cloud Deployment
- Role-Based Authentication
- Advanced Security
- Enterprise Notification Integrations
- Conversational AI Assistant
- Real-Time Collaboration
- Advanced Predictive Analytics

---

#  License

This project was developed for the **Kaggle Vibe Coding Agents Capstone Project** as part of the **Google AI Agents Intensive Vibe Coding Course**.

Licensed under the **MIT License**.

---

#  Author

**Priya J. Shet**

GitHub: https://github.com/ShanuShet

LinkedIn: https://www.linkedin.com/in/priya-j-shet/

Youtube: https://youtu.be/wvx-lsBA8hM

---

 If you found this project useful, consider giving it a star!