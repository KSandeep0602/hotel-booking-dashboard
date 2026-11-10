
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Hotel Booking Analytics",
    page_icon="🏨",
    layout="wide"
)

# ==========================================
# PROFESSIONAL DASHBOARD STYLING
# ==========================================

# Use a consistent Plotly theme
px.defaults.template = "plotly_white"

# Custom CSS
st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: #hbbdwh;
}

/* Main title */
h1 {
    color: #17365d;
    font-weight: 800;
}

/* Section headings */
h2, h3 {
    color: #24476b;
    font-weight: 700;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #hbbdwh;
}

/* KPI metric cards */
div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #dce5f0;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

/* Metric labels */
div[data-testid="stMetricLabel"] {
    color: #52657a;
    font-weight: 600;
}

/* Metric values */
div[data-testid="stMetricValue"] {
    color: #17365d;
    font-weight: 800;
}

/* Dataframe borders */
div[data-testid="stDataFrame"] {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


st.title("🏨 Hotel Booking Analytics")
st.markdown(
    "#### Explore booking trends, cancellation patterns and room pricing."
)

st.caption(
    "An interactive data analytics project using the Hotel Booking Demand dataset."
)

st.divider()

# Load dataset
df = pd.read_csv("hotel_bookings.csv")

# Hotel type filter
st.sidebar.header("Dashboard Filters")

hotel_options = ["All Hotels"] + sorted(df["hotel"].dropna().unique().tolist())

selected_hotel = st.sidebar.selectbox(
    "Select Hotel Type",
    hotel_options
)

# Month filter
month_options = ["All Months"] + [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

selected_month = st.sidebar.selectbox(
    "Select Month",
    month_options
)

# Filter data

# Apply hotel filter
if selected_hotel == "All Hotels":
    filtered_df = df.copy()
else:
    filtered_df = df[df["hotel"] == selected_hotel]

# Apply month filter
if selected_month != "All Months":
    filtered_df = filtered_df[
        filtered_df["arrival_date_month"] == selected_month
    ]

# Dataset overview

# ==========================================
# KPI CARDS
# ==========================================

st.subheader("Hotel Booking Overview")

total_bookings = len(filtered_df)

cancellation_rate = (
    filtered_df["is_canceled"].mean() * 100
    if total_bookings > 0 else 0
)

average_room_rate = (
    filtered_df["adr"].mean()
    if total_bookings > 0 else 0
)

confirmed_bookings = (
    (filtered_df["is_canceled"] == 0).sum()
)

# Display four KPI cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Bookings",
        f"{total_bookings:,}"
    )

with col2:
    st.metric(
        "Cancellation Rate",
        f"{cancellation_rate:.2f}%"
    )

with col3:
    st.metric(
        "Average Room Rate",
        f"{average_room_rate:.2f}"
    )

with col4:
    st.metric(
        "Confirmed Bookings",
        f"{confirmed_bookings:,}"
    )

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())

# Bookings by hotel type
st.subheader("Number of Bookings by Hotel Type")

hotel_counts = (
    filtered_df["hotel"]
    .value_counts()
    .reset_index()
)

hotel_counts.columns = ["Hotel Type", "Bookings"]

fig = px.bar(
    hotel_counts,
    x="Hotel Type",
    y="Bookings",
    color="Hotel Type",
    title="Bookings by Hotel Type"
)

st.plotly_chart(fig, use_container_width=True)





# Monthly Booking Trend
st.subheader("Monthly Booking Trend")

# Create a proper arrival date from the dataset columns
filtered_df["arrival_date"] = pd.to_datetime(
    dict(
        year=filtered_df["arrival_date_year"],
        month=pd.to_datetime(
            filtered_df["arrival_date_month"],
            format="%B"
        ).dt.month,
        day=filtered_df["arrival_date_day_of_month"]
    ),
    errors="coerce"
)

# Count bookings for each month
monthly_bookings = (
    filtered_df.dropna(subset=["arrival_date"])
    .groupby(
        filtered_df["arrival_date"].dt.to_period("M")
    )
    .size()
    .reset_index(name="Bookings")
)

# Convert monthly period into a date for Plotly
monthly_bookings["Month"] = (
    monthly_bookings["arrival_date"].dt.to_timestamp()
)

# Create interactive line chart
fig2 = px.line(
    monthly_bookings,
    x="Month",
    y="Bookings",
    markers=True,
    title="Monthly Hotel Bookings",
    labels={
        "Month": "Month",
        "Bookings": "Number of Bookings"
    }
)

fig2.update_traces(line=dict(width=3))

st.plotly_chart(fig2, use_container_width=True)






# Cancellation Rate by Hotel Type
st.subheader("Cancellation Rate by Hotel Type")

cancellation_data = (
    filtered_df.groupby("hotel")["is_canceled"]
    .mean()
    .reset_index()
)

cancellation_data["Cancellation Rate"] = (
    cancellation_data["is_canceled"] * 100
)

fig3 = px.bar(
    cancellation_data,
    x="hotel",
    y="Cancellation Rate",
    color="hotel",
    text_auto=".2f",
    title="Cancellation Rate by Hotel Type",
    labels={
        "hotel": "Hotel Type",
        "Cancellation Rate": "Cancellation Rate (%)"
    }
)

fig3.update_layout(
    yaxis_title="Cancellation Rate (%)"
)

st.plotly_chart(fig3, use_container_width=True)







# Room Price Distribution
st.subheader("Room Price Distribution")

fig4 = px.histogram(
    filtered_df,
    x="adr",
    nbins=50,
    color="hotel",
    title="Distribution of Average Daily Room Rates",
    labels={
        "adr": "Average Daily Rate",
        "count": "Number of Bookings",
        "hotel": "Hotel Type"
    },
    opacity=0.75
)

fig4.update_layout(
    xaxis_title="Average Daily Rate",
    yaxis_title="Number of Bookings",
    bargap=0.08
)

st.plotly_chart(fig4, use_container_width=True)








# Lead Time vs Cancellation Status
st.subheader("Lead Time vs Cancellation Status")

# Convert cancellation values into readable labels
box_df = filtered_df.copy()

box_df["Booking Status"] = box_df["is_canceled"].map({
    0: "Not Cancelled",
    1: "Cancelled"
})

fig5 = px.box(
    box_df,
    x="Booking Status",
    y="lead_time",
    color="Booking Status",
    title="Lead Time by Booking Status",
    labels={
        "Booking Status": "Booking Status",
        "lead_time": "Lead Time (Days)"
    },
    points="outliers"
)

fig5.update_layout(
    xaxis_title="Booking Status",
    yaxis_title="Lead Time (Days)"
)

st.plotly_chart(fig5, use_container_width=True)










# ==========================================
# CHART 6: CORRELATION HEATMAP
# ==========================================

st.subheader("Correlation Between Numerical Variables")

# Select numerical columns
numeric_columns = [
    "lead_time",
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "adults",
    "children",
    "adr",
    "previous_cancellations",
    "booking_changes",
    "is_canceled"
]

# Calculate correlation values
correlation = filtered_df[numeric_columns].corr()

# Create heatmap
fig6 = px.imshow(
    correlation,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    aspect="auto",
    title="Correlation Heatmap of Hotel Booking Variables"
)

# Improve chart appearance
fig6.update_layout(
    xaxis_title="Variables",
    yaxis_title="Variables",
    height=650
)

# Display chart
st.plotly_chart(fig6, use_container_width=True)

# Explanation
st.caption(
    "Correlation values range from -1 to +1. "
    "Positive values indicate positive relationships, "
    "negative values indicate negative relationships, "
    "and values near zero indicate weak linear relationships. "
    "Correlation does not prove causation."
)
