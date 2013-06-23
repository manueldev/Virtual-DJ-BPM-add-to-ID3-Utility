Virtual-DJ-BPM-add-to-ID3-Utility
=================================

Windows ejecutable via consola de comandos y GUI que extrae los BPM de las canciones en la base de datos de Virtual DJ, guardándolos en el campo BPM de Id3tag del archivo MP3.

Windows executable and GUI that extracts the BPM of the songs in the database Virtual DJ, storing them in the BPM field ID3Tag MP3 file.

## Download executables (console & GUI)

2.0.1-nightly https://drive.google.com/folderview?id=0BzknNgENdjp_ZEVNdzZvSlRWWUU&usp=sharing#list

## Uso:

`virtualdjbpmutility-console.exe --database "x://VirtualDJ Local Database v6.xml" -s 100-t 10 -p`

    --database -d:  Especifica la ruta al XMl con la base de datos de VirtualDJ
    --start -s:     [>0] El track desde el cual se comienza a analizar
    --tracks -t:    [>0] Cantidad de tracks a analizar
    --partyMode -p:	Activa el modo debug

## Python script 1.0 Stable

https://github.com/manueldev/Virtual-DJ-BPM-add-to-ID3-Utility/tree/1.0stable