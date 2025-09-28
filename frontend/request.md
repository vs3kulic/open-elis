# Backend Request Documentation

## Questionnaire Result Calculation

### Request Structure

**Endpoint:** `POST /calculate_result`

**Headers:**
```
Content-Type: application/json
X-API-Key: elis_your_api_key_here
```

**Request Payload:**
```json
{
  "responses": [
    {
      "question_id": 1,
      "options": ["Strukturiert-Hierarchisch", "Offen-Ebenbürtig"],
      "selected_option": "Strukturiert-Hierarchisch",
      "cluster_points": ["PA", "VT"]
    },
    {
      "question_id": 2,
      "options": ["Strukturiert-Hierarchisch", "Offen-Ebenbürtig"],
      "selected_option": "Offen-Ebenbürtig",
      "cluster_points": ["PZ", "SYS"]
    },
    {
      "question_id": 3,
      "options": ["Abstrakt-Sano", "Praktisch-Corpore"],
      "selected_option": "Abstrakt-Sano",
      "cluster_points": ["SYS", "VT"]
    }
  ]
}
```

**Payload Fields:**
- `question_id`: Integer identifying the question (1-26)
- `options`: Array of the two available options for the question
- `selected_option`: String of the user's selected option
- `cluster_points`: Array of therapy clusters that receive points for this selection

### Response Structure

**Success Response (200 OK):**
```json
{
  "recommended_cluster": "VT"
}
```

**Response Fields:**
- `recommended_cluster`: String containing the cluster_short code (e.g., "PA", "VT", "SYS", "PZ", "G") of the therapy cluster with the highest score

### Calculation Logic

The backend processes all 26 responses and calculates scores for each therapy cluster:

1. **Score Accumulation**: For each response, points are added to the clusters specified in `cluster_points`
2. **Bubble Sort**: All cluster-score pairs are sorted by score in descending order using a bubble sort algorithm
3. **Best Cluster Selection**: The cluster with the highest accumulated score is returned as the recommendation

**Example:**
- If responses result in scores: PA=2, VT=3, SYS=1
- The algorithm returns "VT" as it has the highest score (3)

### Frontend Usage

After receiving the recommended cluster, the frontend can:
- Search for therapists offering methods within that cluster using `/therapists?cluster_short={recommended_cluster}`
- Display cluster-specific information and therapy method recommendations to the user