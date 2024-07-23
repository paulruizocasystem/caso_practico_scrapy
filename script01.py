import re #expresiones regulares#
from colorama import Fore #colores#
import requests #peticiones hhttp a paginas web#

website = "https://www.vulnhub.com/"
resultado = requests.get(website)
content = resultado.text
#print(content)

patron = r"/entry/[\w-]*"
maquinas_repetidas = re.findall(patron, str(content))
#print(maquinas_repetidas)
sin_duplicados = list(set(maquinas_repetidas))
#print(sin_duplicados)

maquinas_final = []

for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)
#print(maquinas_final)

#####################
#¿Qué pasa si añaden una maquina nueva?

maquina_noob = "noob-1"
existe_noob = False

for a in maquinas_final:
    if a == maquina_noob:
        existe_noob = True
        break

##Usando la libreria colorama: 
color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW

#if existe_noob == True:
    #print(color_verde + "No hay ninguna maquina nueva")
#else:
    #print(color_amarillo + "Máquina Nueva")