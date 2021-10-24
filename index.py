import time #Sistema de cooldown
import os #Sistema de CLS

#Sistema de CLS (Requiere importar os)
if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

list1 = [] #Que vas a hacer linea 34
list2 = [] #Que vas a hacer linea 73
list3 = [] #Que vas a hacer linea 118
list4 = [] #Que vas a hacer linea 
list5 =  [] #Que vas a hacer linea 

print('Te despiertas, estas en tu habitación dormido, está sonando la alarma del teléfono. Ves que son las 6:00 AM.')
print()
time.sleep(5)
print('Recuerdas que tienes un examen de Sociales, del cual no estudiástes mucho que digamos. Por eso has madrugado, para intentare aprobarlo.')
print()
time.sleep(7)
print('Escuchas una fuerte explosión...')
print()
time.sleep(3)
print('Te asomas por la ventana para ver que ha ocurrido.')
print()
time.sleep(3)
print('Ves que explotó la central nuclear de Columbus, Ohio.')
print()
time.sleep(4)
print('Cuando se acerca la honda expansiva sientes algo raro en tu mente, pero lo ignoras completamente.')
print()
time.sleep(4)
print('¿Que vas a hacer?')
print('\n\t1.- Avisar a todos tus familiares dentro de tu hogar.\n\t2.- Llamar a emergencias e informar de la situación.\n\t3.- Seguir durmiendo\n\t4.- Te da igual lo que ocurra y te pones a estudiar sociales.')
list1=int(input())
if list1==1: #Avisar a todos tus familiares
    os.system(var)
    print('Vas corriendo por todas las habitaciones de la casa. Pegando gritos para que se despierten tus familiares.')
    print()
    time.sleep(7)
    print('Despiertas a tus padres y hermano, preguntándote que ocurre.')
    print()
    time.sleep(5)
    print('Les explicas que ha habido una explosión en la central nuclear.')
    print()
    time.sleep(4)
    print('Cogeís lo más importante y llamais al número de emergencias para seguir los consejos del gobierno.')
    print()
    time.sleep(4)
    print('La linea de emergencias esta colapsada, de todas formas haceís lo que a veces dicen que hay que hacer en caso de desastres.')
    print()
    time.sleep(6)
    print('Cogeís el auto y os vais al chalet que esta alejado de la ciudad. Tiene todas la cosas necesarias para estos casos.')
    print()
    time.sleep(5)
    print('Entonces estas un poco mareado y recuerdas lo que te pasó cuando la explosión. Empiezas a escuchar voces...')
    print('')
    time.sleep(5)
    print('Pero tu hermano te llama para que veas las noticias. Te diriges al salón donde se encuentran tus padres y ves las noticias.')
    print()
    time.sleep(7)
    print('Noticia de Ultima Hora: La explosión de la central fue ocasionado por un individuo, actualmente esta en prisión.')
    print('El acusado se declara inocente, aunque no hay ninguna prueba que lo respalde.')
    print()
    time.sleep(10)
    print('Empiezas a escuchar voces fuertemente en tu mente, la voz te suena de haberlo oido en alguna parte, era el prisionero.')
    print()
    time.sleep(5)
    print('No para de decirte que el es inocente y que estaba en otra parte, pero las pruebas que lo respaldan no están donde los policias habian buscado')
    print()
    time.sleep(10)
    print('¿Que vas a hacer?')
    print('\n\t1.) Intentar ponerte en contacto con el mediante los poderes\n\t2.) Llamar a la policia para infomar de las voces.\n\t3.) Te tomas un paracetamol')
    list2=int(input())
    if list2 ==1: # Intentar ponerte en contacto con el prisionero
        os.system(var)
        print('Vas a tu cuarto y cierras la puerta. Intentas concentrar la mayor energía y concentración para mandarle tu mensaje al prisionero.')
        print()
        time.sleep(7)
        print('Te dice de dirijirte a un puente por la noche para contarte que ha pasado y poder demostrar la verdad. No se preocupara por nada, nadie sabría que se iba a escapar ni nada, lo tiene todo preparado.')
        print()
        time.sleep(6)
        print('Quedaís el día 16 a las 16:00 para poder demostrar la verdad a la gente y no ponerles como mala persona.')
        print()
        time.sleep(5)
    if list2 ==2:
        os.system(var)
        print('Continuara...')
