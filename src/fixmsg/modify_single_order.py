import uuid

from .base_message import BaseMessage


class ModifySingleOrder(BaseMessage):
    sender_comp_id = "firm"
    target_comp_id = "venue"

    def __init__(self, order_id, price, size):
        super().__init__()
        super().set_header({'49': self.sender_comp_id, '56': self.target_comp_id, '35': 'G'})
        super().set_body({'11': uuid.uuid1(), '41': order_id, '38': size, '44': price})
