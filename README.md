
### Agilent 34411A Python Package

This Python package makes it easy to communicate with the Agilent 34411A in Python.

#### Installation

    pip install https://github.com/pklaus/agilent_34411A/archive/master.zip

#### Usage

I use the small CLI script thats being supplied with the package like this:

    agilent_34411a_cli 192.168.0.10 --interval 3 --avg-samples 1

I also added some more transformation functions:

    agilent_34411a_cli 192.168.0.10 \
    --apply-function PT100 \
    --output-format '{:.03f} °C' \
    --interval 0.9 --avg-samples 1

Check what's possible by running `agilent_34411a_cli --help`.

You can, however, also write your own Python script to implement your own measurement tasks:

```python
from agilent_34411a import Agilent_34411A

a = Agilent_34411A('192.168.0.10')
print("Connected to the following device: {}".format(a.idn))

while True:
    value = a.read()
    print("{}".format(value))
```

#### Resources

##### Connecting via VXI-11

Besides connecting directly to port 5025 via TCP/IP, the
DMM also understands the RPC protocol VXI-11.

To make this work, you don't need this package (*agilent_34411A*).
Instead, install the Python bindings for VXI-11:
[python-vxi11](https://github.com/python-ivi/python-vxi11)
and you can connect to the device with the following Python code:

```python
import vxi11

instr =  vxi11.Instrument("192.168.0.207")

print(instr.ask("*IDN?"))
print("{:.05f}".format(float(instr.ask("READ?"))))
```
