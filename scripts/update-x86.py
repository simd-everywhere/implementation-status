#!/bin/python3

from lxml import etree
from pprint import pprint
from glob import glob
import os, sys

functions = {}

files = []
for file in glob(os.path.join(sys.argv[1], 'simde/x86/*.h')):
    files.append(open(file).read())
for file in glob(os.path.join(sys.argv[1], 'simde/x86/avx512/*.h')):
    files.append(open(file).read())

all_functions = etree.parse(sys.argv[2]).xpath('//intrinsics_list/intrinsic[starts-with(@name,"_mm")]')
all_functions_implemented = 0

for function in all_functions:
    funcData = {
        "name": function.xpath('@name')[0],
        "implemented": False
    }

    for header in files:
        # print([funcData["name"], header.find(funcData["name"])])
        if header.find(funcData["name"]) >= 0:
            funcData["implemented"] = True

    for cpuid in function.xpath('CPUID/text()'):
        if cpuid not in functions:
            functions[cpuid] = []

        functions[cpuid].append(funcData)

        break

for cpuid in functions.keys():
    num_functions = 0
    implemented = 0

    for func in functions[cpuid]:
        num_functions = num_functions + 1
        if func["implemented"]:
            implemented = implemented + 1
            all_functions_implemented = all_functions_implemented + 1

    percent_implemented = (float(implemented) / float(num_functions)) * 100.0

    print("## " + cpuid + "\n")

    print("Implemented: %d of %d (%.2f%%)\n" % (implemented, num_functions, percent_implemented))

    for func in functions[cpuid]:
        if func["implemented"]:
            print(" * [x] " + func["name"])
        else:
            print(" * [ ] " + func["name"])
    print("")

print("# Summary\n")

# (float(len(all_functions)) / float(all_functions_implemented)) * 100.0
print("There are a total of %d SIMD functions on x86, %d (%.2f%%) of which have been implemented in SIMDe so far." % (len(all_functions), all_functions_implemented, (float(all_functions_implemented) / float(len(all_functions))) * 100.0))