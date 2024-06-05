from organizer import Organizer
from datetime import datetime

if __name__ == '__main__':
    organizer = Organizer()

    organizer.AddEvent("Event 1", datetime(2024, 6, 7, 10, 0), "Meeting")
    organizer.AddEvent("Event 2", datetime(2024, 6, 8, 15, 30), "Appointment")
    organizer.AddEvent("Event 3", datetime(2024, 6, 10, 9, 0), "Meeting", is_recurring=True, recurrence_interval="weekly")
    organizer.AddEvent("Event 4", datetime(2024, 6, 11, 13, 0), "Deadline")
    organizer.AddEvent("Event 5", datetime(2024, 6, 15, 12, 0), "Appointment")

    organizer.PrintAllEvents()

    organizer.PrintEventsByDate(datetime(2024, 6, 10))
    organizer.PrintEventsInRange(datetime(2024, 6, 7), datetime(2024, 6, 11))

    organizer.PrintEventsByCategory("Meeting")

    organizer.GetNextEventReminders(3)
