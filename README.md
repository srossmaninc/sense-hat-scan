# sense-hat-scan
This is a small utility that utilizes the ping command and python in combination with the RPI Sense Hat to display hosts connected to a network and whether they are alive or not.

The program initially scans the full subnet the Raspberry Pi is connected to using the os library and ping commands. After caching the living host's IP addresses into a list and displaying the information (1 green LED per alive host), the program then continually checks the list of alive hosts every X amount of seconds. If an IP address is unreachable by ping, the respective LED turns red to reflect that the host is dead. The reasoning behind not continually scanning the entire network for hosts each time is the immense amount of time needed by the Raspberry Pi to ping each and every single host.

# next steps
My next step with this program is to potentially utilize multi-threading or another avenue to update the initial host list after a different set Y time.
Antoher possible next step is to increase the amount of RPIs to 4 as each sense hat is capable of displaying only 64 hosts (or pixels) at a time. This will give us 256 LEDs which is perfect as each octet in the IP address can only range from 0-255.
