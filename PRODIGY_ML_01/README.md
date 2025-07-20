# 🏠 House Price Prediction using Linear Regression

**Internship Project** | **Prodigy Infotech**

---

## 📌 Problem Statement

> Implement a Linear Regression model to predict the prices of houses based on their square footage and the number of bedrooms and bathrooms.

This task is part of the **Machine Learning Internship** at **Prodigy Infotech**.

---

## 📊 Dataset Used

- **Source**: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
- **File used**: `train.csv`  
  (Download and place it inside the `data/` folder)

---

## 🚀 Objective

To build a regression model that predicts house prices using basic features like:

- `GrLivArea`: Above ground living area (square feet)
- `BedroomAbvGr`: Number of bedrooms above ground
- `FullBath`: Number of full bathrooms
- `HalfBath`: Number of half bathrooms

Additionally, a derived feature is created:

- `TotalBath = FullBath + 0.5 × HalfBath`

---

## 📂 Project Structure

```bash
house-price-predictor/
├── data/
│   └── train.csv              # Dataset file
│
├── src/
│   ├── features.py            # Feature engineering
│   ├── model.py               # Model training & evaluation
│   ├── visualize.py           # Visualization (scatter plot)
│   └── utils.py               # User input handling
│
├── app.py                     # Main application script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

## ⚙️ Tech Stack
Python 3.13.0

Pandas – for data manipulation

Scikit-learn – for machine learning

Matplotlib – for data visualization

## 🧠 Model Workflow
Data Preprocessing

Handle missing values using SimpleImputer with median strategy

Create the derived feature TotalBath

Modeling

Use LinearRegression from scikit-learn

Combine preprocessing and modeling into a Pipeline

Evaluation

Train/test split (80/20)

Evaluation metrics:

Mean Squared Error (MSE)

R² Score

Visualization

Scatter plot of Actual vs Predicted Sale Price

User Prediction

Accept user input from command line and predict price

## 📈 Sample Output
📊 Model Evaluation:
✅ Mean Squared Error (MSE): 2848523443.42
✅ R² Score: 0.6286

🏡 Enter details to predict house SalePrice:
Enter Above Ground Living Area (GrLivArea): 1500
Enter Number of Bedrooms (BedroomAbvGr): 3
Enter Number of Full Bathrooms (FullBath): 2
Enter Number of Half Bathrooms (HalfBath): 1

💰 Predicted Sale Price: $192,315.75

## 📦 Requirements
All required Python libraries are listed in requirements.txt:
pandas
scikit-learn
matplotlib

## 📁 3. Add Dataset
Download the dataset train.csv from Kaggle

Place it inside the data/ folder

##▶️ 4. Run the Application
python app.py

Enter the requested inputs when prompted

Get the predicted house price in the terminal

🙋‍♂️ Author
Mangal
Machine Learning Intern
Prodigy Infotech

