#!/bin/python3

import re, os, sys

families = {}

skipped_functions = 0

if len(sys.argv) < 3:
    sys.exit('Usage: ' + sys.argv[0] + ' /path/to/simde /path/to/neon-funcs.txt')

with open(sys.argv[2]) as fp:
    regex = re.compile("^v((([a-z0-9]+[^q])|ceq)q?)(_rot(90|180|270))?(_dup)?((_lane)q?)?(_low)?(_high)?(_n)?((_lane)q?)?(_((s|u|p|f|bf)(8|16|32|64|128)))?_((s|u|p|f|bf)(8|16|32|64|128))")
    regex_single = re.compile("^(.+)(b|h|s|d)$")

    possible_singles = []

    func = ''
    while True:
        func = fp.readline().strip()
        if func == '':
            break

        m = regex.match(func)
        if m is None:
            print('No match for ' + func)
            break

        groups = m.groups()

        if groups[18] == 'p' or groups[17] == 'bf16' or groups[17] == 'f16':
            skipped_functions += 1
            continue

        sm = regex_single.match(groups[0])
        if sm is not None:
            possible_singles.append(func)
            continue

        family = groups[1]

        for idx in [7, 9, 10]:
            if groups[idx] is not None:
                family += groups[idx]

        if family not in families:
            families[family] = []

        families[family].append(func)

        # print(func + ' -> ' + family)

        if func == "vabal_high_u8x":
            print([family, groups])

            for i in range(len(groups)):
                print("\t" + str(i) + ": " + str(groups[i]))

            break

    for func in possible_singles:
       m = regex.match(func)
       groups = m.groups()

       sm = regex_single.match(groups[0])
       if sm.group(1) in families:
           families[sm.group(1)].append(func)
       elif sm.group(0) in families:
           families[sm.group(0)].append(func)

complete_families = 0
partial_families = 0
complete_functions = 0
total_functions = 0

for family in families:
    funcs_found = []
    funcs_missing = []

    for func in families[family]:
        r = os.system('grep -PRq simde_' + func + ' ' + sys.argv[1] + '/simde/arm/neon')
        total_functions += 1
        if r == 0:
            funcs_found.append(func)
        else:
            funcs_missing.append(func)

    family_link = '[' + family + '](https://developer.arm.com/architectures/instruction-sets/simd-isas/neon/intrinsics?search=v' + family + ')'

    if len(funcs_missing) == 0:
        print(' - [x] ' + family_link)
        complete_families += 1
        complete_functions += len(families[family])
    else:
        print(' - [ ] ' + family_link)
        if len(funcs_found) != 0:
            partial_families += 1
            for func in families[family]:
                if func in funcs_found:
                    print('   - [x] ' + func)
                    complete_functions += 1
                else:
                    print('   - [ ] ' + func)

print("\n{0}/{1} ({2}%) of function families are fully implemented. Another {3} ({4}%) are partially implemented.\n".format(complete_families, len(families), int((complete_families / len(families)) * 100.0), partial_families, int((partial_families / len(families)) * 100.0)))
print("Overall, {0}/{1} ({2}%) of functions are implemented.\n".format(complete_functions, total_functions, int((complete_functions / total_functions) * 100.0)))
print("Note: this list does not include {0} functions for poly types or 16-bit floats; SIMDe doesn't support those yet.".format(skipped_functions))
