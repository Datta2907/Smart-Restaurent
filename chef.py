import socket
s = socket.socket()
port = 60000
print("\n Server is listing on port :")
s.bind(('', port)) 
s.listen(5)
file = open("order.txt", "wb") 
print("\n opening file\n")
conn, addr = s.accept()
print("\n File has been copied successfully")
conn.close()
print("\n Server closed the connection")
