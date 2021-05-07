# !/bin/python3

from lxml import etree
from pprint import pprint
from glob import glob
import os, sys

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

    if family[0:10].find("broadcast")>-1:
        family = family[0:9]
    if family[0:4].find("cast")>-1:
        family = family[0:4]
    if family[0:8].find("compress")>-1:
        family = family[0:8]
    if family[0:3].find("cvt")>-1:
        family = family[0:3]
    if family[0:6].find("expand")>-1:
        family = family[0:6]
    if family[0:7].find("extract")>-1:
        family = family[0:7]
    if family.find("gather")>-1:
        family = family[family.find("gather"):]
    if family.find("scatter")>-1:
        family = "scatter"
    if family[0:6].find("insert")>-1:
        family = "insert"
    if family[0:4].find("load")>-1:
        family = "load"
    if family[0:4].find("madd")>-1:
        family = "madd"
    if family[0:3].find("mov")>-1:
        family = "mov"
    if family[0:3].find("rcp")>-1:
        family = "rcp"
    if family[0:5].find("rsqrt")>-1:
        family = "rsqrt"
    if family[0:3].find("sll")>-1:
        family = "sll"
    if family[0:3].find("sra")>-1:
        family = "sra"
    if family[0:3].find("srl")>-1:
        family = "srl"
    if family[0:3].find("shr")>-1:
        family = "shr"
    if family[0:3].find("shl")>-1:
        family = "shl"
    if family[0:5].find("store")>-1:
        family = "store"
    if family[0:4].find("zext")>-1:
        family = "zext"
    if family[0:3].find("set")>-1:
        family = "set"
    if family[0:3].find("rol")>-1:
        family = "rol"
    if family[0:3].find("ror")>-1:
        family = "ror"
    if family[0:1].find("k")>-1:
        family = "kbits"
    if family[0:1].find("4")>-1:
        family = family[1:]
    if family[0:6].find("dpwssd")>-1:
        family = "dpwssd"
    if family.find("sad")>-1:
        family = "sad"
    if family[0:3].find("dpb")>-1:
        family = "dpb"
    
    
    
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

