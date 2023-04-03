#!/bin/env python
#Author: Hacker NoDo

import urllib.request
import json
from colorama import init, Fore, Back,Style
print(Fore.GREEN+'''****     **          *******
/**/**   /**         /**////**
/**//**  /**  ****** /**    /**  ******
/** //** /** **////**/**    /** **////**
/**  //**/**/**   /**/**    /**/**   /**
/**   //****/**   /**/**    ** /**   /**
/**    //***//****** /*******  //******
//      ///  //////  ///////    //////
''')


print("Hacker NoDo => canal oficial = https://youtube.com/@hackerNoDo")


ip = str(input("Ingrese ip a geolocalizar: "))
url = "https://ipinfo.io/"+ip+"/json"
abrirURL=urllib.request.urlopen(url)
cargarURL=json.load(abrirURL)

for i in cargarURL:
	print(i + " : " + cargarURL[i])
	
print("Gracias...")