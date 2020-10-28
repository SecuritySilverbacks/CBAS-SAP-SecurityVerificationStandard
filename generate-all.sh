#!/bin/bash

lang="en"
vers="0.8"
verslong="./docs_$lang/OWASP CBAS SAP Security Maturity Model $vers-$lang"

python3 export.py --format json --language $lang > "$verslong.json"
python3 export.py --format xml --language $lang > "$verslong.xml"
python3 export.py --format csv --language $lang > "$verslong.csv"

# ./generate_document.sh $lang $vers
