import time
import os

if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

inventario=[] #Inventario del Usuario
list1=[]    #Respuesta en Menú
list2=[]
list3=[]
list4=[]
print('Bienvenido al juego')
print()
print('\t--------------------------------------------')
print('\t\tEscoga una opción por favor.')
print('\t--------------------------------------------')
print('\n\t1.) Iniciar Juego\n\t2.) Ayuda\n\t3.) Créditos\n\t4.) Salir')
list1=int(input())
if list1==1:
    print('Cargando juego, por favor espere...')
    time.sleep(3)
    os.system(var)
    print("Apunte las respuestas en un papel por si se cierra el juego de manera inesperada.")
    print('Pulse unicamente los números que se indiquén en pantalla y enter. No pulse ninguna tecla para no tener problemas con su experiencia.')
    time.sleep(15)
    os.system(var)
    import index
elif list1==2:
    print('Cargando menú de ayuda')
elif list1==3:
    print('Ayudado xD troleao lmao')
elif list1==4:
    exit()

#en caso de error
else:
    print('A ocurrido algún error porfavor vuelva a ejecutar nuevamente el código.')