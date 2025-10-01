"""This module populates the database with therapy clusters based on existing therapy methods."""
from .models import SessionLocal, TherapyMethodCluster, TherapyType
from .run_mappings import THERAPY_CLUSTERS, THERAPY_TYPES

def populate_tables():
    """Populate the database with predefined therapy clusters and types."""
    session = SessionLocal()

    # Populate types
    for type_short, type_name in THERAPY_TYPES.items():
        therapy_type = TherapyType(
            type_short=type_short,
            type_name=type_name,
            description=f"{type_name} type description"
        )
        session.add(therapy_type)

    # Populate clusters
    for cluster_short, cluster_name in THERAPY_CLUSTERS.items():
        cluster = TherapyMethodCluster(
            cluster_short=cluster_short,
            cluster_name=cluster_name,
            description=f"{cluster_name} cluster description"
        )
        session.add(cluster)

    # Commit all changes at once
    session.commit()
    print(f"Inserted {len(THERAPY_CLUSTERS)} therapy clusters and {len(THERAPY_TYPES)} therapy types into the database.")

if __name__ == "__main__":
    populate_tables()
