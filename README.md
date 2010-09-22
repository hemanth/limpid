## About Limpid
Limpid is a simple gtk application coded in python, as there was a requirment for the course named [Scripting-101](http://p2pu.org/webcraft/scripting-101) which i'm mentoring on Mozilla P2PU.
The app has a window with a split screen, where in the first part of the split is a simple webbased IRC and the other part is a virtual GNU/Linux terminal.

#Advantages :
0. As the course includes loads of coding, it would be very easy to follow the chat and typing in the code and errors as the apper.
1. Easier than switching between and webbased irc and a terminal.
2. As its a client side app, its highly reconfigurable, to meet the requirments, unlike running a evalbot.

## Preparing your system

# List of dependencies :

1. python-gtk
2. vte 
3. webkit

Get the dependencies if on a Debian based system by typing the below, or else get the source and compile :
		sudo apt-get install python-gtk python-vte python-webkit


## After the above, you may run the code by :
		git clone git://github.com/hemanth/limpid.git
		cd limpid
		python limpid.py 
