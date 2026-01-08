import pandas as pd
from pymongo import MongoClient
import time

def run_migration():
    # 1. Connexion à MongoDB Local
    time.sleep(10)
    client = MongoClient("mongodb://mongodb:27017/")
    db = client["Healthcare"]
    collection = db["Patients"]

    # 2. Chargement du CSV
    print("Chargement du fichier CSV")
    df = pd.read_csv("healthcare_dataset.csv")

    # 3. Nettoyage et Conversion 
    # On convertit les colonnes de dates pour MongoDB
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    
    # On s'assure que le montant est bien un nombre décimal
    df['Billing Amount'] = df['Billing Amount'].astype(float)

    # 4. Transformation en format JSON (Dictionnaires)
    data_to_insert = df.to_dict(orient='records')

    # 5. Insertion dans la base
    collection.delete_many({}) # Vide la collection avant de remplir
    print(f"Insertion de {len(data_to_insert)} documents dans MongoDB")
    collection.insert_many(data_to_insert)
    
    print(" Migration réussie ")

if __name__ == "__main__":
    run_migration()