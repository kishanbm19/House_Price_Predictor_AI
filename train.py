import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from preprocess import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score




data=pd.read_csv("dataset/house_prices.csv")


x,y=preprocess_data(data)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()

#Train model
model.fit(x_train,y_train)
y_predict=model.predict(x_test)

mse=mean_squared_error(y_predict,y_test)
r2=r2_score(y_test,y_predict)
print("\n Model Performance \n")
print(f"Mean square error : {mse:.2f}")
print(f"R2 score: {r2:.2f}")

# for saving the model

joblib.dump(model,"models/house_price_model.pkl")


print("Model Trained and saved successfully")




