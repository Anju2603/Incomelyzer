import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df=pd.read_csv("income_data.csv")
df.drop("Income",axis=1,inplace=True)

label_encoders={}
for col in ['Occupation','HouseType','Education','Area','Bracket']:
    le=LabelEncoder()
    df[col]=le.fit_transform(df[col])
    label_encoders[col]=le
    
X=df.drop("Bracket",axis=1)
y=df["Bracket"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=RandomForestClassifier()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print("Accuracy:", accuracy_score(y_test,y_pred))

joblib.dump(model,"income_model.pkl")
joblib.dump(label_encoders,"encoders.pkl")