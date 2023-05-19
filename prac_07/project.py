import datetime


class Project:
    def __init__(self, name, date_string, priority, cost, completion):
        self.name = name
        self.date_string = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, start: {self.date_string}, priority {self.priority}, estimate: {self.cost}, completion: {self.completion}%"

    def is_not_complete(self):
        if self.completion < 100:
            return True

    def is_complete(self):
        if self.completion == 100:
            return True

    def change_completion(self, new_completion):
        self.completion = new_completion
        return self.completion
