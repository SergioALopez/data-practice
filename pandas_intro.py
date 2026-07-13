import pandas as pd

# Create a DataFrame from a list of dictionaries
# - same structure as your students data from before
data = [
    {"name": "Sergio", "age": 29, "grade": "A", "score": 88},
    {"name": "Maria", "age": 22, "grade": "B", "score": 74},
    {"name": "Carlos", "age": 35, "grade": "A", "score": 91},
    {"name": "Ana", "age": 28, "grade": "C", "score": 61},
    {"name": "Luis", "age": 31, "grade": "B", "score": 78},
    {"name": "Sofia", "age": 24, "grade": "A", "score": 95},
]

df = pd.DataFrame(data)

# --- EXPLORING THE DATAFRAME ---
print("=== Full Dataframe ===")
print(df)

print("\n=== Shape (rows, columns) ===")
print(df.shape)

print("\n=== Column names ===")
print(df.columns.tolist())

print("\n=== Quick statistics ===")
print(df.describe())

print("\n=== First 3 rows ===")
print(df.head(3))

# --- FILTERING ---
print("\n=== Grade A Students ===")
grade_a = df[df["grade"] == "A"]        # Pattern to filter -> df[df["column"] condition]
print(grade_a)

print("\n=== Students with score above 80 ===")
high_scorers = df[df["score"] > 80]
print(high_scorers)

# --- SORTING ---
print("\n=== Sorted by score (highest first) ===")
print(df.sort_values("score", ascending=False))

# --- SELECTING COLUMNS ---
print("\n=== Names and scores only ===")
print(df[["name", "score"]])