#!/bin/python3

import os, sys, glob, json, pprint, re

# The NEON intrinsics JSON file doesn't separate functions how we would
# like; the same operation

data = []
families = {}
architectures = {}
familyNames = {}
unsupportedTypes = {
  "poly": [],
  "bf16": []
}

family_overrides = {
  'vpmaxqd_f64': 'pmax',
  'vpminqd_f64': 'pmin',
  'vpmaxnmqd_f64': 'pmaxnm',
  'vpminnmqd_f64': 'pminnm',
  'vrecpxs_f32': 'recp',
  'vrecpxd_f64': 'recp',
  'vldrq_p128': 'ldr',
  'vstrq_p128': 'str',
  'vaeseq_u8': 'aes',
  'vaesdq_u8': 'aes',
  'vaesmcq_u8': 'aes',
  'vaesimcq_u8': 'aes',
  'vsha1cq_u32': 'sha1',
  'vsha1pq_u32': 'sha1',
  'vsha1mq_u32': 'sha1',
  'vsha1su0q_u32': 'sha1',
  'vsha1su1q_u32': 'sha1',
  'vsha256hq_u32': 'sha256',
  'vsha256h2q_u32': 'sha256',
  'vsha256su0q_u32': 'sha256',
  'vsha256su1q_u32': 'sha256',
  'vsha512hq_u64': 'sha512',
  'vsha512h2q_u64': 'sha512',
  'vsha512su0q_u64': 'sha512',
  'vsha512su1q_u64': 'sha512',
  'veor3q_u8': 'eor3',
  'vrax1q_u64': 'rax',
  'vxarq_u64': 'xar',
  'vbcaxq_u8': 'bcax',
  'vsm3ss1q_u32': 'sm3',
  'vsm3tt1aq_u32': 'sm3',
  'vsm3tt1bq_u32': 'sm3',
  'vsm3tt2aq_u32': 'sm3',
  'vsm3tt2bq_u32': 'sm3',
  'vsm3partw1q_u32': 'sm3',
  'vsm3partw2q_u32': 'sm3',
  'vsm4eq_u32': 'sm4',
  'vsm4ekeyq_u32': 'sm4',
  'vmmlaq_s32': 'mmla',
  'vusmmlaq_s32': 'mmla',
  'vbfmmlaq_f32': 'mmla',
  'vbfmlalbq_f32': 'fmlal',
  'vbfmlaltq_f32': 'fmlal',
  'vbfmlalbq_lane_f32': 'fmlal_lane',
  'vbfmlaltq_lane_f32': 'fmlal_lane',
  'vbfmlalbq_laneq_f32': 'fmlal_lane',
  'vbfmlaltq_laneq_f32': 'fmlal_lane',
  'vcvtq_low_f32_bf16': 'cvt_low'
}

pp = pprint.PrettyPrinter(indent=2)

patterns = {
  "family_shortener": re.compile('^([a-z0-9]+)([a-z0-9])(_.+)?$')
}

files = {}
for file in glob.glob(os.path.join(sys.argv[1], 'simde/arm/neon/*.h')):
    files[os.path.splitext(os.path.basename(file))[0]] = open(file).read()

