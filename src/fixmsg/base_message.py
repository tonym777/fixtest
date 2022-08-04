
class BaseMessage:

    def __init__(self):
        self.header = {}
        self.body = {}
        self.tailer = {}

    def build_fix_message(self):
        message = '\x01'.join(key + "=" + value for key, value in self.header.items()) + '\x01'
        message += '\x01'.join(key + "=" + value for key, value in self.body.items()) + '\x01'
        message += '\x01'.join(key + "=" + value for key, value in self.tailer.items())
        return message

    def set_header(self, header):
        for key, value in header.items():
            self.header[key] = value

    def set_body(self, body):
        for key, value in body.items():
            self.body[key] = value

    def set_tailer(self, tailer):
        for key, value in tailer.items():
            self.tailer[key] = value
