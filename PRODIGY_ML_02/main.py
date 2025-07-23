from kmeans_clustering.preprocessing import load_data, select_data, scale_data
from kmeans_clustering.model import find_optimal_clusters, train_kmeans
from kmeans_clustering.visualize import plot_elbow, plot_clusters
from kmeans_clustering.utils import save_clustered_data

# Step 1: Load and prepare data
data = load_data('data/Mall_Customers.csv')
X = select_data(data)
X_scaled = scale_data(X)

# Step 2: Find optimal clusters
wcss = find_optimal_clusters(X_scaled)
plot_elbow(wcss)

# Step 3: Train model and assign clusters
k = 3
model, labels = train_kmeans(X_scaled, k)

# Step 4: Save and visualize results
save_clustered_data(data, labels)
plot_clusters(X_scaled, labels)
