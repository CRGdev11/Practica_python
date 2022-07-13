#Desafio final paso 7
#Autor CRGD

archivo = open("devices.txt", "a")
while True:
    Newitem = input("Nombre del dispositivo: \n")
    if(Newitem == "quit" or Newitem == "Quit"):
        print("Todo hecho!")
        break
    archivo.write(Newitem + "\n")
archivo.close()