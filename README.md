# Dashboard Application with Next.js Frontend and Django Backend 

## Overview

This project is a dynamic dashboard built using **Next.js** with **TypeScript** on the frontend and **Django** on the backend. The dashboard displays four different types of charts: **Candlestick**, **Line**, **Bar**, and **Pie**, with data fetched dynamically from the backend API endpoints. The frontend integrates charting libraries and utilizes **Redux** for state management to provide clear, responsive, and maintainable data visualizations.

Both the frontend and backend are containerized using **Docker**, allowing for easy setup and deployment.

---

## Table of Contents

- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up Using Docker](#2-set-up-using-docker)
    - [2.1 Build and Run the Containers](#21-build-and-run-the-containers)
  - [3. Set Up the Backend (Django)](#3-set-up-the-backend-django)
  - [4. Set Up the Frontend (Next.js with TypeScript and Redux)](#4-set-up-the-frontend-nextjs-with-typescript-and-redux)
  - [5. Visit the Dashboard](#5-visit-the-dashboard)
- [Libraries and Tools Used](#libraries-and-tools-used)
  - [Frontend (Next.js)](#frontend-nextjs)
  - [Backend (Django)](#backend-django)
  - [Docker Setup](#docker-setup)
- [Thought Process and Approach](#thought-process-and-approach)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/VishwajithP2308/NextDashboard.git
cd NextDashboard
```

### 2. Set Up Using Docker

This project is containerized using Docker for easier setup and deployment. To start the project using Docker, follow these steps.

#### 2.1 Build and Run the Containers

You will use `docker-compose` to manage and run the backend (Django) and frontend (Next.js) in containers.

1. Build the containers:

```bash
docker-compose up --build
```

This command will build both the **frontend** and **backend** Docker images.

2. Once the build is complete, start the containers:

```bash
docker-compose up
```

This will start both the frontend on `http://localhost:3000` and the backend on `http://localhost:8000`.

The `docker-compose.yml` file contains the configuration for both the Django backend and the Next.js frontend.

### 3. Set Up the Backend (Django)

If you want to run the backend outside of Docker, follow these steps:

Navigate to the Django backend folder:

```bash
cd django-backend
```

Set up a virtual environment (optional but recommended):

```bash
python -m venv env
```

Activate the virtual environment:

- On Mac/Linux:

```bash
source env/bin/activate
```

- On Windows:

```bash
env\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Run migrations (if needed):

```bash
python manage.py migrate
```

Start the Django server:

```bash
python manage.py runserver
```

The backend will now be running on `http://127.0.0.1:8000/`.

### 4. Set Up the Frontend (Next.js with TypeScript and Redux)

If you want to run the frontend outside of Docker, follow these steps:

Navigate to the Next.js frontend folder:

```bash
cd nextjs-frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will now be running on `http://localhost:3000`.

### 5. Visit the Dashboard

Once both the backend and frontend servers are running (whether using Docker or manually), visit `http://localhost:3000/dashboard` to view the dashboard with dynamically populated charts.

---

## Libraries and Tools Used

### Frontend (Next.js with TypeScript)

- **React**: For building the user interface.
- **Next.js**: Framework for React, used for creating API routes and handling server-side rendering.
- **TypeScript**: For adding static type definitions, ensuring code reliability and better development experience.
- **Redux with Redux Toolkit**: For managing global state, handling data flow between components and simplifying the complexity of data management.
- **React-Redux**: For connecting Redux to React components.
- **Axios**: For making HTTP requests to the backend API.
- **Chart.js and react-chartjs-2**: For rendering Line, Bar, and Pie charts.
- **lightweight-charts**: For rendering the Candlestick chart, which is well-suited for financial data visualization.
- **CSS Modules**: For styling components with scoped CSS classes.
- **Jest** (optional): For testing Next.js components and Redux logic.

### Backend (Django)

- **Django**: Backend framework for creating APIs and serving data.
- **Django REST Framework**: For creating and managing the API endpoints.
- **CORS Headers**: To enable Cross-Origin Resource Sharing between the frontend and backend.
- **SQLite**: Lightweight database used in development (you can switch to other databases like PostgreSQL in production).

---

## Docker Setup

The project is fully containerized using **Docker** to simplify deployment and development.

### Docker for Backend (Django)

The `Dockerfile` for the Django backend sets up the following:

- Uses the official **Python 3.9-slim** Docker image.
- Sets the working directory to `/app`.
- Installs dependencies using `pip`.
- Copies the Django project files and exposes port **8000**.

The backend is built and run in a container, allowing you to easily spin up the backend environment.

### Docker for Frontend (Next.js with TypeScript)

The `Dockerfile` for the Next.js frontend sets up the following:

- Uses the official **Node.js 18** Docker image.
- Sets the working directory to `/app`.
- Installs dependencies using `npm`.
- Builds the Next.js app.
- Exposes port **3000** for the development server.

The frontend is built and run in a container, allowing you to quickly start the development environment.

### Docker Compose

The `docker-compose.yml` file orchestrates both the **Django backend** and **Next.js frontend** services:

- The **backend** service builds the Django app and runs it on port **8000**.
- The **frontend** service builds the Next.js app and runs it on port **3000**.
- Volumes are used for both services, allowing you to make changes locally and have them reflected immediately.

---

## Thought Process and Approach

### Modular Structure

- The application is designed with a clear separation of concerns between the frontend and backend. The frontend is responsible for rendering the UI and fetching data, while the backend serves the data via APIs. This ensures maintainability and scalability.

### TypeScript Integration

- **TypeScript** is used throughout the project, enhancing the development process by providing static types and improving code reliability. Type definitions are added to the components and Redux slices to ensure proper data flow.

### Redux for State Management

- **Redux** is used for managing the global state of chart data across components. This ensures that data fetched from the backend APIs is easily shared across different components on the dashboard without excessive prop drilling.
  
### Dynamic Data Fetching

- The frontend fetches data for the charts using **Axios** and **Redux Thunks** for managing side effects, keeping the state in sync with the backend API responses.

### Chart Integration

- **Chart.js** via `react-chartjs-2` is used for rendering **Line**, **Bar**, and **Pie** charts. **Lightweight-charts** is used for the **Candlestick** chart, which is ideal for displaying stock or financial data.
  
### Error Handling and Loading States

- The application handles **loading** and **error states** gracefully. While data is being fetched, a loading spinner is displayed, and if an error occurs (e.g., failed API call), an error message is shown on the dashboard.

### Responsive Design

- The dashboard layout is responsive, adjusting the charts and their layout for different screen sizes. This is achieved using **CSS Grid** and **Flexbox** for layout control.

---

With this setup, the project ensures a clean architecture, scalability, and maintainability using modern technologies like **TypeScript**, **Redux**, and **Docker** for development, deployment, and production.
