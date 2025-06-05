from extractor import extract_quality_attributes
from prioritizer import prioritize_by_frequency, prioritize_by_role_weighted_frequency
import re

def extract_role(story_text):
    match = re.match(r"As a (\w+)", story_text.strip(), re.IGNORECASE)
    return match.group(1).lower() if match else "unknown"
def read_user_stories(path):
    with open(path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

if __name__ == "__main__":
    stories = read_user_stories("data/user_stories.txt")
    for i, story in enumerate(stories, 1):
        attributes = extract_quality_attributes(story)
        print(f"Story {i}:")
        print(f"  ➤ {story}")
        print(f"  ✅ Extracted Attributes: {attributes}\n")

print("\n🔷 PRIORITIZED QUALITY ATTRIBUTES (By Frequency):")
priorities = prioritize_by_frequency([extract_quality_attributes(s) for s in stories])
for attr, freq in priorities:
    print(f"{attr:<15} ➤ {freq} times")

print("\n🔷 PRIORITIZED QUALITY ATTRIBUTES (By Frequency × Role Weight):")
story_tuples = []
for story in stories:
    role = extract_role(story)
    attrs = extract_quality_attributes(story)
    story_tuples.append((role, attrs))

priorities = prioritize_by_role_weighted_frequency(story_tuples)
for attr, score in priorities:
    print(f"{attr:<15} ➤ Score: {score}")

print("\n🔷 PRIORITIZED QUALITY ATTRIBUTES (By Frequency × Criticality Factor Value):")
# Define CFV scores (manually set by QA Manager or domain expert)
cfv_scores = {
    "security": 10,
    "usability": 6,
    "maintainability": 5,
    "performance": 8,
    "portability": 4
}

# Get frequency count
attribute_counts = {}
for story in stories:
    for attr in extract_quality_attributes(story):
        attribute_counts[attr] = attribute_counts.get(attr, 0) + 1

# Get CFV-weighted priority
from prioritizer import prioritize_by_cfv
cfv_priorities = prioritize_by_cfv(attribute_counts, cfv_scores)

# Print
for attr, score in cfv_priorities:
    print(f"{attr:<15} ➤ Score: {score} (CFV × Frequency)")

