# Task 2: 
# Event Management System Enhancement

# - Problem Statement: 
# Extend an existing Event class by adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.


class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0


        def add_participant(self,count):
              if count > 0:
                    self.participant_count += count

        def get_participant_method(self):
              return self.participant_count

        

def main():
      event1 = Event("Donald", "Monday")
      event1.add_participant(1)
      event1.add_participant(20)
      print(event1.get_participant_method())


main()
