from urllib.parse import quote
from urllib.request import urlopen
import json
import csv
import os

url = "https://apis.datos.gob.ar/georef/api/direcciones?provincia="

def programa_principal():
    # Abro csv con datos de entrada
    loop = 0
    while(loop==0):
        print("#########################################################")
        print("BIENVENIDO AL BUSCADOR DE DIRECCIONES DEL GOBIERNO DE")
        print("LA NACION")
        print("#########################################################")
        print("---------------------------------------------------------")
        print("Este programa utilizara la siguiente API: https://apis.datos.gob.ar/georef/api/direcciones?provincia=")
        print("del Gobierno de la nacion, para extraer datos acerca de un domicilio")
        print("o direccion, que seran validados contra la misma API")
        print("---------------------------------------------------------")
        print("A continuacion, se le solicitara que complete los campos")
        print("para poder buscar una direccion en base a los datos que")
        print("usted proporcione.")
        print("Cuantos mas campos pueda completar, mas informacion precisa")
        print("le sera devuelta. De los 4 campos, hay 2 que seran obligatorios.")
        print("---------------------------------------------------------")
        loop = 12
        while(loop==12):
            enter_para_comenzar = input("Presione enter para comenzar...")
            if len(enter_para_comenzar) == 0:
                print("A continuacion se le solicitaran 5 datos para realizar la busqueda:")
                print("---------------------------------------------------------")
                print("1 - Nombre de calle y el numero que desea buscar * - Campo OBLIGATORIO")
                print("2 - Localidad - Campo No obligatorio, pero se recomienda ingresar una")
                print("3 - Partido - Campo No obligatorio, pero se recomienda ingresar uno")
                print("4 - Provincia * - Campo OBLIGATORIO")
                print("---------------------------------------------------------")
                print("NOTA: Se recomienda ingresar al menos una LOCALIDAD, o un PARTIDO. Si no se ingresa")
                print("ningun dato para estos ultimos, el programa no podra completar la busqueda y regresara al menu principal.")
                print("---------------------------------------------------------")
                loop = 1
                while(loop==1):
                    
                    nombre_calle_y_numero = input("Ingrese la CALLE separada del NUMERO que desea buscar y presione enter: ")
                    if len(nombre_calle_y_numero) < 7:
                        
                        print("---------------------------------------------------------")
                        print("Este campo toma 7 caracteres alfanumericos como mínimo, por favor reingrese el dato.")
                        print("---------------------------------------------------------")
                        loop = 1

                    elif len(nombre_calle_y_numero) >= 7:
                        
                        print("---------------------------------------------------------")
                        print("Calle y numero ingresados: "+nombre_calle_y_numero)
                        loop = 2
                        while(loop==2):
                            
                            confirma_si_no = input("Confirma que es correcto? si/no?...")
                            si = "si"
                            no = "no"
                            if confirma_si_no == si:
                                loop = 3
                                while(loop==3):
                                    print("---------------------------------------------------------")
                                    localidad = input("Ingrese el nombre de una LOCALIDAD y presione enter: ")
                                    print("---------------------------------------------------------")
                                    print("Localidad ingresada: "+ localidad)
                                    print("---------------------------------------------------------")

                                    loop = 4
                                    while(loop==4):
                                        
                                        confirma_si_no = input("Confirma que es correcto? si/no?...")
                                        if confirma_si_no == si:
                                            loop = 5
                                            while(loop==5):
                                                print("---------------------------------------------------------")
                                                partido = input("Ingrese el nombre de un PARTIDO y presione enter: ")
                                                print("---------------------------------------------------------")
                                                print("Partido ingresado: "+ partido)
                                                print("---------------------------------------------------------")
                                                loop = 6
                                                while(loop==6):
                                                    confirma_si_no = input("Confirma que es correcto? si/no?...")
                                                    if confirma_si_no == si:
                                                        loop = 7
                                                        while(loop==7):
                                                            print("---------------------------------------------------------")
                                                            provincia = input("Ingrese el nombre de una PROVINCIA ARGENTINA y presione enter: ")
                                                            if len(provincia) < 5:
                                                                print("---------------------------------------------------------")
                                                                print("Este campo toma al menos 5 caracteres. Por favor reingrese el dato.")
                                                                loop = 7

                                                            elif len(provincia) >= 5:
                                                                
                                                                print("---------------------------------------------------------")
                                                                print("Provincia ingresada: "+ provincia)
                                                                print("---------------------------------------------------------")
                                                                loop = 8
                                                                while(loop==8):
                                                                    confirma_si_no = input("Confirma que es correcto? si/no?...")
                                                                    if confirma_si_no == si:
                                                                        
                                                                        loop = 10
                                                                        while(loop==10):
                                                                            print("---------------------------------------------------------")
                                                                            enter_para_comenzar = input("Presione enter para mostrar los datos crudos de la api ahora...")
                                                                            if len(enter_para_comenzar) == 0:
                                                                                
                                                                                with open('validador_input_nacion.csv', 'w') as file:
                                                                                    
                                                                                    file.write("nombre_calle_y_numero;localidad;partido;provincia;")
                                                                                    file.write('\n'+nombre_calle_y_numero+str(";"))
                                                                                    file.write(localidad+str(";"))
                                                                                    file.write(partido+str(";"))
                                                                                    file.write(provincia+str(";"))
                                                                                    file.close()

                                                                                with open('validador_input_nacion.csv', newline='') as csvfile:
                                                                                    has_header = csv.Sniffer().has_header(csvfile.readline())
                                                                                    csvfile.seek(0)  # Rewind
                                                                                    csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
                                                                                    if has_header:
                                                                                        next(csvreader)  # Me salto la linea de encabezados
                                                                                    # Abro csv para escribir los datos de salida, si existe lo sobreescribe
                                                                                    with open('validador_output_nacion.csv', 'w', newline='') as csvfile:
                                                                                        csvwriter = csv.writer(csvfile, delimiter=';',
                                                                                                             quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                                                                        # Grabo los encabezados
                                                                                        csvwriter.writerow(['nombre_calle', 'numero', 'nombre_localidad', 'mombre_partido', 'nombre_provincia', 'longitud', 'latitud'])
                                                                                        # Recorro los datos de entrada
                                                                                        for row in csvreader:
                                                                                            # Evito las lineas sin id de cliente
                                                                                            if row[0] != "":

                                                                                                try:
                                                                                                    # Identifico los datos de entrada
                                                                                                    nombre_calle_y_numero = row[0]
                                                                                                    localidad = row[1]
                                                                                                    partido = row[2]
                                                                                                    provincia= row[3]
                                                                                                    #longitud = row[4]
                                                                                                    #latitud = row[5]
                                                                                                    #nombre_calle_cruce1 = row[5]
                                                                                                    #nombre_calle_cruce2 = row[6]
                                                                                                    #nombre_partido = row[7]
                                                                                                    #nombre_provincia = row[8]
                                                                                                    provincia_actual= provincia
                                                                                                    direccion_actual = "&direccion=" + nombre_calle_y_numero 
                                                                                                    localidad_actual = "&localidad=" +  localidad
                                                                                                    url_completa = (url + provincia_actual + localidad_actual + direccion_actual).replace(' ', '%20')
                                                                                                    print(url_completa)
                                                                                                    portal = urlopen(url_completa)
                                                                                                    html = portal.read().decode("utf8")
                                                                                                    print("------------------------------------------")
                                                                                                    jason = json.loads(html)
                                                                                                    print(jason)
                                                                                                    
                                                                                                    
                                                                                                    #direcciones = str(jason.get("direcciones")[0]['calle'])
                                                                                                    nombre_calle = str(jason.get("direcciones")[0]['calle']['nombre'])
                                                                                                    numero = str(jason.get("direcciones")[0]['altura']['valor'])
                                                                                                    nombre_calle_cruce1 = str(jason.get("direcciones")[0]['calle_cruce_1']['nombre'])
                                                                                                    nombre_calle_cruce2 = str(jason.get("direcciones")[0]['calle_cruce_2']['nombre'])
                                                                                                    nombre_localidad = str(jason.get("parametros")['localidad'])
                                                                                                    nombre_partido = str(jason.get("direcciones")[0]['departamento']['nombre'])
                                                                                                    nombre_provincia = str(jason.get("direcciones")[0]['provincia']['nombre'])
                                                                                                    longitud = str(jason.get("direcciones")[0]['ubicacion']['lat'])#.replace('.', ',')
                                                                                                    latitud = str(jason.get("direcciones")[0]['ubicacion']['lon'])#.replace('.', ',')

                                                                                                    with open('validador_output_nacion.csv', 'w') as file:
                                                                                                        file.write("Calle"+";"+"Numero"+";"+"Localidad"+";"+"Partido"+";"+"Provincia"+";"+"Longitud"+";"+"Latitud")
                                                                                                        file.write('\n'+nombre_calle+str(";")+numero+str(";")+nombre_localidad+str(";")+nombre_partido+str(";")+nombre_provincia+str(";")+longitud+str(";")+latitud+str(";"))
                                                                                                        file.close()
                                                                                                        
                                                                                                    print("------------------------------------------")
                                                                                                    input("Presione enter para ver los datos formateados en pantalla ahora...")
                                                                                                    print("------------------------------------------")
                                                                                                    print("Calle y altura encontrados: "+ nombre_calle + " "+numero)
                                                                                                    print("------------------------------------------")
                                                                                                    print("Localidad encontrada: "+nombre_localidad)
                                                                                                    print("------------------------------------------")
                                                                                                    print("Partido encontrado: "+nombre_partido)
                                                                                                    print("------------------------------------------")
                                                                                                    print("Provincia encontrada: "+nombre_provincia)
                                                                                                    print("------------------------------------------")
                                                                                                    print("Datos adicionales encontrados.")
                                                                                                    print("Coordenadas en base a la direccion suministrada realizada: ")
                                                                                                    print("------------------------------------------")
                                                                                                    print("Longitud: "+longitud)
                                                                                                    print("------------------------------------------")
                                                                                                    print("Latitud: "+latitud)
                                                                                                    print("------------------------------------------")
                                                                                                    print("Se han generado 2 archivos en este directorio: ")
                                                                                                    os.system('pwd')
                                                                                                    print("------------------------------------------")
                                                                                                    print("1 - Un archivo llamado validador_output_nacion.csv")
                                                                                                    print("2 - Un archivo llamado direccion_json.json")
                                                                                                    print("------------------------------------------")
                                                                                                    
                                                                                                    with open("direccion_json.json", 'w') as json_file:
                                                                                                        json_file.write(html)
                                                                                                        json_file.close()

                                                                                                        
                                                                                                        loop = 11
                                                                                                        while(loop==11):
                                                                                                            print("El programa ha finalizado.")
                                                                                                            vuelta_a_menu = input("Presione enter para regresar al menu principal a realizar otra busqueda...")
                                                                                                            if len(vuelta_a_menu) == 0:
                                                                                                                programa_principal()
                                                                                                            elif len(vuelta_a_menu) > 0:
                                                                                                                print("------------------------------------------")
                                                                                                                print("Solo presione enter para regresar al menu principal...")
                                                                                                                print("------------------------------------------")        
                                                                                                except:
                                                                                                    print("---------------------------------------------------------")
                                                                                                    print("NOTA: INGRESE AL MENOS EL NOMBRE DE UNA LOCALIDAD, O EL NOMBRE DE UN PARTIDO VALIDO,")
                                                                                                    print("NO SE PUDO COMPLETAR LA BUSQUEDA CON LOS DATOS SOLICITADOS.")
                                                                                                    print("---------------------------------------------------------")
                                                                                                    print("Regresando al inicio del programa.")
                                                                                                    programa_principal()


                                                                            elif len(enter_para_comenzar) > 0:
                                                                                print("---------------------------------------------------------")
                                                                                print("Solo presione enter para mostrar los datos...")
                                                                                loop = 10




                                                                    elif confirma_si_no == no:
                                                                        print("---------------------------------------------------------")
                                                                        loop = 7

                                                                    else:
                                                                        print("---------------------------------------------------------")
                                                                        print("Por favor solo ingrese 'si' o 'no'.")
                                                                        loop = 8

                                                                                                                                                
                                                                    
                                                                    


                                                    if confirma_si_no == no:
                                                        print("---------------------------------------------------------")
                                                        loop = 5


                                                    else:
                                                        print("---------------------------------------------------------")
                                                        print("Por favor solo ingrese 'si' o 'no'.")
                                                        loop = 6
                                                        
                                                        
                                            

                                        if confirma_si_no == no:
                                            print("---------------------------------------------------------")
                                            loop = 3

                                        else:
                                            print("---------------------------------------------------------")
                                            print("Por favor solo ingrese 'si' o 'no'.")
                                            loop = 4
                                                        
                                

                            if confirma_si_no == no:
                                print("---------------------------------------------------------")
                                loop = 1

                            else:
                                print("---------------------------------------------------------")
                                print("Por favor solo ingrese 'si' o 'no'.")
                                loop = 2

                    

            elif len(enter_para_comenzar) > 0:
                print("---------------------------------------------------------")
                print("Solo presione enter para regresar para comenzar el programa...")
                print("---------------------------------------------------------")
                loop = 12
                    
programa_principal()

                    
                    
                                                    
        
        
