Sends DMX over UDP/IP (i.e. Art-Net), specifically tailored for the OHM-lighting setup where each strip is its own DMX-universe (150 LEDs with 3 channels RGB each = 450 channels).

Is hosted on github, fork it and make pull requests.

Some scripts use a class from patterns.py to generate the patterns, but the simple ones create the patterns in the script itself (e.g. the flags).

Most scripts have some configuration in scriptname_conf.py such as IP-addresses.

A script could call multiple patterns from patterns.py and alternate between them without the disruption one has when aborting a script and starting a new one. When making new patterns, please put them in patterns.py to benefit from this.

Still needs the C-based artpoll/artmonitor to discover devices. https://github.com/ohm2013loc/art

Should have no external requirements to run, all standard Python.
