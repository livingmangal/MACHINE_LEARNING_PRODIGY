import matplotlib.pyplot as plt
import seaborn as sns

def plot_elbow(wcss, save_path='outputs/elbow_plot.png'):
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, len(wcss)+1), wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.savefig(save_path)
    plt.show()
    plt.close()

def plot_clusters(X_scaled, labels, save_path='outputs/cluster_visualization.png'):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=labels, palette='Set2', s=100)
    plt.title('Customer Segments')
    plt.xlabel('Annual Income (scaled)')
    plt.ylabel('Spending Score (scaled)')
    plt.savefig(save_path)
    plt.show()
    plt.close()
