import sys
from xml.sax import ContentHandler
from xml.sax import make_parser
import eyeD3   
import getopt

reload(sys)

class MuestraBpmManejador(ContentHandler):
    #Se llama al empezar a parsear
    def __init__(self):
        self.indice = 0
        self.titulo = ""
        self.bpmVdj = "0"
        self.bpmTag = "0"
        self.esMp3 = 0
        self.contadorErrorGeneral = 0
        self.errno2Archivos = 0
        self.errno13Archivos = 0
        self.start = 0
        self.tracks = 0
 
    #Se llama al encontrar una etiqueta de inicio de elemento <elemento>
    def startElement(self, name, attrs):
            #Entramos en Song
            if name == 'Song' and self.indice < self.tracks:
                #Se guarda variable sobre si song es mp3
                self.esMp3 = attrs.get('FilePath').count("mp3")
                #Se guarda variable con ruta del mp3
                self.titulo = attrs.get('FilePath')
                print "\n" + self.titulo.encode('cp850','replace')
            #Entramos en BPM de Song, solo si el indice es menor que la cantidad predefinida y si es mp3
            if name == 'BPM' and self.indice < self.tracks and self.esMp3 > 0:
                if attrs.get('Bpm'):
                    #Se guarda el bpm de VDJ solo si ya existia
                    self.bpmVdj = "{0:.4f}".format(round(44100 / float(attrs.get('Bpm')) * 60, 4))
                                        
    def endElement(self, name):
        #Salimos del elemento song
        try:
            if name == 'Song' and self.indice < self.tracks and self.esMp3 > 0:
                
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
                #El indice aumenta
                self.indice += 1
                        
                #limpiar variables
                self.titulo = ""
                self.bpmVdj = "0"
                self.bpmTag = 0
                self.esMp3 = 0
        except IOError, e:
            if e.errno == 2:
                print "ERROR: El archivo no se encuentra en la ruta:\n" + self.titulo.encode('cp850','replace')
            elif e.errno == 13:
                print "ERROR: Se denegaron permisos para escribir en el archivo:\n" + self.titulo.encode('cp850','replace')
            else:
                raise e
        except Exception, e:
            print "ERROR " + str(e)
            raise e
    def setInicio(self,nStart):
        self.start = nStart
    def setTracks(self,nTracks):
        self.tracks = nTracks

def usage():
    print "Uso:\n--database: Especifica la ruta al XMl con la base de datos de VirtualDJ\n--start: El track desde el cual se comienza a analizar\n--tracks: Cantidad de tracks a analizar"

def main(argv):
    try:
        db = ''
        start = 1
        tracks = 1000

        opts, args = getopt.getopt(argv, "d:s:t:", ["database=", "start=", "tracks="])
        
        if len(opts) == 0:
            raise Exception("No se han ingresado argumentos validos")

        for opt, arg in opts:
            if opt in ("-d", "--database"):
                db = arg
            elif opt in ("-s", "--start"):
                start = int(arg)
            elif opt in ("-t", "--tracks"):
                tracks = int(arg)
        print "Analizando base de datos ubicada en: " + db
        print "Desde el track numero: " + str(start)
        print "Tracks a analizar: " + str(tracks)

        parser = make_parser()
        handler = MuestraBpmManejador()
        handler.setInicio(start)
        handler.setTracks(tracks)
        parser.setContentHandler(handler)
        
        #Parseamos el fichero
        parser.parse(db)

    except getopt.GetoptError:
        print "Error: No se han ingresado argumentos validos\n"
        usage()
    except ValueError:
        print "Error: No se han ingresado argumentos validos\n"
        usage()
    except Exception, e:
        print "Error: " + e.args[0] + "\n"
        usage()

tag = eyeD3.Tag()
if __name__ == "__main__":
    main(sys.argv[1:])