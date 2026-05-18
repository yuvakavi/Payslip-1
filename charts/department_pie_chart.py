import matplotlib.pyplot as plt
import os


def generate_pie_chart(department_costs):

    departments = list(
        department_costs.keys()
    )

    costs = list(
        department_costs.values()
    )

    plt.figure(figsize=(10, 8))

    wedges, texts, autotexts = plt.pie(
        costs,
        labels=departments,
        autopct='%1.1f%%',
        startangle=140,
        wedgeprops={
            'width': 0.4
        }
    )

    plt.title(
        "Department-wise Payroll Cost",
        fontsize=16,
        fontweight='bold'
    )

    plt.legend(
        wedges,
        departments,
        title="Departments",
        loc="lower center",
        bbox_to_anchor=(0.5, -0.1),
        ncol=3
    )

    os.makedirs(
        "outputs/charts",
        exist_ok=True
    )

    chart_path = (
        "outputs/charts/"
        "department_pie_chart.png"
    )

    plt.savefig(
        chart_path,
        bbox_inches='tight'
    )

    plt.close()

    return chart_path
