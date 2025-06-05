from collections import Counter

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
