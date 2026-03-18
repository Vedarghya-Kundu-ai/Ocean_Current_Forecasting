import pandas as pd
import joblib as jb

latitude = -106.99689357156068
longitude = -19.883349669231674
uo = -0.06241639
vo = -0.01782307

input_labels = ["latitude", "longitude", "uo", "vo"]
input_data = pd.DataFrame([[latitude, longitude, uo, vo ]], columns=input_labels)

model = jb.load("ocean_current_model.pkl")
y_predict = model.predict(input_data)

print(f"Your predicted East-West ocean current velocity is = {y_predict[0][0]}")
print(f"Your predicted North-South ocean current velocity is = {y_predict[0][1]}")
