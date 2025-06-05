from collections import Counter
from collections import defaultdict

def prioritize_by_frequency(extracted_results):
    """
    Input:
        extracted_results = list of lists, where each inner list is quality attributes for one story
    Output:
        sorted list of (attribute, frequency)
    """
    flat_list = [attr for sublist in extracted_results for attr in sublist]
    counter = Counter(flat_list)
    sorted_priority = counter.most_common()
    return sorted_priority

def prioritize_by_role_weighted_frequency(story_tuples):
    """
    Input: list of (role, [attributes]) tuples
    Output: dict of {attribute: weighted score}
    """
    # Count how often each role appears
    role_counts = defaultdict(int)
    attr_role_matrix = defaultdict(lambda: defaultdict(int))

    for role, attrs in story_tuples:
        role_counts[role] += 1
        for attr in attrs:
            attr_role_matrix[attr][role] += 1

    # Compute weighted scores
    weighted_scores = {}
    for attr, role_map in attr_role_matrix.items():
        score = sum(role_counts[role] * count for role, count in role_map.items())
        weighted_scores[attr] = score

    # Sort by score
    return sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
