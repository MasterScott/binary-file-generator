# Binary File Generator

Random binary file generator, inspired while creating forensic CTF challenges to obtain more obfuscation on folder contents while listing files.

## Usage
```
./generator.py [-h] [-n N] [-x X] [-f F]

optional arguments:
  -h, --help  show this help message and exit
  -n N        define number of files
  -x X        define max hex for single file
  -f F        define number of folders
```

## Default Values
* `-n` : 10
* `-x` : 100
* `-x` : `None`

## Example
Creating 100 files in current dir
```
./generator.py -n 100
```

Creating 100 files in current dir with max 500 byte for single file
```
./generator.py -n 100 -x 500
```

Creating 10 folders containing 1000 files
```
./generator.py -n 1000 -f 10
```

## Result
This is result example of a single random binary file hex values

```
0x00000000  ced4 700c 2ae1 056d 6e6a 31fe 0482 e0e8
0x00000010  f260 bced abea 6c59 aee4 3231 b476 7497
0x00000020  9626 eee0 3744 5ca0 b570 253f 6adc c206
0x00000030  ff79 153c 8d68 f384 6b4c 1172 3eda 5d3a
0x00000040  5bdd 9346 c0fc d40a 2824 1785 5364 bc91
0x00000050  e542 a042 7417 d0f4 703d b3e2 0428 a3ff
```