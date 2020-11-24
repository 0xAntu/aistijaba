Aistijaba
=========

Fast HTTP Response status checker

Note: All URLs must have SSL (HTTP / HTTPS) attached.

# Requirement

==> Python3

Installation & Usage
------------

First go your Terminal. Then

Step 1 # git clone https://github.com/0xAntu/aistijaba.git

Step 2 # cd aistijaba

Step 3 # pip3 install -r requirements.txt

Step 4 # python3 aistijaba.py -h

# Now you can see such pages

```
        __         __
  _____|  |    _  |  |  _     _
 |  _  |  |___| |_|  | |_|___| |_ ___
 |     |__|_ -|  _|__| | | .'| . | .'|
 |__|__|__|___|_| |__|_| |__,|___|__,|
                     |___|

# Develop by ArMan HoSSa!n
# Twitter: https://twitter.com/0xAntu
# Fast HTTP Response status checker

usage: aistijaba.py [-h] [-u URL] [-f URL_FILE] [-o OUTPUT_FILE]

optional arguments:
  -h, --help      show this help message and exit
  -u URL          Target url
  -f URL_FILE     URLs File
  -o OUTPUT_FILE  Save the results to text file
```

Usage:
--------

== For specific domain:

+++] python3 aistijaba.py -u url.com

== For domain list:

+++] python3 aistijaba.py -f urls.txt

== Saving output to a file

+++] python3 aistijaba.py -u url.com -o status.txt

+++] python3 aistijaba.py -f urls.txt -o status.txt


# You can also use bash file

First go your Terminal. Then

Step 1 # git clone https://github.com/0xAntu/aistijaba.git

Step 2 # cd aistijaba

Step 3 # chmod +x aistijaba

Step 4 # cp aistijaba /usr/local/bin

Usage:
--------

== cat urls.txt | aistijaba

++] Saving output to a file

== cat urls.txt | aistijaba | tee status.txt

# Note

You must have python3 installed with pip3 :-)

# Enjoy The SCRIPT :))

If you have find any problem & fix any bug . Please Contact me.

Mail to: armanantu19@gmail.com
