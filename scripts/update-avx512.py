#!/bin/python3

from lxml import etree
from pprint import pprint
from glob import glob
import os, sys

exception_list = ["broadcast", "cast", "compress", "cvt", "expand", "extract", "gather", "scatter", "insert", "load", "madd", "mov", "rcp", "rsqrt", "sll", "sra", "srl", "shr", "shl", "store", "zext", "set", "rol", "ror", "k", "4", "dpwssd", "sad", "dpb"]

def group_extra(family):
    for key in exception_list:
        if key != "gather" and key != "k" and key!= "4":
            if family.find(key)>-1:
                family = key
        elif key == "gather":
            if family.find("gather")>-1:
                family = family[family.find(key):]
        elif key == "k":
            if family[0:1].find("k")>-1:
                family = "kbits"
        else:
            if family[0:1].find("4")>-1:
                family = family[1:]
    return family

functions = {}
tot = 0
files = []
for file in glob(os.path.join(sys.argv[1], 'simde/x86/avx512/*.h')):
    files.append(open(file).read())

all_functions = open(sys.argv[2]).read().split('\n')

families = {}
for function in all_functions:
    funcData = {
        "name": function,
        "implemented": False
    }

    for header in files:
        if header.find(funcData["name"]) >= 0:
            funcData["implemented"] = True
    family = ""
    if funcData["name"].find("_mm") > -1 :
        family = funcData["name"].split('_', 2)[2]
    else:
        family = funcData["name"].split('_', 1)[1]

    if family[0:5].find("mask") > -1:
        if len(family.split("_",1))>1:
            family = family.split("_", 1)[1]

    if family[0:9].find("prefetch") > -1:
        if len(family.split("_",1))>1:
            family = family.split("_", 1)[1]

    family = family.split("_")[0]
    family = group_extra(family)

    if family in families:
        families[family].append(funcData)
    else:
        families[family] = [funcData]

# f = open("../avx512.md", 'w')

for i in families:
    implemented = 0
    for j in families[i]:
        if j["implemented"] == True:
            tot+=1
            implemented +=1
    if implemented!= len(families[i]):
        print(' - [ ] ['+str(i)+']',end = "")
    else:
        print(' - [x] ['+str(i)+']',end = "")
    if i != "kbits":
        print("(https://software.intel.com/sites/landingpage/IntrinsicsGuide/#techs=AVX_512&expand=2306,2439&text="+str(i)+')')
    else:
        print("(https://software.intel.com/sites/landingpage/IntrinsicsGuide/#techs=AVX_512&expand=2306,2439&text=_k)")
    print("Implemented: " + str(implemented) + " out of " + str(len(families[i])) + " (" + str("{:.2f}".format(100*implemented/(len(families[i]))))+ "%)")
    if implemented!=len(families[i]):
        for j in families[i]:
            print("   - [", end = "")
            if j["implemented"]:
                print("x] ", end = "")
            else:
                print(" ] ", end = "")
            print(j["name"])
    print("")
