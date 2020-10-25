# metar-tafs-manual.py
# https://paetalung.github.io/cv/

# Send line Section    
from songline import Sendline

token = '' # VTSE-WEATHER

# Insert METARS or TAFs Here
metar = "test na ja"

metar = metar + "\n"

messenger = Sendline(token)
messenger.sendtext(metar)
