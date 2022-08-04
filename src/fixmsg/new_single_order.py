import uuid

from .base_message import BaseMessage


class NewSingleOrder(BaseMessage):
    sender_comp_id = "firm"
    target_comp_id = "venue"

    def __init__(self, symbol, side, price, size, venue=None):
        super().__init__()
        super().set_header({'49': self.sender_comp_id, '56': self.target_comp_id, '35': 'D'})
        super().set_body({'11': uuid.uuid1(), '55': symbol, '38': size, '44': price, '40': '2', '54': side})

