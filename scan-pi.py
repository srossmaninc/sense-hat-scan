from sense_emu import SenseHat
import time
import os

sense = SenseHat()

network_id = "10.0.2."
hosts_alive = []
hosts_down = []

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

def init_scan():
    for i in range(0, 256):
        response = os.system("ping -c 1 -a " + network_id + str(i))
        
        if response == 0:
            #print(network_id + str(i) + " is UP currently")
            hosts_alive.append(network_id + str(i))
        #else:
            #print(network_id + str(i) + " is DOWN currently")
    
    print("Finished intitial scan and found " + str(len(hosts_alive)) + " alive hosts")
                
def scan():
    hosts_down.clear()
    
    for k in hosts_alive:
        response = os.system("ping -c 1 -a " + k)
        
        if response == 0:
            print(k + " is still up")
        else:
            print(k + " is down")
            hosts_down.append(k)
    print("Scan finished")


init_scan()

while (True):
    x = 0
    y = 0
    for k in hosts_alive:
        if k in hosts_down:
            sense.set_pixel(x, y, r)
        else:
            sense.set_pixel(x, y, g)
        
        x += 1
        if (x >= 8):
            x = 0
            y += 1
    
    # Scan to see if pre-existing hosts are alive
    print("Scanning")
    scan()
    
    # Delay may be unneeded since program should wait until scan completes
    # ^^^ we now use the delay to display the whole screen as blue temporarily before blank
    sense.clear(b)
    time.sleep(5)
    sense.clear()