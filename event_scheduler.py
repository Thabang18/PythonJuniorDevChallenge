'''
Author: T Kgatla 
Date: 31 January 2024 
Class description: This is a linkedlist class, it contains the data structure that will be used to store the events since the
use of an external database is not permitted.

'''

from datetime import datetime


class Event:
    '''
     This is an event class with its appropriate attributes, think of this as a model if you will be implementing the MTV structure 

    '''

    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.next = None  # This is a pointer to the next node. I am making use of a singly linked list to store the information


class EventScheduler:
    def __init__(self):
        self.head = None  # Now, this is where the linked list is implemented, this value is initially set to null

    ''' Singly linked list algorithm '''
    # creates a new event node using the provided title, description, date, and time
    # If the linked list is empty, the new event becomes the head of the linked list
    # Otherwise, it traverses the linked list to find the last node and then appends the new event node
    # to the end by setting the next attribute of the last node to the new event.

    def add_event(self, title, description, date, time):
        new_event = Event(title, description, date, time)
        if not self.head:
            self.head = new_event
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_event

    def search_events(self, keyword_or_date):
        if not self.head:
            print("Error: no events.")
            return

        found = False
        try:

            ''' Algorithm explanation, implements the basic functionality  of a linked list '''
            # Start iterating through the linked list from the head
            # Convert the date of the current event to a date object for comparison
            # Check if the event date matches the search date
            # Print the details of the matching event
            # Indicate that a matching event was found
            # Move to the next event in the linked list

            search_date = datetime.strptime(keyword_or_date, "%Y-%m-%d").date()
            current = self.head
            while current:
                event_date = datetime.strptime(current.date, "%Y-%m-%d").date()
                if event_date == search_date:
                    print(f"Title: {current.title}\nDescription: {
                          current.description}\nDate: {current.date}\nTime: {current.time}\n")
                    found = True
                current = current.next

            ''' Algorithm explanation, implements linked list functionality '''
            # This is the catch part of the code
            # Attempt to parse the input as a date, if unsuccessful, treat it as a keyword search
            # Check if the keyword appears in the title or description of the current event (case-insensitive)
            # Print the details of the matching event
            # Indicate that a matching event was found or else, indicate otherwise
            # Move to the next event in the linked list
        except ValueError:
            current = self.head
            while current:
                if keyword_or_date.lower() in current.title.lower() or keyword_or_date.lower() in current.description.lower():
                    print(f"Title: {current.title}\nDescription: {
                          current.description}\nDate: {current.date}\nTime: {current.time}\n")
                    found = True
                current = current.next

        if not found:
            print(f"No events found with keyword or date '{keyword_or_date}'.")

    def edit_event(self, title, new_title, new_description, new_date, new_time):
        if not self.head:
            print("No events to edit.")
            return

        current = self.head
        while current and current.title != title:
            current = current.next

        if current:
            current.title = new_title
            current.description = new_description
            current.date = new_date
            current.time = new_time
            print("Event edited successfully.")
        else:
            print(f"Event '{title}' not found.")

    def list_events(self):
        if not self.head:
            print("No events scheduled.")
        else:
            current = self.head
            while current:
                print(f"Title: {current.title}\nDescription: {
                      current.description}\nDate: {current.date}\nTime: {current.time}\n")
                current = current.next

    def delete_event(self, title):
        if not self.head:
            print("No events to delete.")
            return

        if self.head.title == title:
            self.head = self.head.next
            print(f"Event '{title}' deleted successfully.")
            return

        current = self.head
        while current.next and current.next.title != title:
            current = current.next

        if current.next:
            current.next = current.next.next
            print(f"Event '{title}' deleted successfully.")
        else:
            print(f"Event '{title}' not found.")

    # Keep the user in a loop, until the user chooses to exit.
if __name__ == "__main__":
    event_scheduler = EventScheduler()

    while True:
        # user options
        print("\nOptions:")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Search Events")
        print("5. Edit Event")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")
        # user choice
        if choice == "1":
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            event_scheduler.add_event(title, description, date, time)
            print("Event added successfully.")
        elif choice == "2":
            print("\nList of all events:")
            event_scheduler.list_events()
        elif choice == "3":
            title_to_delete = input("Enter the title of the event to delete: ")
            event_scheduler.delete_event(title_to_delete)
        elif choice == "4":
            keyword_or_date = input(
                "Enter keyword or date (YYYY-MM-DD) to search events: ")
            event_scheduler.search_events(keyword_or_date)
        elif choice == "5":
            title_to_edit = input("Enter the title of the event to edit: ")
            new_title = input("Enter new event title: ")
            new_description = input("Enter new event description: ")
            new_date = input("Enter new event date (YYYY-MM-DD): ")
            new_time = input("Enter new event time (HH:MM): ")
            event_scheduler.edit_event(
                title_to_edit, new_title, new_description, new_date, new_time)
        elif choice == "6":
            print("Exiting the event scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
