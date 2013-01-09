# -*- coding: cp1252 -*-
import sys
from xml.sax import ContentHandler
from xml.sax import make_parser
import eyeD3   

reload(sys)
sys.setdefaultencoding("cp1252")

class MuestraBpmManejador(ContentHandler):
    #Se llama al empezar a parsear
    def __init__(self):
        self.cant = 100000
        self.indice = -1
        self.titulo = ""
        self.bpmVdj = "0"
        self.bpmTag = "0"
        self.esMp3 = 0
 
    #Se llama al encontrar una etiqueta de inicio de elemento <elemento>
    def startElement(self, name, attrs):
        #Entramos en Song
        if name == 'Song' and self.indice < self.cant:
            #Se guarda variable sobre si song es mp3
            self.esMp3 = attrs.get('FilePath').count("mp3")
            #Se guarda variable con ruta del mp3
            self.titulo = attrs.get('FilePath')
            print "\n" + self.titulo.encode("cp1252")
        #Entramos en BPM de Song, solo si el indice es menor que la cantidad predefinida y si es mp3
        if name == 'BPM' and self.indice < self.cant and self.esMp3 > 0:
            #El indice aumenta
            self.indice =  self.indice + 1
            if attrs.get('Bpm'):
                #Se guarda el bpm de VDJ solo si ya existia
                self.bpmVdj = "{0:.4f}".format(round(44100 / float(attrs.get('Bpm')) * 60, 4))
                                    
    def endElement(self, name):
        #Salimos del elemento song
        try:
            if name == 'Song' and self.indice < self.cant and self.esMp3 > 0:
                
                print "BPM VDJ " + (self.bpmVdj).rjust(17)
                #a leer el tag
                if tag.link(self.titulo):
                    #guarda en var tagbpm del mp3 PARA MOSTRAR solo si este tiene tagbpm
                    if tag.getBPM():
                        self.bpmTag = "{0:.4f}".format(tag.getBPM())
                        print "BPM TAG ORIGINAL " + (self.bpmTag).rjust(8)
                    else:
                        print "ARCHIVO SIN BPM TAG PERO CON ID3TAG"
                else:
                    print "NO ID3TAG, CREANDO"
                    #creamos el tag
                    tag.header.setVersion(eyeD3.ID3_V2_3)


                #setear tag bpm en tagid3,
                if self.bpmVdj != "0":
                #si no hay bpmVdj = (0), no se realiza nada
                    if tag.getBPM() == 0.0 or not tag.getBPM():
                        #si no tiene un bpmtag previo, se guarda desde bpmVdj o si tag.getBPM es null
                        tag.setBPM(self.bpmVdj)
                        #se guarda lo cambiado
                        tag.update()
                        print "GUARDADO DESDE BPMVDJ AL NO HABER PREVIO EN TAG"
                        print "BPM OK: " + "{0:.4f}".format(tag.getBPM()).rjust(17)
                    else:
                        #si ya tiene un bpmtag previo, se compara con el de bpmVdj, si son iguales no se realiza nada, distintos, se guarda el de VDJ
                        if tag.getBPM() != float(self.bpmVdj):
                            tag.setBPM(self.bpmVdj)
                            #se guarda lo cambiado
                            tag.update()
                            print "GUARDADO DESDE BPMVDJ AL SER DISTINTO A TAG"
                            print "BPM OK: " + "{0:.4f}".format(tag.getBPM()).rjust(17)
                else:
                    print "NO HAY BPMVDJ, NO SE GUARDA NADA"
                        
                #limpiar variables
                self.titulo = ""
                self.bpmVdj = "0"
                self.bpmTag = 0
                self.esMp3 = 0
        except Exception, e:
            print "ERROR " + str(e)
            raise e

parser = make_parser()
handler=MuestraBpmManejador()
parser.setContentHandler(handler)
tag = eyeD3.Tag()
#Parseamos el fichero
parser.parse("D:\VirtualDJ Local Database v6.xml")
