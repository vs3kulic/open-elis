import pandas as pd
from datetime import datetime
from .models import Therapist, SessionLocal

def parse_date(date_str):
    return datetime.strptime(date_str, '%d.%m.%y').date()

def import_csv_data():
    df = pd.read_csv("datafiles/PTH-CSV-Liste-2025-09-13.csv", sep=';', encoding='cp1252')
    session = SessionLocal()
    
    for index, row in df.iterrows():
        therapist = Therapist(
            last_name=row['Familien-/Nachname'],
            first_name=row['Vorname'] or '',
            title=row['Titel'] or '',
            email=row['Email1'],
            registration_date=parse_date(row['Eintragungdatum']),
            registration_number=int(row['Eintragungs Nummer']),
            state=row['Berufssitz Bundesland 1'],
            postal_code=row['Berufssitz PLZ 1'],
            therapy_methods=row['PTH-Methoden']
        )
        session.add(therapist)
    
    session.commit()
    session.close()
    print(f"Imported {len(df)} therapist records")

if __name__ == "__main__":
    import_csv_data()