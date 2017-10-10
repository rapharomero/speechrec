Système de Reconnaissance vocale d'appels audio.
================================================
Librairies utilisées:
---------------------

os

collections

contextlib

sys

wave

argparse

webrtcvad

Utilisation :
-------------

Pour lancer le script python depuis le terminal:

Se rendre dans le répertoire contenant les trois fichiers  main.py, speech_rec.py et cutting.py.

Taper en ligne de commande:

python main.py <nom du fichier audio> <nom du fichier texte de sortie>

exemple:

python main.py audio.wav texte.txt

Description:
------------

La reconnaissance vocale utilise toujours la bibliothèque de Google.

Pour rendre la reconnaissance plus efficace nous avons utilisé un système de découpage des fichiers audios se basant sur le moteur de détection d'activité vocale de la plateforme WEBRTC (voir fichier cutting.py).

Par la suite nous effectuons la reconnaissance vocale sur ces parties de fichier puis nous combinons le résultat.
