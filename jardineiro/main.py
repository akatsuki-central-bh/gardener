import time

regar = 0
contador = 1
regar_tempo = 3

while True:
  if(contador - regar) >= regar_tempo * 60:
    print("Regar")
    regar = contador

  contador += 1
  time.sleep(1)
