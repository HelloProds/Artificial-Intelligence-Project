import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
from data_preprocessing import generate_synthetic_data, preprocess_data, normalize_data, split_data


# Step 1: Train an Isolation Forest model
def train_model(X_train):
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(X_train)
    return model


# Step 2: Predict and evaluate the model
def evaluate_model(model, X_test, y_test):
    # Predict anomaly scores (-1: anomaly, 1: normal)
    predictions = model.predict(X_test)

    # Convert predictions to binary (1: anomaly, 0: normal)
    binary_predictions = np.where(predictions == -1, 1, 0)

    # Generate evaluation metrics
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, binary_predictions))
    print("\nClassification Report:")
    print(classification_report(y_test, binary_predictions))


# Main script
if __name__ == "__main__":
    # Preprocess and split the data
    data, labels = generate_synthetic_data()
    X, y = preprocess_data(data, labels)
    X_normalized, scaler = normalize_data(X)
    X_train, X_test, y_train, y_test = split_data(X_normalized, y)

    # Train the Isolation Forest model
    model = train_model(X_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Example of predicting on new data
    print("\nTesting a new sample:")
    sample = pd.DataFrame([[50, 60, 5000, 6000, 1]],
                          columns=['Packet_Size', 'Duration', 'Src_Port', 'Dst_Port', 'Protocol'])
    scaled_sample = scaler.transform(sample)  # Normalize using the earlier scaler
    prediction = model.predict(scaled_sample)
    print("Prediction for the sample:", "Anomaly" if prediction[0] == -1 else "Normal")

