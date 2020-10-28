#!/usr/bin/env python

''' CBAS document parser and converter class.

    Copyright (c) 2020 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    '''

import os
import regex as re
import json
import csv
import dicttoxml

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class CBASSMM:
    cbas = {}
    cbas['Name'] = "Core Business Application - SAP Security Maturity Model"
    cbas['ShortName'] = "CBAS-SAPSMM"
    cbas['Version'] = ""
    cbas['Description'] = "#todo"
    cbas['Controls'] = []
    boilerplate = "boilerplate"
    controls = "Controls"

    cbas_flat = []

    def __init__(self, language):

        regex = re.compile('Version (([\d.]+){3})')
        self.boilerplate = self.boilerplate + "_" + language
        self.controls = self.controls + "_" + language

        for line in open(os.path.join(self.boilerplate, "0x01-Frontispiece.md"), encoding="utf8"):
            m = re.search(regex, line)
            if m:
                self.cbas['Version'] = m.group(1)
                break

        regex = re.compile('## About the Standard\n\n(.*)')

        with open(os.path.join(self.boilerplate, "0x01-Frontispiece.md"), encoding="utf8") as content:
            m = re.search(regex, content.read())
            if m:
                self.cbas['Description'] = m.group(1)

        self.cbas['Requirements'] = chapters = []

        for filename in os.listdir(self.controls):
            control = {}
            control['Shortcode'] = ""
            control['Security Function'] = ""
            control['CSF Category'] = ""
            control['Technology'] = ""
            control['Maturity Level'] = ""
            control['IPAC'] = []
            control['Defender'] = []
            control['Prerequisites'] = []

            control['Description'] = ""
            control['Implementation'] = ""
            control['Verification'] = []
            control['References'] = []

            control['Shortcode'] = filename.replace(".md", "")

            with open(os.path.join(self.controls, filename), encoding="utf8" ) as file:
                text = file.read()
                regex = re.compile('(?<=##.*\\n)([^#]*)(?!##)') #select the body
                m = re.findall(regex, text)
                if m:
                    control['Description'] = m[0]
                    control['Implementation'] = m[1]    
                    control['Verification'] = m[2].splitlines()
                    control['References'] = m[3].splitlines()
                regex = re.compile('(?<=---.*\\n)([^#]*)(?=---)') #select the header
                m = re.findall(regex, text)
                if m:
                    head = m[0]
                    for header in head.splitlines():
                        if 'Security Function:' in header :
                            control['Security Function'] = header.split(sep=':', maxsplit=1)[1].rstrip()
                            continue
                        elif 'Category:' in header :
                            control['CSF Category'] = header.split(sep=':', maxsplit=1)[1].rstrip()
                            continue
                        elif 'Technology:' in header :
                            control['Technology'] = header.split(sep=':', maxsplit=1)[1].rstrip()
                            continue
                        elif 'Maturity Level:' in header :
                            control['Maturity Level'] = header.split(sep=':', maxsplit=1)[1].rstrip()
                            continue
                        elif 'IPAC:' in header :
                            regex = re.compile('(?<=\()[IPAC](?=\))') #select the header
                            m = re.findall(regex, header)
                            for match in m:
                                control['IPAC'].append(match)
                            continue
                        elif 'Defender:' in header :
                            for match in header.split(sep=':', maxsplit=1)[1].strip().split(sep=' '):
                                control['Defender'].append(match)
                            continue
                        elif 'Prerequisites:' in header :
                            for match in header.split(sep=':', maxsplit=1)[1].strip().split(sep=' '):
                                control['Prerequisites'].append(match)
                            continue
                
                self.cbas['Controls'].append(control)
                    
                control_flat = {}
                control_flat['Shortcode'] = control['Shortcode'] 
                control_flat['Security Function'] = control['Security Function']
                control_flat['CSF Category'] = control['CSF Category'] 
                control_flat['Technology'] = control['Technology'] 
                control_flat['Maturity Level'] = control['Maturity Level'] 
                control_flat['IPAC'] = "".join(control['IPAC'])
                control_flat['Defender'] = "".join(control['Defender'])
                control_flat['Prerequisites'] = "".join(control['Prerequisites'])

                control_flat['Description'] = control['Description']
                control_flat['Implementation'] = control['Implementation']
                control_flat['Verification'] = "".join(control['Verification'])
                control_flat['References'] = "".join(control['References'])

                self.cbas_flat.append(control_flat)

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.cbas, indent = 2, sort_keys = False).strip()

    def to_xml(self):
        return dicttoxml.dicttoxml(self.cbas, attr_type=False).decode('utf-8')

    def to_csv(self):
        ''' Returns CSV '''
        si = StringIO()

        writer = csv.DictWriter(si, ['Shortcode', 'Technology', 'Defender', 'Implementation', 'Security Function', 'Maturity Level', 'Description', 'CSF Category', 'Prerequisites', 'References', 'IPAC', 'Verification'])
        writer.writeheader()
        writer.writerows(self.cbas_flat)

        return si.getvalue()
