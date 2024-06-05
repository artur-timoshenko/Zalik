from datetime import datetime

class Event:
    def __init__(self, event_id, title, date, category, is_recurring=False, recurrence_interval=None):
        self.event_id = event_id
        self.title = title
        self.date = date
        self.category = category
        self.is_recurring = is_recurring
        self.recurrence_interval = recurrence_interval

    def PrintEvent(self):
        print("Event ID: " + str(self.event_id))
        print("Title: " + self.title)
        print("Date: " + self.date.strftime("%Y-%m-%d %H:%M"))
        print("Category: " + self.category)
        print("Recurring: " + str(self.is_recurring))
        if self.is_recurring:
            print("Recurrence Interval: " + str(self.recurrence_interval))



class Organizer:
    def __init__(self):
        self.mEvents = dict()

    def AddEvent(self, title, date, category, is_recurring=False, recurrence_interval=None):
        if len(self.mEvents) == 0:
            event_id = 0
        else:
            event_id = max(self.mEvents.keys()) + 1

        new_event = Event(event_id, title, date, category, is_recurring, recurrence_interval)
        self.mEvents[event_id] = new_event
        print("Event '" + title + "' successfully added")

    def PrintAllEvents(self):
        print("All Events: ")
        for event_id in self.mEvents:
            self.mEvents[event_id].PrintEvent()

    def PrintEventsByDate(self, date):
        print("Events on " + date.strftime("%Y-%m-%d") + ":")
        for event_id in self.mEvents:
            if self.mEvents[event_id].date.date() == date.date():
                self.mEvents[event_id].PrintEvent()

    def PrintEventsInRange(self, start_date, end_date):
        print("Events between " + start_date.strftime("%Y-%m-%d") + " and " + end_date.strftime("%Y-%m-%d") + ":")
        for event_id in self.mEvents:
            if start_date <= self.mEvents[event_id].date <= end_date:
                self.mEvents[event_id].PrintEvent()

    def PrintEventsByCategory(self, category):
        print("Events in category '" + category + "':")
        for event_id in self.mEvents:
            if self.mEvents[event_id].category == category:
                self.mEvents[event_id].PrintEvent()

    def GetNextEventReminders(self, n=5):
        print("Next " + str(n) + " Event Reminders:")
        sorted_events = sorted(self.mEvents.values(), key=lambda event: event.date)
        current_time = datetime.now()
        count = 0
        for event in sorted_events:
            if event.date >= current_time:
                event.PrintEvent()
                count += 1
            if count == n:
                break
