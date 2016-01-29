# Skrypt ma na celu inicjować co godzinę start programu java (Temperature.java)
#na Raspberry,  który zbiera i wysyła pomiar temperatury do HCP 

import datetime
import subprocess
now = 0

while 1:
    currentTime = datetime.datetime.now().time() #pobranie aktualnego czasu
    if now == 0:
        now = currentTime.hour  #jeśli czas jest równy zero (uruchomienie skryptu)
                                #to wpisuje aktualna godzine do zmiennej 'now'

# Jesli aktualny czas sie zmienia (nowa pelna godzina), inicjalizowany jest kod
#w terminalu: "java Temperature 1", ktory wysyla jeden rekord do HCP
    if now != currentTime.hour:
        subprocess.call(["java", "Temperature", "1"])
        now = currentTime.hour
