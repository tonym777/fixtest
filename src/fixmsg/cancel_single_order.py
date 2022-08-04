import uuid

from .base_message import BaseMessage


class CancelSingleOrder(BaseMessage):
    sender_comp_id = "firm"
    target_comp_id = "venue"

    def __init__(self, order_id):
        super().__init__()
        super().set_header({'49': self.sender_comp_id, '56': self.target_comp_id, '35': 'F'})
        super().set_body({'11': uuid.uuid1(), '41': order_id})
