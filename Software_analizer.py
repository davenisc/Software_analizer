#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
import os.path
import csv
import time
from functools import reduce
import re
#import json
from os import path
from colorama import Back, Fore, init, Style
from time import sleep
from tqdm import tqdm


def almacenardatos():
    """a='cualquier cosa'
    print('si funciona esta chimbada')
    return a"""
    init()
    print (Fore.WHITE +"_____________________________________________________________________________________________________________________\n")
    init()
    print(Fore.RED + "Coincidencias de (port) o puertos encontrados "+Fore.GREEN+" **************************************")
    print ("")
    RED = '\033[1;31m'
    NOCOLOR = '\033[0;0m'

    palabras4 = ['tcp', '.com', 'n/a']

    palabra4 = 'tcp'
    ocurrencias4 = []
    with open('doc.txt') as lineas:
        for linea in lineas:
            if palabra4 in linea:
                ocurrencias4.append(linea)

    
        #print(aImprimir4)
    return ocurrencias4

def crear_archivo():
    if path.exists('prueba1.txt'):
        print('El archivo ya existe')
        file=open("prueba1.txt", "a")
    else:
        file=open("prueba1.txt", "a")
        print('El archivo fue creado')

        pass    

def menu():

    """
Inicio logo         ###################################################################
    """
#Color de texto inicio  ################################################################
#Color de texto fin  ###################################################################
print ("")
print ("")
print ("")
init()
print(Fore.RED + "Software link "+Fore.GREEN+" : https://github.com/davenisc")
init()
print(Fore.RED + "Description "+Fore.GREEN+"   : SCRIPT FOR RAPID SOFTWARE ANALYSIS")
init()
print(Fore.RED + "Contact Mail "+Fore.GREEN+"  : sysvd@protonmail.com")

#Color de texto inicio ###################################################################

#Color de texto fin    ###################################################################
init()
print(Fore.WHITE + "________________________________________________")
print ("                                                            ")
init()
print(Fore.CYAN + "    ____         __ _                             ")
init()   
print(Fore.CYAN + "   / ___|  ___  / _| |___      ____ _ _ __ ___    ")
init()
print(Fore.CYAN + "   \___ \ / _ \| |_| __\ \ /\ / / _` | '__/ _ \   ")
init()
print(Fore.CYAN + "    ___) | (_) |  _| |_ \ V  V / (_| | | |  __/   ")
init()
print(Fore.CYAN + "   |____/ \___/|_|  \__| \_/\_/ \__,_|_|  \___|   ")
init()                
print(Fore.GREEN + "                 _             _ _              ")
init()
print(Fore.GREEN + "                /_\  _ _  __ _| (_)______ _ _   ")
init()
print(Fore.GREEN + "               / _ \| ' \/ _` | | |_ / -_) '_|  ")
init()
print(Fore.GREEN + "              /_/ \_\_||_\__,_|_|_/__\___|_|    ")
init()
print(Fore.RED + "    --------------------------------------------- ")
init()
print(Fore.RED + "    | @DaveNISC |              |  @whitepadawan |")
init()
print(Fore.RED + "    --------------------------------------------- ")
init()                  
print(Fore.RED + "    |           |              |                |")
print("")
init()
print (Fore.GREEN +"                By SySvd  | v 0.1              \n")
init()
print (Fore.WHITE +"________________________________________________\n")

#print ("")  
#print ("")  

#Color de texto inicio 

 
#Color de texto fin
"""
fin logo
"""
"""
Funci�n que limpia la pantalla y muestra nuevamente el menu
"""
#os.system('clear') # NOTA para windows tienes que cambiar clear por cls

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Enter an option: "))
            correcto=True
        except ValueError:
            print('Error, enter an option')
            print ("")
     
    return num
 
salir = False
opcion = 0

