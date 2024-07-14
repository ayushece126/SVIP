
import pandas as pd

def preprocess_data():
    interactions = pd.read_csv('data/user_interactions.csv')
    metadata = pd.read_csv('data/content_metadata.csv')
    connections = pd.read_csv('data/social_connections.csv')
    # Preprocess the data
    return interactions, metadata, connections

if __name__ == "__main__":
    interactions, metadata, connections = preprocess_data()
    print("Data preprocessed successfully!")
