import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("attendify-firebase-adminsdk-serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://attendify-nomoreproxies-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Students')