import pandas as pd

# Training data
X_train = pd.DataFrame({
    "feature1": [1.1, 1.2, 1.3, 10.0, 1.5, 1.4],
    "feature2": [2.2, 2.3, 2.1, 10.0, 2.4, 2.3]
})
y_train = pd.DataFrame({"Label": [0, 0, 0, 1, 0, 0]})

# Test data
X_test = pd.DataFrame({
    "feature1": [1.2, 1.1, 1.3, 50.0, 1.4, 1.5],
    "feature2": [2.3, 2.2, 2.1, 50.0, 2.2, 2.3]
})
y_test = pd.DataFrame({"Label": [0, 0, 0, 1, 0, 0]})

# Save to CSV
X_train.to_csv("X_train.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("CSV files created successfully!")