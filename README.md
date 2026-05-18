# Accountant agent- LangGraph Based Payroll Analytics System

A LangGraph-based payroll automation system that generates employee payslips in PDF and JSON format and provides department-wise payroll expenditure analytics using interactive dashboards and pie chart visualizations.

---

#  Features

##  Payroll Automation
- Employee salary calculation
- Intern performance-based salary calculation
- Leave deduction handling
- Automated PDF payslip generation
- JSON payslip output generation

##  Department-wise Payroll Analytics
- Department expenditure calculation
- Total company payroll analytics
- Employee count analytics
- Department filtering
- Interactive dashboard analytics

##  Visualization
- Static PNG pie chart using Matplotlib
- Interactive donut pie chart using Streamlit + Plotly

---

#  Project Architecture

```plaintext
Payslip/
│
├── agents/
│   └── payroll_graph.py
│
├── nodes/
│   ├── fetch_node.py
│   ├── calculate_node.py
│   └── pdf_node.py
│
├── utils/
│   ├── pdf_generator.py
│   ├── json_generator.py
│   ├── salary_utils.py
│   └── department_analysis.py
│
├── charts/
│   └── department_pie_chart.py
│
├── data/
│   └── mock_data.py
│
├── outputs/
│   ├── payslips/

├── dashboard.py
├── main.py
├── requirements.txt
└── README.md
```

---

#  LangGraph Workflow

```plaintext
START
   ↓
Fetch Employee Data
   ↓
Calculate Salary
   ↓
Generate PDF Payslip
   ↓
END
```

---

#  Payroll Calculation Logic

##  Employee Salary Logic

```plaintext
Final Salary = Fixed Pay − (Fixed Pay × Leaves / 30)
```

### Example
- Fixed Pay = Rs. 60,000
- Leaves = 2

```plaintext
Deduction = 60000 × 2 / 30 = 4000
Final Salary = 56000
```

---

##  Intern Salary Logic

```plaintext
Final Salary = Performance Points × Rate Per Point
```

### Example
- Performance Points = 45
- Rate Per Point = Rs. 100

```plaintext
Final Salary = 45 × 100 = Rs. 4500
```

---

#  Department Expenditure Calculation

The system calculates organization expenditure by aggregating:
- Employee salaries
- Intern performance payments

for each department.

### Formula

```plaintext
Department Expenditure =
Σ(Employee Salaries)
+
Σ(Intern Salaries)
```

---

#  Dashboard Features

- Total Company Payroll
- Employee Count
- Department Filter
- Department-wise Expenditure Table
- Employee Details Table
- Interactive Donut Pie Chart

---

#  Visualization Types

## Interactive Dashboard
Built using:
- Streamlit
- Plotly

Features:
- Interactive hover analytics
- Department filtering
- Real-time expenditure visualization

Run using:

```bash
streamlit run dashboard.py
```

---

# 🏢 Supported Departments

- Python Django
- Manual Testing
- Digital Marketing
- NodeJS Web Developers
- MERN Stack
- React Native
- Associate HR
- Graphic Designing
- Business Analysis
- Human Resources
- UI / UX Designing
- BBD Captain
- Bunny Team
- Accounting
- Networking Automation

---

#  Output Formats

## PDF Payslip
Generated for:
- Employees
- Interns

Stored in:

```plaintext
outputs/payslips/
```

---

##  JSON Output

Example:

```json
{
    "name": "Ram",
    "department": "Python Django",
    "role": "employee",
    "final_salary": 56000
}
```

---

#  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| LangGraph | Workflow Orchestration |
| LangChain | AI Framework |
| ReportLab | PDF Generation |
| Pandas | Data Handling |
| Plotly | Interactive Charts |
| Streamlit | Dashboard |

---

# ⚙️ Installation

## 1 Clone Repository

```bash
git clone https://github.com/yuvakavi/Payslip.git
```

---

## 2 Move to Project Folder

```bash
cd Payslip
```

---

## 3 Create Virtual Environment

```bash
python -m venv .venv
```

---

## 4 Activate Virtual Environment

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

---

## 5️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Run Project

## Run Payroll Generator

```bash
python main.py
```

---

## Run Dashboard

```bash
streamlit run dashboard.py
```

---

#  requirements.txt

```txt
langgraph
langchain
reportlab
matplotlib
streamlit
plotly
pandas
```
#  Conclusion

This project demonstrates a complete payroll automation and analytics workflow using LangGraph, PDF generation, JSON APIs, department-wise expenditure calculation, and interactive dashboard visualization.
