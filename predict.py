import pandas as pd
import joblib

model=joblib.load("models/house_price_model.pkl")





Area=float(input("Enter House size(sqft):"))
bedrooms=float(input("Enter the number of bedrooms: "))
bathrooms=float(input("Enter the number of bathrooms "))
parking=int(input("Enter the number of available parking lots: "))
age=float(input("Enter the House age:"))

new_house=pd.DataFrame({
    "Area":[Area],
    "Bedrooms":[bedrooms],
    "Bathrooms":[bathrooms],
    "Parking":[parking],
    "Age":[age]


})

prediction=model.predict(new_house)


print(f"\nHouse Price is-> ₹{prediction[0]:.2f}" )
