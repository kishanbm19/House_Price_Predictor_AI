import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv("dataset.csv")

x=data[['Size','Bedrooms','Age']]
y=data['Price']
model=LinearRegression()

#Train model
model.fit(x,y)
print("Model Trained successfully")
size=float(input("Enter House size(sqft):"))
bedrooms=float(input("Enter the number of bedrooms "))
age=float(input("Enter the House age:"))
prediction=model.predict([[size,bedrooms,age]])


print(f"\nHouse Price is-> ₹{prediction[0]:.2f} Lakhs" )




