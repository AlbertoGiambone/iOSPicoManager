from machine import Pin

import time

#dichiaro il pin a cui voglio accedere
GP0 = Pin(0, Pin.IN)


while True:
    try:
        #do 3.3v a GP0
        GP0.value(1)
       
    except KeyboardInterrupt:
        break

print("Finished.")
