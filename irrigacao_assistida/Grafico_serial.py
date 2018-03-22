import matplotlib.pyplot as plt
import numpy as np
import time
import serial #importacao do modulo serial
import random
leitura =[]
fig, ax = plt.subplots()
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #abre porta serial ACM0

i=0
contador = 0
eixo_x = 96
while (1<20):
    while (ser.inWaiting()==0):
     pass
    dados  =int( ser.readline()[:-1])    #firmware deve ter um delay de pelo menos 100ms entre cada envio
    print dados
    ax.clear()
    ax.set_xlim([0,eixo_x])   #faixa do eixo horizontal
    ax.set_ylim([0,100]) # faixa do eixo vertical
    leitura.append(dados)

    ax.plot(leitura)
    plt.pause(.00001)
    fig.savefig('plot.png')
    contador = contador + 1
    if (contador > eixo_x):
	   leitura.pop(0)
    i=i+1

ser.close()
