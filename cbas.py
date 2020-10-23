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
import re
import json
from xml.sax.saxutils import escape
import csv
import dicttoxml

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class CBASSMM:
    cbas = {}
    cbas['Name'] = "SAP Security Maturity Model"
    cbas['ShortName'] = "CBAS-SMM"
    cbas['Version'] = ""
    cbas['Description'] = "#todo"
    cbas['Boilerplate'] = "boilerplate"
    cbas['Controls'] = "Controls"

    cbas_flat = []

    def __init__(self, language):

        regex = re.compile('Version (([\d.]+){3})')
        self.cbas['Boilerplate'] = self.cbas['Boilerplate'] + "_" + language
        self.cbas['Controls'] = self.cbas['Controls'] + "_" + language

        #loading the boilerplate
        for line in open(os.path.join(self.cbas['Boilerplate'], "0x01-Frontispiece.md"), encoding="utf8"):
            m = re.search(regex, line)
            if m:
                self.cbas['Version'] = m.group(1)
                break

        regex = re.compile('## About the Standard\n\n(.*)')

        with open(os.path.join(self.cbas['Boilerplate'], "0x01-Frontispiece.md"), encoding="utf8") as content:
            m = re.search(regex, content.read())
            if m:
                self.cbas['Description'] = m.group(1)

        self.cbas['Requirements'] = chapters = []


        for file in os.listdir(self.cbas['Controls']):
            header = {};
            header['Identifier'] = ""
            header['SecurityFunction'] = ""
            header['Category'] = ""
            header['Technology'] = ""
            header['MaturityLevel'] = ""
            header['IPAC'] = ""
            header['Defender'] = []
            header['Prerequisits'] = []

            content = {}
            content['Description'] = ""
            content['Implementation'] = ""
            content['VerificationOfControl'] = []
            content['References'] = []

            # re.match("0x\d{2}-V", file)
            regex = re.compile('0x\d{2}-(V([0-9]{1,3}))-(\w[^-.]*)')
            m = re.search(regex, file)
            if m:

                if m:

                    req_flat = {}
                    req_flat['chapter_id'] = chapter['Shortcode']
                    req_flat['chapter_name'] = chapter['Name']
                    req_flat['section_id'] = section['Shortcode']
                    req_flat['section_name'] = section['Name']

                    req = {}
                    req_flat['req_id'] = req['Shortcode'] = "V" + m.group(1)
                    req['Ordinal'] = int(m.group(1).rsplit('.', 1)[1])
                    req_flat['req_description'] = req['Description'] = m.group(2)

                    level1 = {}
                    level2 = {}
                    level3 = {}

                    req_flat['level1'] = m.group(3).strip(' ')
                    req_flat['level2'] = m.group(4).strip(' ')
                    req_flat['level3'] = m.group(5).strip(' ')

                    level1['Required'] = m.group(3).strip() != ''
                    level2['Required'] = m.group(4).strip() != ''
                    level3['Required'] = m.group(5).strip() != ''

                    level1['Requirement'] = ("Optional" if m.group(3).strip('✓ ') == "o" else m.group(3).strip('✓ '))
                    level2['Requirement'] = ("Optional" if m.group(4).strip('✓ ') == "o" else m.group(4).strip('✓ '))
                    level3['Requirement'] = ("Optional" if m.group(5).strip('✓ ') == "o" else m.group(5).strip('✓ '))

                    req['L1'] = level1
                    req['L2'] = level2
                    req['L3'] = level3

                    req['CWE'] = [int(i.strip()) for i in filter(None, m.group(6).strip().split(','))]
                    req_flat['cwe'] = m.group(6).strip()
                    req['NIST'] = [str(i.strip()) for i in filter(None,m.group(7).strip().split('/'))]
                    req_flat['nist'] = m.group(7).strip()

                    section['Items'].append(req)
                    self.cbas_flat.append(req_flat)

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.cbas, indent = 2, sort_keys = False).strip()

    def to_xml(self):
        return dicttoxml.dicttoxml(self.cbas, attr_type=False).decode('utf-8')

    def to_csv(self):
        ''' Returns CSV '''
        si = StringIO()

        writer = csv.DictWriter(si, ['csfsecurityfunction_id', 'csfcategory_name', 'ipac_id', 'ipac_name', 'technology', 'maturitylevel', 'prerequisits', 'description', 'implementation', 'verification', 'references'])
        writer.writeheader()
        writer.writerows(self.cbas_flat)

        return si.getvalue()
