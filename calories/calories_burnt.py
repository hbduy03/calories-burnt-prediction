from datetime import datetime

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os
from config import DATA1_PATH, DATA2_PATH, MODEL_PATH, RECORD_PATH


def khoitao():
    data1 = pd.read_csv(DATA1_PATH)
    data2 = pd.read_csv(DATA2_PATH)

    df = pd.merge(data1, data2, how='inner', on='User_ID')
    df['Gender'] = LabelEncoder().fit_transform(df['Gender'])

    x = df.drop(columns= ['User_ID' ,'Calories'],  axis=1)
    y = df['Calories']

    x_train, x_test, y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=888)

    model = RandomForestRegressor()

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Độ lệch chuẩn: {mae:.2f} Kcal")

    joblib.dump(model, MODEL_PATH)

def CaloriesBurnt_Predict(input: dict):
    if not os.path.exists(MODEL_PATH):
        khoitao()
    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame([input])
    df['Gender'] = LabelEncoder().fit_transform(df['Gender'])

    feature_cols = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
    df_pre = df[feature_cols]
    kq = model.predict(df_pre)[0]
    print(f'Dự đoán lượng calories tiêu thụ: {kq:.2f} Kcal')
    df['Calories'] = kq
    df['Timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(RECORD_PATH):
        df.to_csv(RECORD_PATH, mode='a', header=False, index=False)
    else:
        df.to_csv(RECORD_PATH, index=False)
    return kq



