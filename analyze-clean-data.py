import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

df = pd.read_csv('C:/Users/Sachar/Desktop/Coding/Data Scince R/AI-Project/lung_disease_data.csv', header=0, sep=',')

columns = df.info()

diseases = df["Disease Type"].unique()

# diseases = COPD, Bronchitis, Asthma, Lung cancer, Pneumonia

Age = df["Age"].unique()

NanRows = df[df.isna().any(axis=1)]

#plt.pie(ageGroups, labels=diseases, colors=["red", "yellow", "green", "blue", "orange"], autopct='%1.1f%%')

# print(NanRows)
# print(np.sort(Age))
# print(df["Age"].value_counts())

print(df["Gender"].unique()) #Male, Female
print(df["Smoking Status"].unique()) #No, yes
print(df["Disease Type"].unique()) #COPD, Bronchitis, Asthma, Lung cancer, Pneumonia
print(df["Treatment Type"].unique()) #Therapy, Surgery, Medication
print(df["Hospital Visits"].unique()) #float
print(df["Recovered"].unique()) #yes, no
print(df["Lung Capacity"].unique()) #float

# how many people were tested:
def peopleTestedByAge(df):
    Groups = []
    for i in range(2,9):
        count = df["Age"].loc[(df["Age"]<(i+1)*10) & (df["Age"]>(i)*10)].count()
        Groups.append(count)
    return Groups
        






groupsResult = peopleTestedByAge(df)
labels = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"]
colors = ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#955251", "#B565A7"]

# Create the main figure with GridSpec for layout control
fig = plt.figure(figsize=(12, 6))
gs = GridSpec(2, 2, width_ratios=[1, 3], height_ratios=[1, 1])  # 1:2 ratio for left and right plots

# Create the bar plot (left upper corner)
ax_bar = fig.add_subplot(gs[0,0])
ax_bar.barh(labels, groupsResult, color=colors, height=0.8)
ax_bar.set_title("Count per Age Group", fontsize=12, fontweight='bold', pad=10)
ax_bar.set_xlabel("Count", fontsize=10)
ax_bar.tick_params(axis='both', labelsize=8)

# Remove spines for a clean look
for spine in ax_bar.spines.values():
    spine.set_visible(False)

# Create the pie chart (middle right)
ax_pie = fig.add_subplot(gs[:,1])
wedges, texts, autotexts = ax_pie.pie(
    groupsResult,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(edgecolor='w', linewidth=2),
    radius=1.0  # Reduce pie size slightly
)

# Adjust label underlines (correct size and position)
for i, wedge in enumerate(wedges):
    angle = (wedge.theta2 + wedge.theta1) / 2.0
    x = np.cos(np.deg2rad(angle))
    y = np.sin(np.deg2rad(angle))
    
    
    horizontal_alignment = "left" if x >= 0 else "right"
    connection_style = f"angle,angleA=0,angleB={angle:.0f}"

    ax_pie.annotate(
        labels[i],
        xy=(x, y),
        xytext=(1.35 * np.sign(x), 1.4 * y),
        horizontalalignment=horizontal_alignment,
        arrowprops=dict(
            arrowstyle="-",
            connectionstyle=connection_style,
            color=colors[i],
            lw=1.5
        ),
        fontsize=12,
        fontweight='bold'
    )

# Add a title for the pie chart
ax_pie.set_title("Patients Tested by Age", fontsize=16, fontweight='bold', pad=20)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()