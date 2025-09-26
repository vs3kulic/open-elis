import pandas as pd
from datetime import datetime
from .models import Therapist, TherapyMethod, SessionLocal

def parse_date(date_str):
    return datetime.strptime(date_str, '%d.%m.%y').date()

def import_csv_data():
    df = pd.read_csv("datafiles/PTH-CSV-Liste-2025-09-13.csv", sep=';', encoding='cp1252')
    session = SessionLocal()

    # Add therapists
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
        )
        session.add(therapist)
        session.flush()  # Flush to get therapist.id

        # Add therapy methods
        methods = row['PTH-Methoden'].split(',')
        for method in methods:
            # Check if method already exists
            therapy_method = session.query(TherapyMethod).filter_by(method_name=method.strip()).first()
            if not therapy_method:
                therapy_method = TherapyMethod(method_name=method.strip())
                session.add(therapy_method)
                session.flush()  # Flush to get therapy_method.id

            # Check if the relationship already exists
            if therapy_method not in therapist.therapy_methods:
                therapist.therapy_methods.append(therapy_method)

    session.commit()
    session.close()
    print(f"Imported {len(df)} therapist records")

if __name__ == "__main__":
    import_csv_data()
