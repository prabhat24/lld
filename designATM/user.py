
import uuid


class User():

    def __init__(self, username, phone_number, address):
        self.cid = uuid.uuid4()
        self.username = username
        self.phone_number = phone_number
        self.address = address