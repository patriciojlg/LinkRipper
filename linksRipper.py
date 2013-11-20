# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:08:15 2013

@author: joaquino
linksRipper  v0.1



Extrae links de descarga de peliculas de distintos sitios... 
y extrae de ésta los nombres de las peliculas y sus link de descargas respectivo. 
En sí está pensado para no ver publicidad - y tener link de descargas de manera rápida.
El proyecto hasta el momento está pensado para trabajar con un solo portal, no obstante, 
más adelante logrará sacar links de descargas de los sitios que acumulan descargas de peliculas más importantes
como peliculasyonkis, ice-films.info, newdivx.com, etc. 

ENJOY!!!
"""

import urllib2
import re


coleccionLink = []
n = 1
url = "http://www.descargarmega.com/?q=peliculas-hdrip"



def ripperLink():
    global n
    global coleccionLink
    global url    
    respuesta = urllib2.urlopen(url)
    html = respuesta.read()
    #<h2 class="title" property="dc:title" datatype=""><a href="/?q=content/looper">Looper</a></h2>
    titulos = re.findall('content/(.*?)">.*</a></h2>',html) 
    
    for links in titulos:
        coleccionLink.append(links)
    
    url = "http://www.descargarmega.com/?q=peliculas-hdrip&page="+str(n)
    print titulos
    
    if (titulos != []):
        n = n+1
        ripperLink()
    else:
        ##DEBUG!
        print "\n\nResumen de la lista"
        print coleccionLink 
        print "\n\n\nFIN DEL BUCLE"
        
def getEnlaces():
    vez = 0
    tamano = len(coleccionLink)
    while vez != tamano:
        urlParaEnlace =  urllib2.urlopen("http://www.descargarmega.com/?q=content/"+coleccionLink[vez])
        htmlParaEnlace = urlParaEnlace.read()      
                                     #<td class="rtecenter"><a href="http://pastebin.com/E4HwxGYH" target="_blank">ESDLA La Comunidad del Anillo (V.E.)</a></td>
        urlParaPastebin = re.findall('<td class="rtecenter"><a href="(.*?)" target="_[b|B]lank">',htmlParaEnlace)
        if (urlParaPastebin == []):
            urlParaPastebin = re.findall('<td class="rtecenter"><a href="(.*?)">.*</a></td>',htmlParaEnlace)
            
        ##DEBUG!
        urlLinkFinal = urllib2.urlopen(urlParaPastebin[0])
        htmlLinkFinal = urlLinkFinal.read()
        #<li class="li1 ln-xtra"><div class="de1">https://mega.co.nz/#!l90XTKRQ!O4KRaVXssRkmZ1gh-0QxzybWcswJvXe4RUq-YrVgXNI</div></li>
        linkFinal = re.findall('<li class="li1 ln-xtra"><div class="de1">(.*?)</div></li>',htmlLinkFinal) 
        print linkFinal
        print coleccionLink[vez]
        linkFinal = []
        vez = vez+1
     
        
            
    

ripperLink()
getEnlaces()
 
   
        