while not salir:

    init()
    print(Fore.RED + "Run Terminal"+Fore.GREEN+"      Root")
    init()
    print(Fore.RED + "Run CMD"+Fore.GREEN+"           Administrator \n\n")
 
    init()
    print(Fore.RED + "1. "+Fore.WHITE+" Analyze software ")
    init()
    print(Fore.RED + "2. "+Fore.WHITE+" See result       ")
    init()
    print(Fore.RED + "3. "+Fore.WHITE+" What is software analyzer")
    init()
    print(Fore.RED + "4. "+Fore.WHITE+" Exit")
    print ("") 
    print ("Choose an option")
    print ("") 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:

        ############################################################################################################
        
        print ("")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Analyze software\n\n")
        soft_a = raw_input('Drag the software to be analyzed here\n\n >>> ')
        print("")
        for i in tqdm(range(100)):
            sleep(0.02)
        print("")    

        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" We will start the analysis of this software " +Fore.GREEN+ " please wait! " +Fore.WHITE+ "<*>\n")
        init()
        print(Fore.RED + "[*]"+Fore.WHITE+" Better go and have a coffee while the information collection process finishes, the script will go back to the main menu when the scan finishes. " +Fore.GREEN+ "" +Fore.WHITE+ "")
        print("")
        init()
        print(Fore.RED + "   ( ( "+Fore.WHITE+"")
        init()
        print(Fore.RED + "    ) ) "+Fore.WHITE+"")
        init()
        print(Fore.RED + "  ........"+Fore.WHITE+"")
        init()
        print(Fore.RED + "  |      |]"+Fore.WHITE+"  go!! ")
        init()
        print(Fore.RED + "  \      / "+Fore.WHITE+"  and have   ")
        init()
        print(Fore.RED + "   `----'"+Fore.WHITE+"    a coffee   ")
        print("")

        
        #os.system("gnome-terminal -e 'ping 8.8.8.8'")
        #command = '  nslookup ' + url_analyze +  ' > scan_ip.txt '

        #os.system(command)

        command = '  md5sum  ' + soft_a +  ' > log_hash.txt '

        os.system(command)

        search_hash = open('hash.txt','w')

        regex = '[A-Za-z-0-9]{32,32}'


        datos2 = open('log_hash.txt')
        for line2 in datos2:
            line2 = line2.rstrip()
            y = re.findall('[A-Za-z-0-9]{32,32}', line2)
            if len(y) > 0 :
                search_hash.write(str(y[0]+ "\n"))
                #print (y[0])

        search_hash = open('hash.txt','w')


        lines = [line.strip() for line in open('log_hash.txt', 'r')]
        for x in lines:
            found_h = re.search('[A-Za-z-0-9]{32,32}', x)
            if found_h:
                search_hash.write(x + "\n")


        command = '  automater  ' + 'has.txt' +  ' > log_scan.txt '
        os.system(command)

        command = '  exiftool  ' + soft_a +  ' > log_metadata.txt '

        os.system(command)
    
        for i in tqdm(range(100)):
            sleep(0.02) 
        print("") 

        init()
        print(Fore.RED + "[*]"+Fore.GREEN+" Finished analysis }:) \n\n")
        print ("")
        time.sleep(5)
        os.system('clear')
        
    elif opcion == 2:

        ############################################################################################################
        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" Hash found (MD5)\n")

        print_hash = open('hash.txt','r')

        #[for].[0-9]+.[0-9]+.[0-9]+.[0-9]+ IP del server
        #[0-9].+[a-z]\s*[a-z]+\s\s[a-z]+ puerto 

        regex = '[A-Za-z-0-9]{32,32}'

        list_hash = []

        for line2 in print_hash:
            line2 = line2.rstrip()
            y = re.findall('[A-Za-z-0-9]{32,32}', line2)
            if len(y) > 0 :
                if y[0] not in list_hash:
                    list_hash.append(y[0])
                    print (y[0])
        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        ########################################################################################

        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+" Data found (Metadata)\n")

        print_data = open('log_metadata.txt','r')

        #[for].[0-9]+.[0-9]+.[0-9]+.[0-9]+ IP del server
        #[0-9].+[a-z]\s*[a-z]+\s\s[a-z]+ puerto 

        regex = '[\w].+'

        list_data = []

        for line3 in print_data:
            line3 = line3.rstrip()
            b = re.findall('[\w].+', line3)
            if len(b) > 0 :
                if b[0] not in list_data:
                    list_data.append(b[0])
                    print (b[0])
        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")
        
        #######################################################################################################

        print ("")    

        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        
        print(Fore.RED + "[*]"+Fore.WHITE+"  Malware analysis result (AV)\n")

        print_data = open('log_scan.txt','r')

        #[for].[0-9]+.[0-9]+.[0-9]+.[0-9]+ IP del server
        #[0-9].+[a-z]\s*[a-z]+\s\s[a-z]+ puerto 

        regex = '([BitDefender]{11,11}....+)'

        list_data = []

        for line3 in print_data:
            line3 = line3.rstrip()
            b = re.findall('([BitDefender]{11,11}....+)', line3)
            if len(b) > 0 :
                if b[0] not in list_data:
                    list_data.append(b[0])
                    init()
                    print (Fore.RED +b[0])
        
        print("")

        print_data1 = open('log_scan.txt','r')

        regex = '([McAfee]{6,6}....+)'

        list_data1 = []

        for line4 in print_data1:
            line4 = line4.rstrip()
            c = re.findall('([McAfee]{6,6}....+)', line4)
            if len(c) > 0 :
                if c[0] not in list_data1:
                    list_data1.append(c[0])
                    init()
                    print (Fore.RED +c[0])

        print("")        

        print_data2 = open('log_scan.txt','r')

        regex = '([Symantec]{8,8}....+)'

        list_data2 = []

        for line5 in print_data2:
            line5 = line5.rstrip()
            k = re.findall('([Symantec]{8,8}....+)', line5)
            if len(k) > 0 :
                if k[0] not in list_data2:
                    list_data2.append(k[0])
                    init()
                    print (Fore.RED +k[0])

        print("")

        print_data3 = open('log_scan.txt','r')

        regex = '([Kaspersky]{8,8}....+)'

        list_data3 = []

        for line6 in print_data3:
            line6 = line6.rstrip()
            f = re.findall('([Kaspersky]{8,8}....+)', line6)
            if len(f) > 0 :
                if f[0] not in list_data3:
                    list_data3.append(f[0])
                    init()
                    print (Fore.RED +f[0])

        print("")

        print_data4 = open('log_scan.txt','r')

        regex = '([TrendMicro]{10,10}....+)'

        list_data4 = []

        for line7 in print_data4:
            line7 = line7.rstrip()
            g = re.findall('([TrendMicro]{10,10}....+)', line7)
            if len(g) > 0 :
                if g[0] not in list_data4:
                    list_data4.append(g[0])
                    init()
                    print (Fore.RED +g[0])

        print("")  

        print_data5 = open('log_scan.txt','r')

        regex = '([Microsoft]{9,9}....+)'

        list_data5 = []

        for line8 in print_data5:
            line8 = line8.rstrip()
            h = re.findall('([Microsoft]{9,9}....+)', line8)
            if len(h) > 0 :
                if h[0] not in list_data5:
                    list_data5.append(h[0])
                    init()
                    print (Fore.RED +h[0])

        print("")

        print_data6 = open('log_scan.txt','r')

        regex = '([Fortinet]{8,8}....+)'

        list_data6 = []

        for line9 in print_data6:
            line9 = line9.rstrip()
            j = re.findall('([Fortinet]{8,8}....+)', line9)
            if len(j) > 0 :
                if j[0] not in list_data6:
                    list_data6.append(j[0])
                    init()
                    print (Fore.RED +j[0])



        init()
        print (Fore.WHITE +"________________________________________________________________________\n")
        time.sleep(3)
        print ("")



    elif opcion == 3:

        ############################################################################################################
        
        print ("")
        init()  
        print(Fore.RED + "[*]"+Fore.WHITE+"    Hello and welcome to " +Fore.GREEN+ "Software_analizer (**)\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   With this script you can optimize your time, do a quick analysis before analyzing ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   with other tools that may take a little  more time to give you a result. ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   This tool will show a series of results such as metadata, hash and malware analysis")
        init()
        print(Fore.RED + "[!]"+Fore.WHITE+"    This script makes use of and depends on the following tools for its operation " +Fore.GREEN+ ":\n")
        init()
        print(Fore.CYAN + "[1]"+Fore.WHITE+"       Md5sum V 8.28")
        init()
        print(Fore.CYAN + "[2]"+Fore.WHITE+"       Automater ")
        init()
        print(Fore.CYAN + "[3]"+Fore.WHITE+"       Exiftool V 10.80\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   In the same way, Software_analizer.py makes use of regular expressions to filter the ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   data that we need,use of the libraries (os, time, re, time, color, tqdm and sleep)\n")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   It is important to keep in mind that if you are going to use Kali linux you  ")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   should only install the tqdm librarybut if you are going to use Windows you")
        init()
        print(Fore.CYAN + "[+]"+Fore.WHITE+"   must install all the libraries with the option pip install \n\n")

        ########################################################################################
    

    elif opcion == 4:
        salir = True
    else:
        print ("Enter a number between 1 and 5")
print ("") 
print ("********Finished script***********")
print ("")

#comandos error

"""ping 
 apt-cache show nmap
 apt-cache search nmap
 sudo apt-get install python-nmap
 sudo apt-get install python3-nmap

"""

#paginas de consulta
#https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/
#http://www.poketcode.com/es/python/archivos_csv/index.html
#http://python-para-impacientes.blogspot.com/2014/02/ejecutar-un-comando-externo.html




#######################################################################################
# Fuentes
# https://www.solvetic.com/tutoriales/article/3871-como-guardar-resultado-comando-en-archivo-texto-linux/
# https://caminosdigitales.es/ejecutar-systeminfo-y-guardar-en-archivo-con-python/
# https://lapertenencia.wordpress.com/2014/08/16/python-guardando-resultado-comandos-linux-en-una-variable/