import json
from datetime import datetime, timedelta

from planner import time_text

FILE = "reminders.json"

def load_reminders():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_reminders(reminders):
       with open(FILE, "w") as f:
           json.dump(reminders, f, indent=2)

def add_reminder(reminders):
    name = input("What is it? (e.g. Vitamin D, submit report): ").strip()
    time_text = input("Time (HH:MM, 24-hour): ").strip()
    timing = input("Timing (once/daily): ").strip().lower()

    try:
        datetime.strptime(time_text, "%H:%M")
    except ValueError:
        print("Please enter a time like 16:30")
        return


    reminders.append({
        "name": name,
        "time": time_text,
        "timing": timing,
        "done_today": False,
    })
    save_reminders(reminders)
    print("Reminder added!")

def check_reminder(reminders):
    now = datetime.now()
    print(f"\nCurrent time: {now.strftime('%H:%M')}\n")

    due_now = []
    upcoming = []

    for r in reminders:
        reminder_time = datetime.strptime(r["time"], "%H:%M").time()
        reminder_dt = datetime.combine(now.date(), reminder_time)

        diff = (reminder_dt - now).total_seconds() / 60

        if r["done_today"]:
            continue
        elif -15 <= diff <= 0:
            due_now.append(r)
        elif 0 < diff <= 60:
            upcoming.append((r, int(diff)))

    if due_now:
        print("Due now:")
        for r in due_now:
            print(f" - {r['name']} ({r['time']})")
    if upcoming:
        print("\nComing up:")
        for r, mins in upcoming:
            print(f" - {r['name']} at {r['time']} (in {mins} min)")
    if not due_now and not upcoming:
        print("Nothing due right now.")

def mark_done(reminders):
    for i, r in enumerate(reminders, start=1):
        print(f"{i}. {r['name']} ({r['time']})")
    try:
        choice = int(input("Mark which one as done? (number): "))
        reminders[choice - 1]["done_today"] = True
        save_reminders(reminders)
        print("Marked as done for today!")
    except (ValueError, IndexError):
        print("Invalid choice.")

reminders = load_reminders()

while True:
    print("\n1. Add reminder\n2. Check what's due\n3. Mark as done\n4. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        add_reminder(reminders)
    elif choice == "2":
        check_reminder(reminders)
    elif choice == "3":
        mark_done(reminders)
    elif choice == "4":
        print("Closing program...")
        break
    else:
        print("Please choose from 1 to 4.")




