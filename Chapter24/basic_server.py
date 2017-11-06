# -*- coding:utf-8 -*-

from asyncore import dispatcher
import socket, asyncore

PORT = 5005

class ChatServer(dispatcher):
    """
    一个可在调用结束后自动清理信息的聊天服务器
    """

    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        print 'Connection attemp form ', addr[0]


if __name__ == "__main__":
    s = ChatServer(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass
