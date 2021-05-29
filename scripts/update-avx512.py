#!/bin/python3

from lxml import etree
from pprint import pprint
from glob import glob
import os, sys, re, pprint
from functools import cmp_to_key

pp = pprint.PrettyPrinter(indent=4)

special_cases = [
    {
        "name": "zext",
        "pattern": re.compile('^zext')
    },
    {
        "name": "cast",
        "pattern": re.compile('^cast(ps|pd|si)(128|256|512)$')
    },
    {
        "name": "cvt_round",
        "pattern": re.compile('^cvt_round')
    },
    {
        "name": "cvt",
        "pattern": re.compile('^cvt(ps|pd|epi|epu)(8|16|32|64)?$')
    },
    {
        "name": "cvti",
        "pattern": re.compile('^cvti(8|16|32|64)?$')
    },
    {
        "name": "cvt_storeu",
        "pattern": re.compile('^cvtepi(8|16|32|64)_storeu$')
    },
    {
        "name": "cvts",
        "pattern": re.compile('^cvtsepi')
    },
    {
        "name": "cvtt",
        "pattern": re.compile('^cvtt(pd|ph|ps|sd|ss)$')
    },
    {
        "name": "cvtt_round",
        "pattern": re.compile('^cvtt_round(pd|ph|ps|sd|ss)$')
    },
    {
        "name": "cvtus",
        "pattern": re.compile('^cvtusepi(8|16|32|64)$')
    },
    {
        "name": "cvtus_storeu",
        "pattern": re.compile('^cvtusepi(8|16|32|64)_storeu$')
    },
    {
        "name": "extract",
        "pattern": re.compile('^extract(i|f)(32x4|32x8|64x2|64x4)')
    }
]

files = {}
for file in glob(os.path.join(sys.argv[1], 'simde/x86/avx512/*.h')):
    files[os.path.splitext(os.path.basename(file))[0]] = open(file).read()

iig = etree.parse(sys.argv[2]);

cpuids = sorted(set(iig.xpath('//intrinsics_list/intrinsic[@tech="AVX-512"]/CPUID/text()')))
families = {}
techs = {}
functions = []

func_name_re = re.compile('^_mm(256|512)?_(?:(mask[z23]?)_)?([a-zA-Z0-9_]+?)_([a-zA-Z0-9]+?)(_mask)?$')

for function in iig.xpath('//intrinsics_list/intrinsic[@tech="AVX-512"]'):
    funcData = {
        "name": function.xpath('@name')[0].strip(),
        "implemented": False,
        "techs": function.xpath('CPUID/text()'),
        "family": "Unknown",
    }

    nameMatch = func_name_re.match(funcData["name"])
    if nameMatch != None:
        funcData["width"] = nameMatch.group(1)
        if funcData["width"] == None:
            funcData["width"] = "128"
        funcData["mask"] = nameMatch.group(2)
        if funcData["mask"] == None:
            funcData["mask"] = ""
        funcData["family"] = nameMatch.group(3)
        funcData["type"] = nameMatch.group(4)

        for special_case in special_cases:
            m = special_case["pattern"].match(funcData["family"])
            if m != None:
                funcData["family"] = special_case["name"]

    if (funcData["family"]) in files:
        if files[funcData["family"]].find("simde" + funcData["name"]) >= 0:
            funcData["implemented"] = funcData["family"]
    if funcData["implemented"] == False:
        for header in files.keys():
            if files[header].find("simde" + funcData["name"]) >= 0:
                funcData["implemented"] = header
                break

    if not funcData["family"] in families:
        families[funcData["family"]] = []

    for tech in funcData["techs"]:
        if not tech in techs:
            techs[tech] = { "implemented": 0, "total": 0 }

        techs[tech]["total"] += 1
        if funcData["implemented"]:
            techs[tech]["implemented"] += 1

    families[funcData["family"]].append(funcData)
    functions.append(funcData)

families = dict(sorted(families.items(), key=lambda item: item[0]))

# pp.pprint(families)
# pp.pprint(techs)

print("# Summary\n")

total_functions_implemented = 0
total_functions = 0
for func in functions:
    total_functions += 1
    if func["implemented"]:
        total_functions_implemented += 1

print("Of the %d functions currently in AVX-512, SIMDe implements %d (%.2f%%):\n" % (total_functions, total_functions_implemented, ((float(total_functions_implemented) / float(total_functions)) * 100.0)))

print("|      Technology     | Implemented | Total | Percent Complete |")
print("| ------------------- | ----------- | ----- | ---------------- |")
for tech in techs.keys():
    print('| %19s' % tech, end=' |')
    print(' %11d' % techs[tech]["implemented"], end=' |')
    print(' %5d' % techs[tech]["total"], end=' |')

    progress = (float(techs[tech]["implemented"]) / float(techs[tech]["total"])) * 100.0
    print(' %15.2f%% |' % progress)

print('\nNote that some functions require multiple AVX-512 extension (*e.g.*, AVX512F and AVX512VL.')

print('\n# Families\n')

def family_cmp(a, b):
    if ("width" in a) and ("width" in b):
        if a["width"] != b["width"]:
            return int(a["width"]) - int(b["width"])

    if ("type" in a) and ("type" in b):
        if a["type"] != b["type"]:
            return a["type"] < b["type"]

    if ("mask" in a) and ("mask" in b):
        return len(a["mask"]) - len(b["mask"])

    return 0
family_cmp_key = cmp_to_key(family_cmp)

for family_name in families.keys():
    print('## ' + family_name + '\n')

    family = families[family_name]

    family_implemented = 0
    family_total = 0
    for func in family:
        family_total += 1
        if func["implemented"]:
            family_implemented += 1

    print("%d of %d (%.2f%%) implmented.\n" % (family_implemented, family_total, ((float(family_implemented) / float(family_total)) * 100.0)))

    family.sort(key=family_cmp_key)

    for func in family:
        is_implemented = ' '
        if func["implemented"] != False:
            is_implemented = 'x'
        print(" * [%c] [%s](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=%s&techs=AVX_512)" % (is_implemented, func["name"], func["name"]), end='')
        if func["implemented"] != False:
            if func["implemented"] != func["family"]:
                print(' (in %s.h)' % func["implemented"])
            else:
                print('')
        else:
            print('')

    print('')