# The question we're trying to answer here is (for example) vceq_u8 the
# 128-bit version of vce_u8, or the 64-bit version of vceqq_u8?  In
# order to do this we make two passes; the first time we ignore the
# anything ending with "q" *except* for anything ending in "qq" (which
# we know will be a 128-bit version of the single-q family).  Then we
# can go through in a second pass and check to see which family already
# exists.
def group_intrin(intrin, force=False):
  # print("\n" + intrin["name"] + "...")
  # pp.pprint(intrin)

  name_components = intrin["name"].split("_")
  base_name = name_components[0]

  # __crc* functions
  if len(base_name) == 0:
    return True;

  assert base_name[0] == 'v'

  family_name = base_name[1:]

  for component in name_components[1:]:
    unsupportedType = False

    if component in ['s8', 'u8', 's16', 'u16', 's32', 'u32', 's64', 'u64', 'f16', 'f32', 'f64']:
      pass
    elif component in ['p8', 'p16', 'p32', 'p64', 'p128']:
      unsupportedTypes["poly"].append(intrin)
      intrin["skip"] = True
    elif component in ['bf16']:
      unsupportedTypes[component].append(intrin)
      intrin["skip"] = True
    elif component in ['dup', 'high', 'low', 'n', 'x2', 'x3', 'x4']:
      family_name += '_' + component
    elif component in ['lane', 'laneq']:
      family_name += '_lane'
    elif component in ['rot90', 'rot180', 'rot270']:
      family_name += '_rot'
    else:
      assert False

  if intrin["name"] in family_overrides:

    family_name = family_overrides[intrin["name"]]

  elif not force:

    # Ends with q, but not qq
    if base_name[-1] == 'q':
      if base_name[-2] == 'q':
        family_name = family_name[:-1]
      else:
        return False

    if base_name[-1] == 'b' and name_components[-1] in ["s8", "u8"]:
      return False
    elif base_name[-1] == 'w' and name_components[-1] in ["s16", "u16", "f16", "bf16"]:
      return False
    elif base_name[-1] == 's' and name_components[-1] in ["s32", "u32", "f32"]:
      return False
    elif base_name[-1] == 'd' and name_components[-1] in ["s64", "u64", "f64"]:
      return False

  else:

    if family_name not in families:
      m = patterns["family_shortener"].match(family_name)
      shorter = m.group(1)
      if m.group(3) != None:
        shorter += m.group(3)
      if shorter in families:
        family_name = shorter
      else:
        assert False

  for header in files.keys():
    if files[header].find("simde_" + intrin["name"]) >= 0:
      intrin["implemented"] = True
      break

  if family_name not in families:
    families[family_name] = {
      "unsupported": 0,
      "implemented": 0,
      "functions": []
    }

  for arch in intrin["Architectures"]:
    if arch not in architectures:
      architectures[arch] = {
        "total": 0,
        "implemented": 0,
        "unsupported": 0
      }

    architectures[arch]["total"] = architectures[arch]["total"] + 1
    if intrin["skip"]:
      architectures[arch]["unsupported"] = architectures[arch]["unsupported"] + 1
    if intrin["implemented"]:
      architectures[arch]["implemented"] = architectures[arch]["implemented"] + 1

  families[family_name]["functions"].append(intrin)
  if intrin["skip"]:
    families[family_name]["unsupported"] = families[family_name]["unsupported"] + 1
  elif intrin["implemented"]:
    families[family_name]["implemented"] = families[family_name]["implemented"] + 1

  return True

with open(sys.argv[2]) as fp:
  for intrin in json.load(fp):
    if intrin["SIMD_ISA"] != "neon":
      continue

    intrin["implemented"] = False
    intrin["skip"] = False

    data.append(intrin)

  skipped = []
  for intrin in data:
    # if len(skipped) > 10:
    #   break
    if not group_intrin(intrin, False):
      skipped.append(intrin)

  for intrin in data:
    group_intrin(intrin, True)

# Okay, now everything should be where we want it.

print("# Summary\n")



print("TL;DR: SIMDe currently implements %d out of %d (%.2f%%) NEON functions.  If you don't count poly types, it's %d / %d (%.2f%%).\n" % (
  architectures["A64"]["implemented"],
  architectures["A64"]["total"],
  ((float(architectures["A64"]["implemented"]) / float(architectures["A64"]["total"])) * 100.0),
  architectures["A64"]["implemented"],
  architectures["A64"]["total"] - architectures["A64"]["unsupported"],
  ((float(architectures["A64"]["implemented"]) / (float(architectures["A64"]["total"] - architectures["A64"]["unsupported"]))) * 100.0),
))

