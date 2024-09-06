Dashboard Application with Next.js Frontend and Django Backend
Overview
This project is a dashboard built using Next.js on the frontend and Django on the backend. The dashboard displays four different types of charts: Candlestick, Line, Bar, and Pie, with data fetched dynamically from the backend. The frontend integrates charting libraries to provide clear and responsive data visualizations.


---

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/VishwajithP2308/NextDashboard.git
cd NextDashboard

### 2. Set Up the Backend (Django)

1. Navigate to the Django backend folder:
   cd django-backend

2. Set up a virtual environment (optional but recommended):
   python -m venv env
   use source env/bin/activate On Mac/Linux
   use env/Scripts/activate On Windows

4. Install dependencies:
   pip install -r requirements.txt

5. Run migrations (if needed):
   python manage.py migrate

6. Start the Django server:
   python manage.py runserver

The backend will now be running on `http://127.0.0.1:8000/`.

### 3. Set Up the Frontend (Next.js)

1. Navigate to the Next.js frontend folder:
   cd ../nextjs-frontend

2. Install frontend dependencies:
   npm install

3. Start the development server:
   npm run dev

The frontend will now be running on `http://localhost:3000`.

### 4. Visit the Dashboard

Once both the backend and frontend servers are running, visit `http://localhost:3000/dashboard` to view the dashboard with dynamically populated charts.

---

Libraries and Tools Used
Frontend (Next.js)
React: For building the user interface.
Next.js: Framework for React, used for creating API routes and handling server-side rendering.
Axios: For making HTTP requests to the backend API.
Chart.js: For rendering Line, Bar, and Pie charts.
lightweight-charts: For rendering the Candlestick chart.
CSS Modules: For styling components.
Backend (Django)
Django: Backend framework for creating APIs and serving data.
Django REST Framework: For creating and managing the API endpoints.
CORS Headers: To enable Cross-Origin Resource Sharing between the frontend and backend.
Thought Process and Approach
Modular Structure: The application is designed to separate concerns between the frontend and backend. The frontend is responsible for displaying the data, while the backend serves the data through APIs.

Dynamic Data Fetching: The frontend uses Next.js API routes to act as intermediaries between the frontend and backend. Data for the charts is fetched dynamically from the Django backend, ensuring a clean separation of concerns.

Chart Integration: The react-chartjs-2 library is used for rendering the Line, Bar, and Pie charts, while lightweight-charts is used for the Candlestick chart due to its suitability for financial data visualization.

Error Handling and Loading States: The application handles loading and error states gracefully. When the data is being fetched, a loading spinner is displayed, and any errors during API requests are displayed on the dashboard.

Responsive Design: The dashboard layout is responsive, ensuring that the charts adjust appropriately for different screen sizes. This was achieved using CSS Grid/Flexbox layouts.

