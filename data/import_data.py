"""This module contains utilities for importing external data sources."""
import pandas as pd
from datetime import datetime
from .models import SessionLocal, Therapist, TherapistAddress, TherapistContact, TherapyMethod

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
            registration_date=parse_date(row['Eintragungdatum']),
            registration_number=int(row['Eintragungs Nummer']),
        )
        session.add(therapist)
        session.flush()  # Flush to get therapist.id
        
        # Add therapist contact
        contact = TherapistContact(
            email=row['Email1'],
            website=row.get('Website', None),  # Handle missing website gracefully
            therapist=therapist  # Associate contact with therapist
        )
        session.add(contact)
        
        # Add therapist address
        address = TherapistAddress(
            state=row['Berufssitz Bundesland 1'],
            postal_code=row['Berufssitz PLZ 1'],
            therapist=therapist
        )
        session.add(address)

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

        print(f"Inserting therapist: {row['Familien-/Nachname']}, {row['Vorname']}")
        print(f"Inserting contact: {row['Email1']}")
        print(f"Inserting address: {row['Berufssitz Bundesland 1']}, {row['Berufssitz PLZ 1']}")
        print(f"Inserting therapy methods: {methods}")

    session.commit()
    session.close()
    print(f"Imported {len(df)} therapist records")

if __name__ == "__main__":
    import_csv_data()
