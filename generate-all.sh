#!/bin/bash

vers="0.8.1"
lang="en"
verslong="./docs_$lang/OWASP SAP Security Verification Standard $vers-$lang"

python3 export.py --format json --language $lang > "$verslong.json"
python3 export.py --format xml --language $lang > "$verslong.xml"
python3 export.py --format csv --language $lang > "$verslong.csv"

# ./generate_document.sh $lang $vers


lang="de"
verslong="./docs_$lang/OWASP SAP Security Verification Standard $vers-$lang"
python3 export.py --format json --language $lang > "$verslong.json"
python3 export.py --format xml --language $lang > "$verslong.xml"
python3 export.py --format csv --language $lang > "$verslong.csv"
