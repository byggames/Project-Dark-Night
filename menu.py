import time #Sistema Cooldown
import os #Sistema de CLS

if os.name == "posix": #Sistema de CLS
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

list1=[]    #Respuesta en Menú
os.system(var)
print('Bienvenido al juego')
print()
print('\t<-------------------------------------------->')
print('\t\tEscoga una opción por favor.')
print('\t<-------------------------------------------->')
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
    print('No hay, recargando juego...')
    time.sleep(3)
    os.system(var)
    import menu

elif list1==3:
    print('En desarrollo... No disponible, redirigiendo al menú...')
    time.sleep(3)
    os.system(var)
    import menu
    
elif list1==4:
    os.system(var)
    exit()

#en caso de error, se vuelve a ejecutar el menú
else:
    os.system(var)
    print('A ocurrido algún error, recargando juego. Por favor espere')
    time.sleep(4)
    os.system(var)
    import menu