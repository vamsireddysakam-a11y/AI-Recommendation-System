# AI Recommendation System

# Dataset
items = {
    "Action": ["Avengers", "John Wick", "Mission Impossible"],
    "Comedy": ["Friends", "The Mask", "Brooklyn Nine-Nine"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Pursuit of Happyness"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"]
}

print("===== AI Recommendation System =====")
print("Available Categories:")
for category in items:
    print("-", category)

# User input
user_input = input("\nEnter your favorite categories (comma separated): ")

# Convert input into a list
preferences = [x.strip().title() for x in user_input.split(",")]

# Recommendation Logic
recommendations = []

for preference in preferences:
    if preference in items:
        recommendations.extend(items[preference])

# Display results
if recommendations:
    print("\nRecommended Movies:")
    for movie in recommendations:
        print("✔", movie)
else:
    print("\nSorry! No recommendations found.")