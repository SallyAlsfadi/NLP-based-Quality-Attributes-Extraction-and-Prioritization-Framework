from extractor import extract_quality_attributes
from prioritizer import prioritize_by_frequency

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