import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import joblib


# Step 1: Simulate network traffic data
def generate_synthetic_data(num_samples=1000):
    #np.random.seed(42) #added comment to deactivate fixed seed so data is different on every generation, remove comment to ensure same data generation

    # Features: [Packet Size, Duration, Source Port, Destination Port, Protocol]
    normal_data = np.random.normal(loc=50, scale=10, size=(num_samples, 5))
    anomaly_data = np.random.normal(loc=100, scale=20, size=(int(num_samples * 0.1), 5))

    # Combine normal and anomaly data
    data = np.vstack((normal_data, anomaly_data))
    labels = np.hstack((np.zeros(num_samples), np.ones(int(num_samples * 0.1))))

    return pd.DataFrame(data, columns=['Packet_Size', 'Duration', 'Src_Port', 'Dst_Port', 'Protocol']), labels


# Step 2: Clean and prepare data
def preprocess_data(data, labels):
    """
    Cleans and prepares the dataset for processing:
    - Adds labels to the dataset.
    - Removes duplicates and missing values.
    - Separates features (X) and labels (y).
    """
    # Add labels to the DataFrame
    data['Label'] = labels

    # Remove duplicates if any
    data.drop_duplicates(inplace=True)

    # Remove missing or invalid values
    data.dropna(inplace=True)

    # Separate features and labels
    X = data.drop(columns=['Label'])
    y = data['Label']

    return X, y


# Step 3: Normalize data
def normalize_data(X):
    """
    Normalizes the feature data using StandardScaler.
    Returns the scaled data and the scaler for later reuse.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler


# Step 4: Split data into training and test sets
def split_data(X, y, test_size=0.2, random_state=42):
    """
    Splits the data into training and test sets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


# Step 5: Save processed data
def save_data(X_train, X_test, y_train, y_test, scaler, output_dir="processed_data"):
    """
    Saves the processed datasets and scaler to disk for reuse.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Save datasets
    pd.DataFrame(X_train, columns=['Packet_Size', 'Duration', 'Src_Port', 'Dst_Port', 'Protocol']).to_csv(
        os.path.join(output_dir, "X_train.csv"), index=False
    )
    pd.DataFrame(X_test, columns=['Packet_Size', 'Duration', 'Src_Port', 'Dst_Port', 'Protocol']).to_csv(
        os.path.join(output_dir, "X_test.csv"), index=False
    )
    pd.Series(y_train).to_csv(os.path.join(output_dir, "y_train.csv"), index=False, header=True)
    pd.Series(y_test).to_csv(os.path.join(output_dir, "y_test.csv"), index=False, header=True)

    # Save the scaler for reuse
    joblib.dump(scaler, os.path.join(output_dir, "scaler.pkl"))


# Main script
if __name__ == "__main__":
    # Generate synthetic data
    data, labels = generate_synthetic_data()

    # Preprocess data
    X, y = preprocess_data(data, labels)

    # Normalize data
    X_normalized, scaler = normalize_data(X)

    # Split data
    X_train, X_test, y_train, y_test = split_data(X_normalized, y)

    # Save processed data
    save_data(X_train, X_test, y_train, y_test, scaler)

    # Display results
    print("Training set size:", X_train.shape)
    print("Test set size:", X_test.shape)
    print("First few training examples:")
    print(pd.DataFrame(X_train[:5], columns=['Packet_Size', 'Duration', 'Src_Port', 'Dst_Port', 'Protocol']))
