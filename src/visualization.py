import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
import numpy as np

def plot_pca_3d(data, clusters, output_path='results/figures/pca_3d.png'):
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(data)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    scatter = ax.scatter(pca_result[:, 0], pca_result[:, 1], pca_result[:, 2], c=clusters, cmap='viridis', s=10)
    fig.colorbar(scatter, ax=ax, label='Cluster')
    
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_zlabel('PC3')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    plt.close()

def plot_regime_timeline(timestamps, clusters, output_path='results/figures/regime_timeline.png'):
    df = pd.DataFrame({'Time': pd.to_datetime(timestamps), 'Regime': clusters})
    df['Time'] = df['Time'].dt.floor('min')
    df = df.groupby('Time').agg(lambda x: x.mode()[0]).reset_index()
    plt.figure(figsize=(16, 2))
    sns.heatmap([df['Regime']], cmap='tab10', cbar=True, xticklabels=300)
    plt.title('Regime Timeline')
    plt.yticks([])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    plt.close()

def plot_price_with_regimes(timestamps, prices, clusters, output_path='results/figures/price_regime_overlay.png'):
    df = pd.DataFrame({'Time': pd.to_datetime(timestamps), 'Price': prices, 'Regime': clusters})
    plt.figure(figsize=(16, 6))
    scatter = plt.scatter(df['Time'], df['Price'], c=df['Regime'], cmap='tab10', s=1)
    plt.colorbar(scatter, label='Regime')
    plt.title('Price with Regime Overlay')
    plt.xlabel('Time')
    plt.ylabel('Mid Price')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    plt.close()

def plot_transition_matrix(clusters, output_path='results/figures/transition_matrix.png'):
    le = LabelEncoder()
    encoded = le.fit_transform(clusters)
    n_states = len(set(encoded))
    trans_mat = np.zeros((n_states, n_states))
    for (i, j) in zip(encoded[:-1], encoded[1:]):
        trans_mat[i, j] += 1
    trans_mat = trans_mat / trans_mat.sum(axis=1, keepdims=True)
    plt.figure(figsize=(6, 5))
    sns.heatmap(trans_mat, annot=True, cmap='Blues', fmt=".2f")
    plt.xlabel('Next Regime')
    plt.ylabel('Current Regime')
    plt.title('Markov Regime Transition Matrix')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    plt.close()