"""This module maps therapy types to therapy methods."""
from .models import SessionLocal, TherapyMethod, TherapyMethodCluster, TherapyType

#---------------------
# MAPPINGS
#---------------------

THERAPY_CLUSTERS = {
    "PA": "Psychoanalytisch",
    "HT": "Humanistisch",
    "ST": "Systemisch",
    "VT": "Verhaltenstherapeutisch"
}

THERAPY_TYPES = {
    "HT": "Heart Talkers",
    "SF": "Squad Fixers",
    "DD": "Deep Divers",
    "HH": "Habit Hackers"
}

THERAPY_METHODS_TO_CLUSTERS = {
    "Analytische Psychologie": "PA",
    "Daseinsanalyse": "PA",
    "Dynamische Gruppenpsychotherapie": "PA",
    "Existenzanalyse": "HT",
    "Existenzanalyse und Logotherapie": "HT",
    "Gestalttheoretische Psychotherapie": "HT",
    "Personenzentrierte Psychotherapie": "HT",
    "Gruppenpsychoanalyse/Psychoanalytische Psychotherapie": "PA",
    "Hypnosepsychotherapie": "PA",
    "Individualpsychologie": "PA",
    "Integrative Gestalttherapie": "HT",
    "Integrative Therapie": "HT",
    "Katathym Imaginative Psychotherapie": "PA",
    "Konzentrierte Bewegungstherapie": "PA",
    "Neuro-Linguistische Psychotherapie": "ST",
    "Psychoanalyse/Psychoanalytische Psychotherapie": "PA",
    "Psychoanalytisch orientierte Psychotherapie": "PA",
    "Psychodrama": "HT",
    "Systemische Familientherapie": "ST",
    "Transaktionsanalytische Psychotherapie": "PA",
    "Verhaltenstherapie": "VT",
    "Autogene Psychotherapie": "PA"
}

THERAPY_TYPE_TO_CLUSTERS = {
    "HT": "HT", # Heart Talkers -> Humanistisch
    "SF": "ST", # Squad Fixers -> Systemisch
    "DD": "PA", # Deep Divers -> Psychoanalytisch
    "HH": "VT" # Habit Hackers -> Verhaltenstherapeutisch
}

#---------------------
# MAPPING FUNCTIONS
#---------------------

def map_methods_to_clusters():
    """Function to map therapy methods to their respective clusters."""
    session = SessionLocal()

    # Map therapy methods to clusters
    for method_name, cluster_short in THERAPY_METHODS_TO_CLUSTERS.items():
        # Find the cluster by its short code
        cluster = session.query(TherapyMethodCluster).filter_by(cluster_short=cluster_short).first()
        if not cluster:
            print(f"Cluster {cluster_short} not found for method {method_name}")
            continue

        # Find the therapy method by its name
        method = session.query(TherapyMethod).filter_by(method_name=method_name).first()
        if not method:
            print(f"Therapy method {method_name} not found")
            continue

        # Assign the cluster to the therapy method
        method.cluster_id = cluster.id
        method.name = cluster.cluster_name
        session.add(method)

    # Commit changes
    session.commit()
    print("Mapped therapy methods to clusters successfully.")
    session.close()

def map_types_to_clusters():
    """Function to map therapy types to their respective clusters."""
    session = SessionLocal()

    # Iterate over therapy types and their corresponding clusters
    for type_short, cluster_short in THERAPY_TYPE_TO_CLUSTERS.items():
        # Find the cluster by its short code
        cluster = session.query(TherapyMethodCluster).filter_by(cluster_short=cluster_short).first()
        if not cluster:
            print(f"Cluster {cluster_short} not found for therapy type {type_short}")
            continue

        # Find the therapy type by its short code
        therapy_type = session.query(TherapyType).filter_by(type_short=type_short).first()
        if not therapy_type:
            print(f"Therapy type {type_short} not found")
            continue

        # Assign the cluster ID to the therapy type
        therapy_type.cluster_id = cluster.id
        session.add(therapy_type)

        print(f"Mapped therapy type {type_short} to cluster {cluster.cluster_name} (ID: {cluster.id})")

    # Commit changes
    session.commit()
    print("Mapped therapy types to clusters successfully.")
    session.close()

if __name__ == "__main__":
    map_methods_to_clusters()
    map_types_to_clusters()
