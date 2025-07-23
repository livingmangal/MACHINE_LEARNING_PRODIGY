from sklearn.cluster import KMeans

def find_optimal_clusters(X_scaled, max_k=10):
    wcss = []
    for i in range(1, max_k + 1):
        model = KMeans(n_clusters=i, random_state=42)
        model.fit(X_scaled)
        wcss.append(model.inertia_)
    return wcss

def train_kmeans(X_scaled, k):
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(X_scaled)
    return model, labels
