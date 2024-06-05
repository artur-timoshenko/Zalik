class Event:
    def __init__(self, id, title, date, category, is_recurring=False, recurrence_interval=None):
        self.id = id
        self.title = title
        self.date = date
        self.category = category
        self.is_recurring = is_recurring
        self.recurrence_interval = recurrence_interval

    def Print(self):
        print(
            "  Event id: " + str(self.id) + ", title: " + self.title +
            ", date: " + self.date.strftime("%Y-%m-%d %H:%M") +
            ", category: " + self.category +
            (", is_recurring: " + str(self.is_recurring) if self.is_recurring else "") +
            (", recurrence_interval: " + self.recurrence_interval if self.recurrence_interval else "")
        )
