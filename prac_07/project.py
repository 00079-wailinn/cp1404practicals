import datetime


class Project:
    def __init__(self, name, start_date, priority, completion_percentage, cost):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.completion_percentage = int(completion_percentage)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion_percentage}%"

    def is_complete(self):
        return self.completion_percentage == 100

    def update(self, completion_percentage=None, priority=None):
        if completion_percentage is not None:
            self.completion_percentage = int(completion_percentage)
        if priority is not None:
            self.priority = int(priority)

    def __lt__(self, other):
        return self.priority < other.priority