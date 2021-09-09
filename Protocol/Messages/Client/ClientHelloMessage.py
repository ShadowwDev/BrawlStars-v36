from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Protocol.Messages.Server.ServerHelloMessage import ServerHelloMessage
from Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

class ClientHelloMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.helpers = Helpers()

    def decode(self):
        pass

    def process(self, db):
        ServerHelloMessage(self.client, self.player).send()
        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()



