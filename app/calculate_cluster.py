"""This module processes questionnaire responses to recommend therapy clusters"""
# pylint: disable=consider-using-enumerate

def process_all_responses(responses):
    """
    Processes all responses and calculates scores for each cluster.

    Args:
        responses (list): List of response objects from the frontend.

    Returns:
        dict: Scores for each cluster.
    """
    # Initialize scores for clusters
    scores = {}

    # Iterate through all responses
    for response in responses:
        for cluster in response["cluster_points"]:
            scores[cluster] = scores.get(cluster, 0) + 1

    return scores

def calculate_cluster(scores):
    """
    Determines the cluster with the highest score.

    Args:
        scores (dict): Scores for each cluster.

    Returns:
        str: The cluster with the highest score.
    """
    # Add score tuples to a list for sorting
    sorted_scores = []
    for cluster, score in scores.items():
        sorted_scores.append((cluster, score))

    # Perform bubble sort to sort scores in descending order
    for i in range(len(sorted_scores)):
        for j in range(i + 1, len(sorted_scores)):
            if sorted_scores[i][1] < sorted_scores[j][1]:
                sorted_scores[i], sorted_scores[j] = sorted_scores[j], sorted_scores[i]

    # Get the key of the highest score
    best_cluster = sorted_scores[0][0]
    return best_cluster