print("SIMDe does not currently support polynomial types, so they are excluded from this list (though separate totals are often provided to be transparent about what was skipped.  We do plan to support these types in the future.\n")

print("# Functions by Architecture\n")

print('| Architecture | Functions | Functions with supported types | Implemented by SIMDe | Percent implemented |')
print('|--------------|----------:|-------------------------------:|---------------------:|--------------------:|')
for arch in architectures.keys():
  print('| ', end='')
  if arch == "v7":
    print('%12s' % "ARMv7", end=' |')
  elif arch == "A32":
    print('%12s' % "ARMv8", end=' |')
  elif arch == "A64":
    print('%12s' % "AArch64", end=' |')
  else:
    print('%12s' % arch, end=' |')

  print('%10d' % (architectures[arch]["total"]), end=' |')
  print('%31d' % (architectures[arch]["total"] - architectures[arch]["unsupported"]), end=' |')
  print('%21d' % (architectures[arch]["implemented"]), end=' |')
  print('%19.2f%%' % ((float(architectures[arch]["implemented"]) / float(architectures[arch]["total"] - architectures[arch]["unsupported"])) * 100.0), end=' |')

  print('')
print('')

completeFamilies = []
incompleteFamilies = []
unimplementedFamilies = []

for family_name in sorted(families):
  family = families[family_name]

  if (len(family["functions"]) - family["unsupported"]) == family["implemented"]:
    completeFamilies.append(family_name)
  elif family["implemented"] > 0:
    incompleteFamilies.append(family_name)
  else:
    unimplementedFamilies.append(family_name)

print("# Families\n")

print("There are %d function families in NEON (based on how we define families).  Discounting functions which use unsupported types, SIMDe has completely implemented %d (%.2f%%) and partially implemented another %d (%.2f%%).\n" % (
  len(families),
  len(completeFamilies),
  (float(len(completeFamilies)) / float(len(families))) * 100.0,
  len(incompleteFamilies),
  (float(len(incompleteFamilies)) / float(len(families))) * 100.0
))

print("## Incomplete Families\n")

print("There are currently %d incomplete families.\n" % len(incompleteFamilies))

for family_name in incompleteFamilies:
  print('### ' + family_name + "\n")

  family = families[family_name]
  implementable = (len(family["functions"]) - family["unsupported"])

  if implementable == 0:
    print("Family only contains functions which require unsupported types.\n")
  else:
    print('SIMDe currently implements %d of %d (%.2f%%) functions' % (family["implemented"], implementable, (float(family["implemented"]) / implementable) * 100.0), end="")
    if family["unsupported"] > 0:
      print(", not counting %d which require currently unsupported types.\n" % family["unsupported"])
    else:
      print(".\n")

  for func in family["functions"]:
    if not func["skip"]:
      if func["implemented"]:
        print(' * [x] ', end='')
      else:
        print(' * [ ] ', end='')
      print(func["name"])

  print('')

print("## Unimplemented Families\n")

print("There are currently %d unimplemented families.\n" % len(incompleteFamilies))

for family_name in unimplementedFamilies:
  family = families[family_name]

  desc = []
  if len(family["functions"]) > family["unsupported"]:
    desc.append("%d functions" % (len(family["functions"]) - family["unsupported"]))
  if family["unsupported"] > 0:
    desc.append("%d functions with unsupported types" % family["unsupported"])

  print(' * %s' % family_name, end='')
  print(" (" + (", plus ".join(desc)) + ")")
print('')

print("## Complete Families\n")

print("SIMDe contains complete implementations of %d functions families.\n" % len(completeFamilies))

for family_name in completeFamilies:
  family = families[family_name]

  print(" * " + family_name, end='')

  if family["unsupported"] > 0:
    print(' (%d functions with unsupported types)' % family["unsupported"])
  else:
    print('')
