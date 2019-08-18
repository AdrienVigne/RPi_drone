import socket
from traitement_trajectoire import Trajectoire
from time import sleep
"""
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("192.168.1.45",35351))
print("Serveur d'écoute sur le port : ",82700)
sock.listen(5)
print("attente connexion")
connexion,adresse=sock.accept()
print("client conneté ip : %s, port : %s",adresse[0],adresse[1])
"""
x=[]
y=[]
z=[]

f = open('trajectoire.csv','r')
for line in f :
    L = line.split(";")
    L = [float(l) for l in L ]
    x.append(L[0])
    y.append(L[1])
    z.append(L[2])

T=Trajectoire(-1.7545,48.0425,17)
Longitude,Latitude = T.trajet(x,y,z)


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try :
    sock.bind(("192.168.1.62",31000))
except :
    sock.close()
    sock.bind(("192.168.1.62",31000))

print("Serveur d'écoute sur le port : ",31000) # canal de sync
sock.listen(5)
print("attente connexion")
connexion,adresse=sock.accept()
print("client conneté ip : %s, port : %s",adresse[0],adresse[1])

for i in range(len(Longitude)):
    msg = str(i)+'\r\n'
    print(msg)
    connexion.send(msg.encode())
    while connexion.recv(1024).decode() != 'ok':
        sleep(0.05)
        print('attente')

connexion.send('q'.encode())
connexion.close()
sock.close()
