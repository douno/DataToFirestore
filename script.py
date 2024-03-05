import firebase_admin
import pandas as pd
from firebase_admin import credentials, firestore

cred = credentials.Certificate(
    "YOUR_SERVICE_ACCOUNT_KEY.json"
)
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://pythonfirebase.firebaseio.com/"}
)

db = firestore.client()
doc_ref = db.collection("applications")

# Import data
df = pd.read_csv("PPP_data.csv")
tmp = df.to_dict(orient="records")
list(map(lambda x: doc_ref.add(x), tmp))
