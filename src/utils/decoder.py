import base64

class Decoder:
    input: str
    
    def __init__(self, input):
        self.input = input

    def decode_base64(self):
        bytes= base64.b64decode(self.input)
        return bytes.decode('utf-8')