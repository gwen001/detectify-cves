<h1 align="center">detectify-cves</h1>

<h4 align="center">Find CVEs that don't have a Detectify modules.</h4>

<p align="center">
    <img src="https://img.shields.io/badge/python-v3-blue" alt="python badge">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT license badge">
    <a href="https://twitter.com/intent/tweet?text=https%3a%2f%2fgithub.com%2fgwen001%2fcsp-analyzer%2f" target="_blank"><img src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fgwen001%2Fcsp-analyzer" alt="twitter badge"></a>
</p>

<!-- <p align="center">
    <img src="https://img.shields.io/github/stars/gwen001/csp-analyzer?style=social" alt="github stars badge">
    <img src="https://img.shields.io/github/watchers/gwen001/csp-analyzer?style=social" alt="github watchers badge">
    <img src="https://img.shields.io/github/forks/gwen001/csp-analyzer?style=social" alt="github forks badge">
</p> -->

---

## Description

The script compares the official public list of CVEs from [cve.mitre.org](https://cve.mitre.org/) and the list of [Detectify](https://detectify.com/) modules to find CVEs that don't have a modules yet.

## Install

```
git clone https://github.com/gwen001/detectify-cves
cd detectify-cves
pip3 install -r requirements.txt
```

## Requirements

1/ One cloned, go to the script directory:
```
cd detectify-cves
```

2/ Get CVE list:
````
wget https://cve.mitre.org/data/downloads/allitems.csv
````

3/ Get Detectify modules list (you need a crowdsourced Detectify account):  
  - login on Detectify: https://cs.detectify.com/login  
  - Check `Scanner modules` on the left menu: https://cs.detectify.com/dashboard/modules
  - Check the background requests performed by your browser, find `https://fedeo.cs.detectify.com/graphql` with huge JSON response ~1.5Mo.
  - Save the output (without HTTP headers) on the script directory as `detectify-modules.json`

## Usage

```
$ python3 detectify-cves.py -s wordpress
```

```
usage: detectify-cves.py [-h] [-s SEARCH] [-l LIMIT] [-d DETECTIFY]

options:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        search a specific keyword
  -l LIMIT, --limit LIMIT
                        display only n first results
  -d DETECTIFY, --detectify DETECTIFY
                        related to Detectify modules: 0:no module available, 1:module available (default), -1:doesn't matter
```

---

<img src="https://raw.githubusercontent.com/gwen001/detectify-cves/main/preview.png" />

---

Feel free to [open an issue](/../../issues/) if you have any problem with the script.  

