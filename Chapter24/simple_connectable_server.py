# -*- coding:utf-8 -*-

from asyncore import dispatcher
import socket, asyncore


class ChatServer(dispatcher):

    def handle_accept(self):
        conn, addr = self.accept()
        print 'connection attempt from ', addr[0]


s = ChatServer()
s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5005))
s.listen(5)
asyncore.loop()
