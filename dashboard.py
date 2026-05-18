import streamlit as st
import plotly.express as px
import pandas as pd

from data.mock_data import mock_employees
from utils.department_analysis import (
    calculate_department_costs
)

# ---------------- PAGE TITLE ----------------

st.title("Payroll Analytics Dashboard")


# ---------------- DEPARTMENT COSTS ----------------

department_costs = (
    calculate_department_costs(
        mock_employees
    )
)

departments = list(
    department_costs.keys()
)

costs = list(
    department_costs.values()
)

# Create dataframe
df = pd.DataFrame({
    "Department": departments,
    "Cost": costs
})


# ---------------- TOTAL COMPANY PAYROLL ----------------

total_payroll = sum(costs)

st.metric(
    "Total Company Payroll",
    f"Rs. {round(total_payroll, 2)}"
)


# ---------------- DEPARTMENT FILTER ----------------

selected_department = st.selectbox(
    "Select Department",
    ["All Departments"] + departments
)


# ---------------- FILTERED EMPLOYEE DATA ----------------

if selected_department == "All Departments":

    filtered_employees = mock_employees

else:

    filtered_employees = [

        emp for emp in mock_employees

        if emp["department"] == selected_department
    ]


# ---------------- EMPLOYEE COUNT ----------------

employee_count = len(filtered_employees)

st.metric(
    "Employee Count",
    employee_count
)


# ---------------- EMPLOYEE TABLE ----------------

st.subheader("Employee Details")

employee_df = pd.DataFrame(
    filtered_employees
)

st.dataframe(employee_df)


# ---------------- DEPARTMENT EXPENDITURE TABLE ----------------

st.subheader("Department Expenditure")

st.dataframe(df)


# ---------------- PIE CHART ----------------

fig = px.pie(
    df,
    names="Department",
    values="Cost",
    hole=0.5,
    title="Department-wise Payroll Cost"
)

st.plotly_chart(fig)