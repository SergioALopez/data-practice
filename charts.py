import pandas as pd
import matplotlib.pyplot as plt

data = [
    {"name": "Sergio", "age": 29, "grade": "A", "score": 88},
    {"name": "Maria", "age": 22, "grade": "B", "score": 74},
    {"name": "Carlos", "age": 35, "grade": "A", "score": 91},
    {"name": "Ana", "age": 28, "grade": "C", "score": 61},
    {"name": "Luis", "age": 31, "grade": "B", "score": 78},
    {"name": "Sofia", "age": 24, "grade": "A", "score": 95},
]

df = pd.DataFrame(data)

# Bar chart of scores
plt.figure(figsize=(8, 5))
plt.bar(df["name"], df["score"], color="steelblue")
plt.title("Student Scores")
plt.xlabel("Student")
plt.ylabel("Scores")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("scores_bar.png")
plt.show()
print("Chart saved as 'scores_bar.png'!")

# --- CHART 2: Pie chart of grade distribution ---
grade_counts = df["grade"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%", colors=["steelblue", "orange", "green"])
plt.title("Grade Distribution")
plt.tight_layout()
plt.savefig("grades_pie.png")
plt.show()
print("Chart 2 saved!")

# CHART 3: Scatter plot - age vs score ---
plt.figure(figsize=(8, 5))
plt.scatter(df["age"], df["score"], color="purple", s=100)
for i, row in df.iterrows():
    plt.annotate(row["name"], (row["age"], row["score"]), textcoords="offset points", xytext=(8, 4))
plt.title("Age vs Score")
plt.xlabel("Age")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("age_vs_score.png")
plt.show()
print("Chart 3 saved")