elif list1==2: #Llamar a emergencias e informar de la situación
    os.system(var)
    print('Coges el teléfono y marcas el número de emergencias. Te atiende una señora')
    time.sleep(4)
    print('-- Inicio de llamada --')
    time.sleep(2)
    print(' Señora - 911 ¿Cual es su emergencia?')
    print()
    time.sleep(2)
    print('Yo - ¡Ha habido una explosión en la Central Nuclear de Columbus')
    print()
    time.sleep(2)
    print(' Señora - El equipo de bomberos se está encargando de ello. Por favor siga las ordenes que hay en emision en los canales de TV y mantenga libre la línea. Gracias.')
    print()
    time.sleep(7)
    print('-- Fin de llamada --')
    time.sleep(5)
    os.system(var)
    print('Enciendes la TV, todos los canales emiten lo mismo: ☢ ABANDONEN SUS CASAS INMEDIATAMENTE. NIVEL DE EMERGENCIA 10 ☢ .')
    print()
    time.sleep(6)
    print('Avisas a tus padres y hermano de lo que ocurre, y cojeís el coche para ir al chalet que esta apartado de la ciudad.')
    print()
    time.sleep(6)
    print('Te dirijes hacia tu habitación, te empieza a doler la cabeza bruscamente. Y empiezas a escuchar unas voces.')
    print()
    time.sleep(4)
    print('Le dices que no te encuentras muy bien y que te quedarías en tu habitación. Ellos no saben lo de las voces... Empiezas a escucharlas, dicen que es inocente y que las pruebas estan donde no han revisado')
    print()
    time.sleep(10)
    print('Decides ir a ver que esta ocurriendo en el salón. A lo mejor no son voces y es la television. Pero en la televisión solo estaba en emisión el mensaje de alerta.')
    print()
    time.sleep(10)
    print('¿Que vas a hacer?')
    print()
    print('\n\t1.) Investigar el mensaje de las voces y de quienes son.\n\t2.) Tomarte un paracetamol y a echarte una siesta para no seguirlas escuchando.')
    list3=int(input())
    if list3==1: #Investigar mensaje de las voces y de quienes son
        print('')
    elif list3==2: #Tomarse un paracetamol y ehcarse una siesta.
        os.system(var)
        print('Te tomas un paracetamol y tratas de hecharte una siesta')
