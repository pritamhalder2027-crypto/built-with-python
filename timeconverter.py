from zoneinfo import ZoneInfo
from datetime import datetime

#Step-1: Data - city names and their time zone names
cities = {
    "mumbai": "Asia/Mumbai",
    "singapore": "Asia/Singapore",
    "london": "Europe/London",
    "new york": "America/New_York",
    "tokyo": "Asia/Tokyo",
    "toronto": "America/Toronto",
    "hongkong": "Asia/HongKong",
    "dubai": "Asia/Dubai",
}

#Step-2: Decide morning / afternoon / evening / night
def part_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

#Step-3: Get the current time in any city
def get_time(city):
    zone = ZoneInfo(cities[city])
    return datetime.now(zone)

#Step-4: Ask the user and show the result
home = input("Your city: ").lower()
target = input("City to check: ").lower()

if home not in cities or target not in cities:
    print("Sorry,, that city is not in my list yet")
else:
    home_time = get_time(home)
    target_time = get_time(target)

    print(f"Time in {home.title()}: {home_time.strftime('%H:%M')} ({part_of_day(home_time.hour)})")
    print(f"Time in {target.title()}: {target_time.strftime('%H:%M')} ({part_of_day(target_time.hour)})")

