#!/usr/bin/python3

import sys
import json
import csv
import re
import argparse
from termcolor import colored


parser = argparse.ArgumentParser()
parser.add_argument("-s","--search",help="search a specific keyword")
parser.add_argument("-l","--limit",help="display only n first results")
parser.add_argument("-d","--detectify",help="related to Detectify modules: 0:no module available, 1:module available (default), -1:doesn't matter")
parser.parse_args()
args = parser.parse_args()

if args.search:
    search = args.search
else:
    search = ''

if args.limit:
    limit = int(args.limit)
else:
    limit = 0

if args.detectify and int(args.detectify)>=-1 and int(args.detectify)<=1:
    detectify = int(args.detectify)
else:
    detectify = 1


def search_module( t_modules, cve, search ):
    if search == '' or search.lower() in cve[2].lower():
        for mod in t_modules:
            if cve[0] in mod['moduleName']:
                return [ mod['moduleName'], mod['userName'], mod['dateAdded'] ]
            # if cve[0] in mod['module_name']:
            #     return [ mod['module_name'], mod['user_name'], mod['date_added_string'] ]
        return 1
    return 0


with open('detectify-modules.json',encoding='utf8',errors='ignore') as json_file:
    j_detectify = json.load(json_file)
    t_modules = j_detectify['data']['scannerModules']


with open('allitems.csv',encoding='utf8',errors='ignore') as csv_file:
    i = 0
    csv_reader = csv.reader(csv_file, delimiter=',')
    for cve in reversed(list(csv_reader)):
        if "** RESERVED **" not in cve[2]:
            r = search_module( t_modules, cve, search )
            if r != 0:
                # output = cve[0]+" - "+cve[2][:100].strip()
                # output = "https://cve.mitre.org/cgi-bin/cvename.cgi?name="+cve[0]+" - "+cve[2][:100].strip()
                output = "https://cve.mitre.org/cgi-bin/cvename.cgi?name="+cve[0]+" - "+cve[2][:120].strip()
                if len(cve[2]) > 120:
                    output = output + "..."
                if type(r) is list:
                    output = output + "\n" + colored("   -> %s - %s - %s" % (r[2],r[1],r[0]),"red")
                    # output = output + colored(" -> %s - %s - %s" % (r[1],r[2],r[0][:100]),"red")
                    # output = output + colored(" -> %s - %s - %s" % (r[2],r[1],r[0][:100].strip()),"red")
                output = output + "\n"

                if detectify == 0 and not type(r) is list:
                    i = i + 1
                    sys.stdout.write( output )
                if detectify == 1 and type(r) is list:
                    i = i + 1
                    sys.stdout.write( output )
                elif detectify < 0:
                    i = i + 1
                    sys.stdout.write( output )

            if limit and i >= limit:
                break
