import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler

df = pd.read_csv("data.csv")

X = df[["Weight", "Volume"]]
y = df[["CO2"]]

scalex = scale.fit_transform(X)

regr = linear_model.LinearRegression
regr.fit(X,y)

scaled = scale.transform([[2300, 1.3]])

predictCO2 = scale.predict([scaled[0]])
print(predictCO2)