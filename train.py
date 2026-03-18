import xarray as xr
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from sklearn.metrics import r2_score

dataset = xr.open_dataset(
    "cmems_obs-mob_glo_phy-cur_my_0.25deg_P1D-m_multi-vars_179.88W-179.88E_89.88S-89.88N_0.00m_2020-12-31-2023-12-31.nc"
)

subset = dataset.sel(longitude=slice(30, 50), latitude=slice(-40, 10))

df = subset[["uo", "vo"]].compute().to_dataframe().reset_index()
df = df.dropna(subset=["uo", "vo"])

df_next_day = df.copy()
df_next_day['time'] = df_next_day["time"] - pd.Timedelta(days=1)
df_next_day = df_next_day.rename(columns={"uo": "uo_next", "vo": "vo_next"})

df_merged = df.merge(df_next_day, on=["time", "latitude", "longitude"], how="inner")
df_merged = df_merged.dropna()
df_merged = df_merged.astype({"latitude": "float32", "longitude": "float32", "uo": "float32", "vo": "float32"})
df_merged = df_merged.sample(n=100000)
# print(df_merged.head())

""" model = RandomForestRegressor(n_estimators=100)

features = df_merged[["latitude", "longitude", "uo", "vo"]]
labels = df_merged[["uo_next", "vo_next"]]

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

model.fit(X_train, y_train)
model = joblib.dump(model, "ocean_current_model.pkl") """
features = df_merged[["latitude", "longitude", "uo", "vo"]]
labels = df_merged[["uo_next", "vo_next"]]
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
model = joblib.load("ocean_current_model.pkl")

y_predict = model.predict(X_test)
score = r2_score(y_test, y_predict)
# print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
print(f"Your model has a {score*100}% accuracy")

