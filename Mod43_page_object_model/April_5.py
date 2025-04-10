import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(
    {
        "Department": ["HR", "IT", "Finance", "HR", "IT"],
        "Salary": [70000, 80000, 75000, 71000, 82000],
        "Age": [70, 80, 75, 71, 82],
    }
)

sns.barplot(x="Department", y="Salary", data=data)
plt.title("Average Salary by Department")
plt.show()

sns.lmplot(x="Age", y="Salary", data=data)
plt.title("Salary vs. Age")
plt.show()

sns.boxplot(x="Department", y="Salary", data=data)
plt.title("Salary Distribution by Department")
plt.show()

corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
