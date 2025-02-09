from machine import Pin, UART
from utime import sleep

# Initialize UART on GPIO0 (TX) and GPIO1 (RX)
uart = UART(1, baudrate=9600, tx=Pin(0), rx=Pin(1))

pin = Pin("LED", Pin.OUT)

GP0 = Pin(0, Pin.IN)



    


print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
