# 🧠 KMeans Customer Segmentation

This project uses the K-Means clustering algorithm to segment mall customers based on their **Annual Income** and **Spending Score**.


## 📁 Project Structure

KMeans-Customer-Segmentation/ #replaced by PRODIGY_ML_02 due to internship requirements
│
├── data/
│ └── Mall_Customers.csv # Raw dataset
│
├── outputs/
│ ├── elbow_plot.png # Elbow curve plot
│ ├── cluster_visualization.png # Cluster scatter plot
│ └── clustered_customers.csv # Labeled data
│
├── kmeans_clustering/
│ ├── __init__.py
│ ├── preprocessing.py # Data loading, selection, scaling
│ ├── model.py # KMeans + elbow method
│ ├── utils.py # Saving labeled data
│ └── visualize.py # Plotting functions
│
├── main.py # Main script
├── requirements.txt # Python dependencies
└── README.md # Project overview and instructions


## 📊 Dataset

- Source: [Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
- File: `Mall_Customers.csv`
- Columns used:
  - `Annual Income (k$)`
  - `Spending Score (1-100)`

---

## ⚙️ Setup Instructions

1.  **Clone the repository** or download the project folder.
2.  Place the dataset `Mall_Customers.csv` inside the `data/` directory.
3.  (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate        # Windows: venv\Scripts\activate
    ```
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run the project:
    ```bash
    python main.py
    ```

---

## 📈 Outputs

After running `main.py`, you will get:

| Output File                     | Description                                   |
| :------------------------------ | :-------------------------------------------- |
| `outputs/elbow_plot.png`        | Helps determine optimal clusters (k)          |
| `outputs/cluster_visualization.png` | Visualizes customer segments                  |
| `outputs/clustered_customers.csv` | Dataset with added `Cluster` column           |

---

## 🧠 Techniques Used

* K-Means Clustering
* Elbow Method
* StandardScaler
* Seaborn & Matplotlib for visualization

---

## 📌 Notes

* The number of clusters `k=5` is chosen based on the elbow method result.
* All plots are saved and shown.
* Features are scaled using `StandardScaler` for better clustering.
````