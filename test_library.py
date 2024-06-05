import unittest
from organizer import Organizer
from datetime import datetime

class TestOrganizer(unittest.TestCase):

    def setUp(self):
        self.organizer = Organizer()

    def test_add_event(self):
        self.organizer.AddEvent("Test Event", datetime.strptime("2024-06-07 10:00", "%Y-%m-%d %H:%M"), "Meeting")
        self.assertEqual(len(self.organizer.mEvents), 1)
        self.assertEqual(self.organizer.mEvents[0].title, "Test Event")

    def test_print_all_events(self):
        self.organizer.AddEvent("Event 1", datetime.strptime("2024-06-07 10:00", "%Y-%m-%d %H:%M"), "Meeting")
        self.organizer.AddEvent("Event 2", datetime.strptime("2024-06-08 15:30", "%Y-%m-%d %H:%M"), "Appointment")
        self.organizer.PrintAllEvents()

    def test_print_events_by_date(self):
        self.organizer.AddEvent("Event 1", datetime.strptime("2024-06-07 10:00", "%Y-%m-%d %H:%M"), "Meeting")
        self.organizer.AddEvent("Event 2", datetime.strptime("2024-06-08 15:30", "%Y-%m-%d %H:%M"), "Appointment")
        self.organizer.PrintEventsByDate(datetime.strptime("2024-06-08", "%Y-%m-%d"))

    def test_print_events_in_range(self):
        self.organizer.AddEvent("Event 1", datetime.strptime("2024-06-07 10:00", "%Y-%m-%d %H:%M"), "Meeting")
        self.organizer.AddEvent("Event 2", datetime.strptime("2024-06-08 15:30", "%Y-%m-%d %H:%M"), "Appointment")
        self.organizer.AddEvent("Event 3", datetime.strptime("2024-06-10 09:00", "%Y-%m-%d %H:%M"), "Meeting")
        self.organizer.PrintEventsInRange(datetime.strptime("2024-06-07", "%Y-%m-%d"), datetime.strptime("2024-06-10", "%Y-%m-%d"))

    def test_print_events_by_category(self):
        self.organizer.AddEvent("Event 1", datetime.strptime("2024-06-07 10:00", "%Y-%m-%d %H:%M"), "Meeting")
        self.organizer.AddEvent("Event 2", datetime.strptime("2024-06-08 15:30", "%Y-%m-%d %H:%M"), "Appointment")
        self.organizer.AddEvent("Event 3", datetime.strptime("2024-06-10 09:00", "%Y-%m-%d %H:%M"), "Meeting")
        self.organizer.PrintEventsByCategory("Meeting")

if __name__ == '__main__':
    unittest.main()
