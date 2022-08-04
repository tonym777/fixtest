
class BaseMessage:

    def __init__(self):
        self.header = {}
        self.body = {}
        self.tailer = {}

    def build_fix_message(self):
        message = '\x01'.join(str(key) + '=' + str(value) for key, value in self.header.items()) + '\x01'
        message += '\x01'.join(str(key) + '=' + str(value) for key, value in self.body.items()) + '\x01'
        self.tailer['10'] = self.compute_check_sum(message)
        message += '\x01'.join(str(key) + '=' + str(value) for key, value in self.tailer.items())
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

    def get_field(self, tag):
        if self.body.get(tag):
            return self.body[tag]
        if self.header.get(tag):
            return self.header[tag]
        if self.tailer.get(tag):
            return self.tailer[tag]

    @staticmethod
    def compute_check_sum(fix):
        check_sum = 0
        for c in fix:
            check_sum += ord(c)
        check_sum = check_sum % 256
        return check_sum