elif list1==3: #Seguir durmiendo SEGUIR DESARROLLANDO IDEA MARTA
    os.system(var)
    print('Sientes la alarma del teléfono, la pospones para una hora más tarde.')
    print()
    time.sleep(5)
    print('Sigues posponiendo la alarma, te despiertas a las 10 A.M. No ves a nadie que este en casa, enciendes la TV como de costumbre pero en todos los canales sale un mensaje que dice: ☢ DIRIJANSE A LAS AFUERAS DE LA CIUDAD INMEDIATAMENTE. NIVEL DE EMERGENCIA 10 ☢.')
    print()
    time.sleep(6)
    print('Coges el auto y te vas para el chalet')
    print()
    time.sleep(5)
    print('Y cuando llegas sigues durmiendo por una tremenda resaca.')
    print()
    time.sleep(4)
    print('Entonces empiezas a escuchar unas voces en tu cabeza que dicen que dicen de ir a un puente por la noche... Sin nadie más.')
    print()
    time.sleep(7)
    print('Piensas que es de la resaca, pero este te responde diciendote que no, no es una resaca, entonces te levantas de la cama pensando en lo que te ha pasado')
    print()
    time.sleep(7)
    print('Te empieza a decirte una dirección de alguna calle de Columbus Norte ¿Que decides hacer?')
    print()
    print('\n\t1.) Decides apuntarlo en un papel\n\t2.) Piensas que es tu subconsciente y que estas dormido.\n\t3.) Llamas a la policia')
    list4=int(input())
    if list4==1: #Decides apuntarlo e ir
        os.system(var)
        print('Coges un papel y bolígrafo que estaba en la mesa, y apuntas la dirección que te han dado. Puente "Las Manolitas" a las 1:00 AM en la esquina del arbol dentro del parque Don Bermejo.')
        print()
        time.sleep(7)
        print('También te dice que no se lo digas a nadie, solo tu puedes ir.')
        print()
        time.sleep(4)
        print('Esperas a que sea de noche, decides ir a un restaurante para paliar un poco los nervios.')
        print()
        time.sleep(5)
        print('Te pides una hamburguesa, ves que se esta acercando la hora, te tomas lo que queda de hamburguesa y te vas hacia el auto, ya que el sitio esta un poco retirado de donde esta tu chalet')
        print()
        time.sleep(7)
        print('Pasas por el puente "Las Manolitas", el cual esta muy oscuro, sales del auto a unos pocos metros de la entrada del parque Don Bermejo.')
        print()
        time.sleep(6)
        print('Te diriges hacia el arbol que te indico, puedes ver claramente a un chico, no más de 25 años, con sudadera negra con capucha puesta, entonces escuchas una fuerte voz en tu cabeza, es el.')
        print()
        time.sleep(8)
        print('Te empieza a contarte lo que ocurrió...')
        print()
        time.sleep(4)
        os.system(var)
        print('Chico - Yo realmente no soy culpable de la explosión...')
        print()
        time.sleep(4)
        print('Tu - ¿Que pasó?')
        print()
        time.sleep(3)
        print('Chico - Estaba junto a unos amigos, cerca de la explosión, estabamos investigando en una casa abandonada, en la cual era muy extraña, muchos cables y palancas...')
        print()
        time.sleep(7)
        print('Chico - La casa estaba dividida en 2 plantas y un sotano. Nos dirijimos a las plantas de arriba, escuchabamos cosas raras dentro de la casa, sentiamos que habia alguien más dentro de la casa.')
        print()
        time.sleep(9)
        print('Chico - Nos fijamos en algunos papeles que habia en esa casa. La gran mayoría eran planos de la Central Nuclear, y de otros sitios que no sabía de donde era.')
        print()
        time.sleep(7)
        print('Chico - Decidimos subir a la planta de arriba y ver que habia, se escuchaban pasos, algunos muy cercanos, apareció un señor, después de vernos bajo corriendo las escaleras. Y entonces sonó la explosión.')
        print()
        time.sleep(6)
        print('Chico - Entonces nos llego la onda expansiva, la cual nos dejo inconscientes durante unos minutos, al menos a mis amigos, a mi me dio un golpe muy fuerte en la cabeza. Y tarde unas horas en despertar.')
        print()
        time.sleep(7)
        print('Chico - Los policias revisaron los alrededores y me encontraron en el sotano, el que lo voló me llevo hacia el sotano y puso mis huellas en la palanca que detonó la bomba, al tener las huellas no decidieron buscar más cosas y decidieron arrestarme.')
        print()
        time.sleep(9)
        print('Chico - Necesito que vayas allí y los recogas para demostrar mi inocencia ya que el que lo provocó sigue libre y podrá hacer algo más grave... ¿Me puede ayudarme?')
        print()
        time.sleep(8)
        print('Decide lo que vas a hacer')
        print()
        print('\n\t1.) Ir hacia la casa abandonada.\n\t2.) Irte corriendo de allí.\n\t3.) Pedirle más información al chico.')
        list5=int(input())
        if list5==1:
            os.system(var)
            print('Te diriges al coche, te pones a pensar si es buena idea...')
            time.sleep(5)
            print()
            print('(Creo que no es un buen plan...) (Y si es una enredada) (Y si  es verdad... Hay madre que voy a hacer...)')
            time.sleep(3)
            print('(no es que sea buena idea acercarse, seguramente habrá policias cerca y demasiada radiación, ¿como haré para salvarle?, me acercaré al sitio haber que encuentro, voy a por protección e ire a la carga.)')
            time.sleep(5)
            print()
            print('Te diriges hacia ')

    elif list4==2: #Piensas que es tu subconsiente
        os.system(var)
        print('No amiguito, no soy tu subconsciente, porque no se lo que hay alrededor tuya ni puedo mover brazos ni pies. Si quieres saber quien soy vente al Parque Don Bermejo pasando el puente de Las Manolitas, allí te lo explicará todo.')
    elif list4==3:
        os.system(var)
        print('')
elif list1==4: #Estudiar el exámen de Sociales
    os.system(var)
    print('Coges el libro de sociales y empiezas a estudiarte el tema que te vas a examinar')
    print()
    time.sleep(4)
    print('Te empieza a sonar el teléfono, es el grupo de clase. El profesor a suspendido las clases por la situación que hay.')
    print()
    time.sleep(4)
    print('Aún asi decides estudiar, tus padres te llaman para ir a un sitio seguro fuera de la ciudad.')
    print()
    time.sleep(4)
    print('Os dirigís a vuestro chalet que esta apartado de la ciudad para evitar una mayor radiación.')
    print()
    time.sleep(5)
    print('Entras a tu habitación del chalet, pero te empieza a dolerte muy fuertemente la cabeza, sientes... voces.')

#En caso de error, sale mensaje de error y reinicia el juego desde menú.
else:
    os.system(var)
    print('A ocurrido un error, se ejecutara nuevamente el menú. Por favor espere...')
    time.sleep(5)
    os.system(var)
    import menu