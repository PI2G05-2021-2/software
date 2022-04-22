from random import *
from socket import *
import time

serverHost = 'localhost'
serverPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

while True:
    data = sockobj.recv(100)
    print(data.decode())
    tempo = 0
    while True:
        temperatura = uniform(2.5, 10.0)
        tempo = tempo + 1
        potencia = uniform(2.5, 10.0)
        velocidade = randrange(50)
        strg = "{'TEMPERATURA' : '%s', 'TEMPO' : '%s', 'POTENCIA' : '%s', 'VELOCIDADE' : '%s'}"
        argmts = (str(temperatura),str(tempo),str(potencia),str(velocidade))
        msg = strg % argmts
        print(msg)
        sockobj.send(msg.encode())
        time.sleep(2)

        if tempo == 10:
            break
        
    sockobj.close()
    break