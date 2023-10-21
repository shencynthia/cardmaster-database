import firebase_admin
from firebase_admin import credentials, firestore

# Use the service account key you downloaded from Firebase Console
cred = credentials.Certificate('service_account_key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
