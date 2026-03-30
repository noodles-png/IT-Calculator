# IT-Calculator
A terminal based calculator written in Python to convert common used Units in the IT world. 
This is a learning project for myself and doesn't use integrated´function like hex() 

## Installation and How to use
```bash
git clone https://github.com/noodles-png/it-rechner.git
cd it-rechner
python main.py
```

No external dependencies required – runs on Python 3.10+.
## Features
- Conversion of different based number to other bases. Decimal, Binary and Hexadecimal
- Conversion of storage sizes
- Calculator for bandwith relevant infos
- Shows subnetting masks of Ipv4

## Upcoming features
- GUI or standalone app 

## Project structure
## Project Structure
```
it-rechner/
├── main.py                  # Entry point, main menu
├── modules/
│   ├── __init__.py
│   ├── helpers.py           # Shared utilities (outro prompt, unit selection)
│   ├── numbers.py           # Number system conversion (bin/oct/dec/hex)
│   ├── storage.py           # Storage unit conversion (SI & binary)
│   ├── network.py           # Bandwidth, transfer time, file size calc
│   ├── config.py            # Planned config module for coloured text
│   └── subnetting.py        # IPv4 subnet calculator
└── README.md
```

## What I learned
- Modular project structure with reusable helper functions (DRY principle)
- Bitwise operations for IP address and subnet calculations
- Number system conversion using positional notation
- Writing clean, PEP8-compliant Python code with docstrings and type hints
- Git workflow with feature-based commits

## License
It is a learning project and falls under the MIT licence