# 1- import random module
import random

# 2- create subjects
subjects = [
    "Virat Kohli",
    "Gojo Satoru",
    "A Mumbai Cat",
    "A Couple",
    "A flock of birds",
    "A taxi driver from Bangalore"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "orders",
    "celebrates"

]

places_or_things = [
    "at Gateway of India",
    "in metro",
    "in a street",
    "at stadium",
    "in a movie theatre",
    "at a holy shrine"
]

# start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

#print ending message
print("\nThanks for using the Fake News Headline Generator.Have a great day!")