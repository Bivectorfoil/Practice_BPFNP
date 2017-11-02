# -*- coding:utf-8 -*-

from nntplib import NNTP
# from time import time, strftime, localtime


# day = 24 * 60 * 60
# yesterday = localtime(time() - day)
# date = strftime('%y%m%d', yesterday)
# hour = strftime('%H%M%S', yesterday)
#
# servername = 'freenews.netfront.net'
# # servername = 'news.vsi.ru'
# group = 'comp.lang.python.annouuce'
# server = NNTP(servername, readermode=True)
#
# ids = server.newnews(group, date, hour)[1]  # for some resons, newnews method
# will return 502 NEWNEWS command disabled by administrator error.

servername = 'freenews.netfront.net'
groupname = 'comp.lang.python.announce'
server = NNTP(servername, readermode=True)

response, count, first, last, name = server.group(groupname)
resp, subs = server.xhdr('subject', (str(first) + '-' + str(last)))
for sub in subs[:5]:  # print the last ten subjects
    id = sub[0]
    head = server.head(id)[3]
    for line in head:
        if line.lower().startswith('subject:'):
            subject = line[9:]
            break
    body = server.body(id)[3]

    print subject
    print '-' * len(subject)
    print '\n'.join(body)

server.quit()
