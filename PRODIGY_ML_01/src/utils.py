import pandas as pd

def get_user_input():
    try:
        grlivarea = float(input("Enter Above Ground Living Area (GrLivArea): "))
        bedrooms = int(input("Enter Number of Bedrooms (BedroomAbvGr): "))
        fullbath = int(input("Enter Number of Full Bathrooms (FullBath): "))
        halfbath = int(input("Enter Number of Half Bathrooms (HalfBath): "))
        total_bath = fullbath + 0.5 * halfbath

        features = ["GrLivArea", "BedroomAbvGr", "TotalBath"]
        user_df = pd.DataFrame([[grlivarea, bedrooms, total_bath]], columns=features)
        return user_df

    except Exception as e:
        print("❌ Error in input. Please enter valid numeric values.")
        print("Details:", e)
        return None
