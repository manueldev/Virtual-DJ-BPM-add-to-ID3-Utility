Virtual-DJ-BPM-add-to-ID3-Utility
=================================

Script Python que extrae los BPM de las canciones en la base de datos de Virtual DJ, guardándolos en el campo BPM de Id3tag del archivo MP3.

## Uso:

'python main.py --database x://VirtualDJ Local Database v6.xml -s 100-t 10 -p'

    --database -d:  Especifica la ruta al XMl con la base de datos de VirtualDJ
    --start -s:     [>0] El track desde el cual se comienza a analizar
    --tracks -t:    [>0] Cantidad de tracks a analizar
    --partyMode -p:	Activa el modo debug