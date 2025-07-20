from src.features import prepare_features
from src.model import build_pipeline, train_model, evaluate_model
from src.visualize import plot_predictions
from src.utils import get_user_input

import pandas as pd

# Load data
train_df = pd.read_csv("data/train.csv")

# Prepare features
X, y = prepare_features(train_df)

# Train/test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train model
model = build_pipeline()
train_model(model, X_train, y_train)

# Evaluate model
evaluate_model(model, X_test, y_test)

# Plot predictions
plot_predictions(model, X_test, y_test)

# Predict using user input
user_df = get_user_input()
if user_df is not None:
    predicted_price = model.predict(user_df)[0]
    print(f"💰 Predicted Sale Price: ${predicted_price:,.2f}")
