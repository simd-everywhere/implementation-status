#!/bin/python3

import sys, os, glob, re, pprint

pp = pprint.PrettyPrinter(indent=2)

families = {}
summary = {
  'functions': 0,
  'implemented': 0,
}

func_parser = re.compile(r'^((__msa_)(.+?)(_([us]))?(_([bhwd]))?)$')

files = {}
for file in glob.glob(os.path.join(sys.argv[1], 'simde/mips/msa/*.h')):
    files[os.path.splitext(os.path.basename(file))[0]] = open(file).read()

with open(sys.argv[2]) as fp:
  for line in fp.readlines():
    m = func_parser.match(line)
    family_name = m.group(3)
    intrin_name = m.group(1)

    if not family_name in families:
      families[family_name] = {
        'functions': []
      }

    funcInfo = {
      'name': intrin_name,
      'implemented': False,
    }

    families[family_name]['functions'].append(funcInfo)

    for header in files:
      if files[header].find("simde_" + intrin_name[2:]) >= 0:
        funcInfo['implemented'] = True
        break

    summary['functions'] = summary['functions'] + 1
    if funcInfo['implemented']:
      summary['implemented'] = summary['implemented'] + 1

print('# MSA\n')

print('Overall, SIMDe implementents %d of %d (%.2f%%) functions from MSA.\n' % (
  summary['implemented'],
  summary['functions'],
  (float(summary['implemented']) / float(summary['functions'])) * 100.0
))

for family_name in sorted(families.keys()):
  family = families[family_name]

  print('## ' + family_name + '\n')

  for func in family['functions']:
    if func['implemented']:
      print(' * [x] ' + func['name'])
    else:
      print(' * [ ] ' + func['name'])

  print('')
