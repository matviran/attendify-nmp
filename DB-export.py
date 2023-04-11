import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("attendify-firebase-adminsdk-serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://attendify-nomoreproxies-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Students')

data = {
    '20220802065':{
        'name' : 'Onkar Yaglewad',
        'major' : 'B Tech CSE',
        'starting_year' : 2022,
        'total_attendance' : 6,
        'year' : 4,
        'last_attendance_time' : '2023-4-10 00:54:34'
    }
}


for key, value in data.items():
    ref.child(key).set(value)
