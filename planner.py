from datetime import datetime
from zoneinfo import ZoneInfo

# STEP 1: Data - city names and their time zone names
cities = {
    "mumbai": "Asia/Kolkata",
    "singapore": "Asia/Singapore",
    "london": "Europe/London",
    "new york": "America/New_York",
    "tokyo": "Asia/Tokyo",
    "dubai": "Asia/Dubai",
}

# STEP 2: Morning / afternoon / evening / night (same as before)
def part_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

# STEP 3: Is this a sensible time for a meeting? (9 AM to 9 PM)
def is_good_time(hour):
    return 9 <= hour < 21

# STEP 4: Build the meeting time in the organiser's city
def make_meeting_time(city, time_text):
    zone = ZoneInfo(cities[city])
    today = datetime.now(zone).date()
    meeting_time = datetime.strptime(time_text, "%H:%M").time()
    return datetime.combine(today, meeting_time, tzinfo=zone)

# STEP 5: Ask the user
home = input("Your city: ").strip().lower()
time_text = input("Meeting time in your city (HH:MM, 24-hour): ").strip()
others = input("Participants' cities (separate with commas): ").lower().split(",")

# STEP 6: Check input, then show the meeting time for everyone
if home not in cities:
    print("Sorry, your city is not in my list yet.")
else:
    try:
        meeting = make_meeting_time(home, time_text)
    except ValueError:
        print("Please enter the time like 18:30")
    else:
        print(f"\nMeeting: {time_text} in {home.title()}\n")

        for city in others:
            city = city.strip()
            if city not in cities:
                print(f"{city.title()}: not in my list yet")
                continue

            local = meeting.astimezone(ZoneInfo(cities[city]))

            # Did the date change compared with the organiser's city?
            if local.date() > meeting.date():
                day_note = " (next day)"
            elif local.date() < meeting.date():
                day_note = " (previous day)"
            else:
                day_note = ""

            verdict = "Good time" if is_good_time(local.hour) else "Inconvenient"
            print(f"{city.title():<10} {local.strftime('%H:%M')}{day_note} "
                  f"({part_of_day(local.hour)}) - {verdict}")
