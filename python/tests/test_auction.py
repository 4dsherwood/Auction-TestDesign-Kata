import pytest
from approvaltests import verify

from auction.auction import AuctionEventListener, AuctionMessageTranslator

#from .auction import *   # E   ModuleNotFoundError: No module named 'tests.auction'
#from auction import *
#from AuctionEventListener import *


def test_notifies_auction_closed_when_close_message_received():
    message = "SOLVersion: 1.1; Event: CLOSE;"
    # TODO: write a test for this message translation

def test_notifies_auction_closed_when_close_message_received_using_mock():
    # Arrange: Set up the translator and mock listener
    class MockListener(AuctionEventListener):
        def __init__(self):
            self.notifications = []

        def notify(self,message):
            self.notifications.append(message)

    # Create an instance of the mock listener
    mock_listener = MockListener()

    # Create an instance of the message translator using the mock listener
    translator = AuctionMessageTranslator(mock_listener)

    # Act: Send the test message through the translator
    message = "SOLVersion: 1.1; Event: CLOSE;"
    translator.process_message(message)

    # Assert: Verify the output using ApprovalTests
    verify(mock_listener.notifications)


def test_notifies_bid_details_when_price_message_received():
    # Arrange: Set up the translator and mock listener
    class MockListener(AuctionEventListener):
        def __init__(self):
            self.notifications = []

        def notify(self,message):
            self.notifications.append(message)

    # Create an instance of the mock listener
    mock_listener = MockListener()

    # Create an instance of the message translator using the mock listener
    translator = AuctionMessageTranslator(mock_listener)

    # Act: Send the test message through the translator
    message = "SOLVersion: 1.1; Event: PRICE; CurrentPrice: 192; Increment: 7; Bidder: Someone else;"
    translator.process_message(message)

    # Assert: Verify the output using ApprovalTests
    verify(mock_listener.notifications)

def test_notifies_bid_details_when_price_message_received_blank():
    message = "SOLVersion: 1.1; Event: PRICE; CurrentPrice: 192; Increment: 7; Bidder: Someone else;"
    # TODO: write a test for this message translation
