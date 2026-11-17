Structure:
Récupération de l'audio grâce au microphone
Lecture de l'audio dans server/audio/capture.py
Calculs dans server/audio/analyse.py
Résultats traités puis envoyés sous forme de JSON au FastAPI par websocket
On produit l'image puis la renvoie par websocket au browser