#!/bin/bash

SCRIPT_DIR="$(dirname $0)"
if [ -z "$1" ]; then
    PATH_TO_SIMDE="${SCRIPT_DIR}/../../simde"
else
    PATH_TO_SIMDE="$1"
fi

# Download the IIG
if [ ! -e "${SCRIPT_DIR}"/../data/iig.xml ]; then
  IIG_VERSION="$(curl -s https://software.intel.com/sites/landingpage/IntrinsicsGuide/ | grep -Po '(?<=intrinsicsguide.min.js\?)([0-9\.]+)')"
  curl -s "https://software.intel.com/sites/landingpage/IntrinsicsGuide/files/data-${IIG_VERSION}.xml" > "${SCRIPT_DIR}"/../data/iig.xml;
fi

"${SCRIPT_DIR}"/update-x86.py "$PATH_TO_SIMDE" "${SCRIPT_DIR}/../data/iig.xml" > "${SCRIPT_DIR}/../x86.md"
"${SCRIPT_DIR}"/update-neon.py "$PATH_TO_SIMDE" "${SCRIPT_DIR}/../data/neon-funcs.txt" > "${SCRIPT_DIR}/../neon.md"
"${SCRIPT_DIR}"/update-avx512.py "$PATH_TO_SIMDE" "${SCRIPT_DIR}/../data/iig.xml" > "${SCRIPT_DIR}/../avx512.md"
