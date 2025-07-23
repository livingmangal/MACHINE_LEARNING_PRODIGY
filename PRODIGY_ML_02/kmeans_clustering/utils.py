def save_clustered_data(data, labels, save_path='outputs/clustered_customers.csv'):
    data['Cluster'] = labels
    data.to_csv(save_path, index=False)

