import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre del ordenador es: " + hostname)
print("Tu direccion Ip es: " + ip)