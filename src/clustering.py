import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def perform_clustering(data, n_clusters=3):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)
    return clusters

import pandas as pd

def save_regime_transitions(clusters, output_path='results/regime_transitions.csv'):
    transitions = pd.DataFrame(clusters, columns=['Regime'])
    transitions['Next_Regime'] = transitions['Regime'].shift(-1)
    transitions = transitions.dropna()
    transitions.to_csv(output_path, index=False)
    print(f"Regime transitions saved to {output_path}")