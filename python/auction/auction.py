
class AuctionEventListener:
    # TODO: add methods here
    def notify(self, message):
        return message

class AuctionMessageTranslator:
    def __init__(self, listener: AuctionEventListener):
        self.listener = listener

    def process_message(self, message: str):
        if "CLOSE" in message:
            self.listener.notify("Auction Closed")

        elif "PRICE" in message:
            data = {}
            for element in message.split(";"):
                if not element:
                    continue
                pair = element.split(":")
                data[pair[0].strip()]  = pair[1].strip()

            current_price = int(data["CurrentPrice"])
            increment = int(data["Increment"])
            bidder = data["Bidder"]
            # 'Someone else bid 199'
            notification_message = f"{bidder} bid {current_price+increment}"

            self.listener.notify(notification_message)

        else:

            self.listener.notify("ERROR: Received a Blank Message")
            pass

