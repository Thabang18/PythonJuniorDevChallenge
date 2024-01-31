'''
Author: T Kgatla 
Date: 31 January 2024 
Class description: This class is used for the sole purpose of testing if the event_scheduler class behaves as expected 

'''

import unittest
from datetime import datetime
from event_scheduler import EventScheduler


class TestEventScheduler(unittest.TestCase):
    def setUp(self):
        self.event_scheduler = EventScheduler()


    ''' Algorithm explanation, implements the linked list logic'''
    # Add a test event to the event_scheduler
    # Check if the head of the event_scheduler is not None
    # Check if the title of the head event matches the test event title
    # Let the user know about the test results 
        
    def test_add_event(self):
        self.event_scheduler.add_event(
            "Test Event", "Test Description", "2024-01-31", "12:00")
        self.assertIsNotNone(self.event_scheduler.head)
        self.assertEqual(self.event_scheduler.head.title, "Test Event")

        # Additional information for the user
        print("Test for adding an event passed successfully.")
        print("Event added to the scheduler.")

    def test_list_events(self):
        self.event_scheduler.add_event(
            "Test Event 1", "Description 1", "2024-01-31", "12:00")
        self.event_scheduler.add_event(
            "Test Event 2", "Description 2", "2024-02-01", "14:00")

        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        self.event_scheduler.list_events()

        output = sys.stdout.getvalue()

        # Reset redirect.
        sys.stdout = original_stdout

        self.assertIn("Test Event 1", output)
        self.assertIn("Test Event 2", output)

        # Additional information for the user
        print("Test for listing events passed successfully.")
        print("Events listed correctly.")


if __name__ == "__main__":
    unittest.main()
