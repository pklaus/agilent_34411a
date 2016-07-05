
### Agilent 34411A Python Package

This Python package makes it easy to communicate with the Agilent 34411A in Python.

#### Installation

    pip install https://github.com/pklaus/agilent_34411A/archive/master.zip

#### Usage

I use the small CLI script thats being supplied with the package like this:

    agilent_34411a_cli 192.168.0.10 --interval 3 --avg-samples 1

I also added some more transformation functions:

````bash
agilent_34411a_cli 192.168.0.10 \
--apply-function PT100 \
--output-format '{:.03f} °C' \
--interval 0.9 --avg-samples 1
````

Check what's possible by running `agilent_34411a_cli --help`.

You can, however, also write your own Python script to implement your own measurement tasks:

````python
from agilent_34411A import Agilent_34411A

a = Agilent_34411A('192.168.0.10')
print("Connected to the following device: {}".format(a.idn))

while True:
    value = a.read()
    print("{}".format(value))
````
