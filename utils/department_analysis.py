from collections import defaultdict
from utils.salary_utils import calculate_salary


def calculate_department_costs(employees):

    department_costs = defaultdict(float)

    for emp in employees:

        salary = calculate_salary(emp)

        department = emp.get(
            "department",
            "Unknown Department"
        )

        department_costs[department] += salary

    return dict(department_costs)