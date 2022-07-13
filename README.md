# sense-hat-scan
This is a small utility that utilizes the ping command and python in combination with the RPI Sense Hat to display hosts connected to a network and whether they are alive or not.

The program initially scans the full subnet the Raspberry Pi is connected to using the os library and ping commands. After caching the living hosts IP addresses into a list and displaying the information (1 green LED per alive host), the program then continually checks the list of alive hosts every X amount of seconds. If an IP address is unreachable by ping, the respective LED turns red to show that the host is dead. The reasoning behind not continually scanning the whole network for hosts each time is the immense amount of time needed by the Raspberry Pi to ping each and every single host.

# next steps
My next step with this program is to potentially utilize multi-threading or another avenue to update the initial host list after a different set Y time.
