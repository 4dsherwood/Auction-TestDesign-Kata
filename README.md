Auction Test Design Kata
========================

There are bugs in the code, clearly marked. Write tests that expose the bugs.

Next Steps
----------
Write tests for a new message type: "CLOSE_NO_SALE" which tells you the reserve price on the item was not met. The listener should be notified both that the auction closed, but also the reserve price. Sample message:

	SOLVersion: 1.1; Event: CLOSE; ReservePrice: 200;

Acknowledgements
----------------
This is inspired by the example in the book "Growing Object Oriented Software, Guided by Tests" by Steve Freeman and Nat Pryce

  ~~~--------~~~~~ Our observations ~~~~~ -----
TDD
Write tests that expose the bugs.

"CLOSE_NO_SALE"  might be related to the Reserve price
new message type: "CLOSE_NO_SALE"
notify the listener:
1) auction closed
2) ReservePrice = 200
