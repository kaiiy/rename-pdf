# rename-pdf

Rename PDF files with underscores instead of special characters.

## Installation

```sh 
$ rye install pypdf
$ wget https://raw.githubusercontent.com/kaiiy/rename-pdf/main/bin/rename-pdf -O ~/.local/bin/rename-pdf
$ chmod u+x ~/.local/bin/rename-pdf
```

## Usage

```sh
$ rename-pdf --help
usage: rename-pdf [-h] path

Rename PDF files with underscores instead of special characters.

positional arguments:
  path        path to the PDF file or directory

options:
  -h, --help  show this help message and exit
```

## Deployment

```sh
$ cp ./src/main.py ./bin/rename-pdf
```
