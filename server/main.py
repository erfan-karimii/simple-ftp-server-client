from twisted.cred.checkers import AllowAnonymousAccess , InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory , FTPRealm

# IP_ADDR = "87.248.153.134"
IP_ADDR = "127.0.0.1"
PORT = 21


checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("erfan","123")
checker.addUser("masoud","123")


portal = Portal(FTPRealm("./public","./private"),[AllowAnonymousAccess(),checker])

factory = FTPFactory(portal)
reactor.listenTCP(PORT,factory,interface=IP_ADDR)
print(f"Starting FTP server on {IP_ADDR}:{PORT}...")
reactor.run() 
