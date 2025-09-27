"""This module processes questionnaire responses to recommend therapy clusters"""
import json

# Load mapping from JSON file
def load_mapping():
    with open("datafiles/mapping.json", "r", encoding="utf-8") as file:
        return json.load(file)

# Process a single response
def process_response(value_instance, scores, mapping):
    for entry in mapping["mapping"]:
        if entry["valueInstance"] == value_instance:
            scores[entry["school1"]] += 1
            if entry["school2"]:
                scores[entry["school2"]] += 1

# Process all responses
def process_all_responses(responses, mapping):
    # Initialize scores
    scores = {school: 0 for school in ["PA", "VT", "SYS", "PZ", "G", "not G"]}

    # Iterate through all responses
    for value_instance in responses:
        for entry in mapping["mapping"]:
            if entry["valueInstance"] == value_instance:
                scores[entry["school1"]] += 1
                if entry["school2"]:
                    scores[entry["school2"]] += 1

    return scores

# Calculate final recommendations
def calculate_recommendations(scores):
    # Convert scores to a list of tuples
    score_list = []
    for school, score in scores.items():
        score_list.append((school, score))

    # Sort scores manually (highest first)
    for i, _ in enumerate(score_list):
        for j in range(i + 1, len(score_list)):
            if score_list[i][1] < score_list[j][1]:
                score_list[i], score_list[j] = score_list[j], score_list[i]

    # Return top 2 school names
    recommendations = []
    for i, (school, _) in enumerate(score_list):
        if i >= 2:
            break
        recommendations.append(school)

    return recommendations
