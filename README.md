
### Agilent 34411A Python Package

This Python package makes it easy to communicate with the Agilent 34411A in Python.

#### Installation

    pip install https://github.com/pklaus/agilent_34411A/archive/master.zip

#### Usage

I use it like this:

    agilent_34411a_cli 192.168.0.10 --apply-function PT100 --output-format '{:.03f} °C' --interval 0.9 --avg-samples 1

