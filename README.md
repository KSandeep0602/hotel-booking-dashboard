# 🏨 Hotel Booking Analytics Dashboard

An interactive data visualization dashboard built using Python, Streamlit, Pandas, and Plotly to analyze hotel booking trends, cancellations, and room pricing.

## 📌 Project Overview

This project explores hotel booking data to understand customer booking patterns, cancellation behavior, and room pricing trends.

The dashboard allows users to interactively explore hotel booking information using filters and interactive visualizations.

## 🎯 Project Objectives

- Analyze hotel booking trends.
- Compare City Hotel and Resort Hotel bookings.
- Understand booking cancellation patterns.
- Explore average daily room rates.
- Study relationships between numerical variables.
- Build an interactive analytics dashboard.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit

## 📊 Dashboard Features

### Key Performance Indicators (KPIs)

- Total Bookings
- Cancellation Rate
- Average Room Rate
- Confirmed Bookings

### Interactive Filters

- Hotel Type: All Hotels, City Hotel, Resort Hotel
- Month: All Months or an individual month

### Visualizations

1. Bar Chart – Number of Bookings by Hotel Type
2. Line Chart – Monthly Booking Trends
3. Bar Chart – Cancellation Rate by Hotel Type
4. Histogram – Room Price Distribution
5. Box Plot – Lead Time by Booking Status
6. Heatmap – Correlation Between Numerical Variables

## 📁 Project Structure

```text
hotel-booking-dashboard/
│
├── .streamlit/
│   └── config.toml
│
├── app.py
├── hotel_bookings.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd hotel-booking-dashboard
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the dashboard

```bash
python -m streamlit run app.py
```

The dashboard will open at:

`http://localhost:8501`

## 📂 Dataset

Dataset: Hotel Booking Demand

Source: [Kaggle – Hotel Booking Demand Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

The dataset contains hotel booking records, including hotel type, arrival dates, lead time, cancellation status, guest information, and average daily room rates.

## 📈 Expected Learning Outcomes

- Data analysis using Pandas.
- Data visualization using Plotly.
- Building interactive dashboards with Streamlit.
- Creating filters and KPI metrics.
- Understanding hotel booking patterns and cancellation behavior.

## 👨‍💻 Author

K SANDEEP

## 📌 Project Status

Completed – Interactive Hotel Booking Analytics Dashboard.