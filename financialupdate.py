import random

#Information
data = {
    "index": {
        "subjects": ["The Sensex", "Nifty50", "Bank Nifty"],
        "actions": ["rose by 1.0%", "fell sharply", "Hit a record high", "remained flat"],
        "places": ["in early morning", "amid global tensions", "after quarterly results"],
    },
    "currency": {
        "subjects": ["The rupee", "US Dollar"],
        "actions": ["weakened", "risen above", "held steady"],
        "places": ["against major currencies", "amid rising oil prices", "on FIIs outflows"],
    },
    "institution": {
        "subjects" : ["SEBI", "The RBI", "JP Morgan Chase", "Morgan Stanley", "BlackRock", "Blackstone"],
        "actions": ["announced a rate cut", "issues new guidelines", "kept rates unchanged"],
        "places": ["amid inflation concerns", "following the policy review", "to support growth"],
    },
    "commodity": {
        "subjects": ["Gold Prices", "Crude Oil"],
        "actions": ["gained momentum", "slipped", "surged"],
        "places": ["on global demand", "amid supply worries", "in international markets"],
    },
}

#Logic Section
def generate_points(num_points=4):
    categories = random.sample(list(data.keys()), min(num_points, len(data)))
    points = []
    for cat in categories:
        group = data[cat]
        points.append(
            f"{random.choice(group['subjects'])} "
            f"{random.choice(group['actions'])} "
            f"{random.choice(group['places'])}. "
        )
    return points

def print_update(num_points=4):
    print("\nFinancial Update")
    for i, point in enumerate(generate_points(num_points), start=1):
        print(f"{i}. {point}")

print_update(4)