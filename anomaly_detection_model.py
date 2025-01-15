import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load preprocessed data
def load_data(data_dir="data"):
    X_train = pd.read_csv(f"{data_dir}/X_train.csv")
    X_test = pd.read_csv(f"{data_dir}/X_test.csv")
    y_train = pd.read_csv(f"{data_dir}/y_train.csv").iloc[:, 0]  # Convert to Series
    y_test = pd.read_csv(f"{data_dir}/y_test.csv").iloc[:, 0]  # Convert to Series
    return X_train, X_test, y_train, y_test

# Train Isolation Forest model
def train_model(X_train, contamination=0.1):
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(X_train)
    return model

# Evaluate model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    # Convert Isolation Forest outputs (-1 for anomaly, 1 for normal) to 0/1 for comparison
    y_pred = [0 if pred == 1 else 1 for pred in y_pred]

    # Metrics
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

# Main script
if __name__ == "__main__":
    # Load preprocessed data
    X_train, X_test, y_train, y_test = load_data()

    # Train Isolation Forest
    print("Training Isolation Forest model...")
    model = train_model(X_train)

    # Evaluate the model
    print("\nEvaluating model on test data...")
    evaluate_model(model, X_test, y_test)

    # Save the trained model
    joblib.dump(model, "isolation_forest_model.pkl")
    print("\nModel saved as 'isolation_forest_model.pkl'.")
