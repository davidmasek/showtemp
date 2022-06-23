# showtemp

Simple utility for displaying current CPU temperature.

## Requirements

Tested on Ubuntu 20.04 with Python 3.9. Depedends on `psutil` package. I expect this to work on most recent mainstream linux systems.

## Installation

```bash
# clone directory and run this inside 
python setup.py install
```

## Usage

```bash
$ showtemp
Core 0: 64°C
Core 1: 63°C
Core 2: 70°C
Core 3: 65°C
```

Your output may vary.

## Command line options

See `command_line.py` for details. Note `--list_all`.
