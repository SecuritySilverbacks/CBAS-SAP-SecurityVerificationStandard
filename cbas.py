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
import copy

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
    source_language = 'en'
    config = { }

    def __init__(self, source_language:str, config:dict):

        regex = re.compile('Version (([\d.]+){3})')
        self.source_language = source_language
        self.boilerplate = self.boilerplate + "_" + self.source_language
        self.controls = self.controls + "_" + self.source_language
        self.config = config

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
        files = [f for f in os.listdir(path = self.controls) if re.match('.*\.md', string=f) ]
        for filename in files:
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
                if filename in {'Control_Template.md', 'README.md'}:
                    continue

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
                        attribute = header.split(sep=':', maxsplit=1)[0].strip()
                        value = header.split(sep=':', maxsplit=1)[1]
                        if self.get_ControlIdentifier_for_lang(identifier='Security Function', lang=self.source_language) == attribute :
                            control['Security Function'] = value.strip()
                            continue
                        elif self.get_ControlIdentifier_for_lang(identifier='Category', lang=self.source_language) == attribute :
                            control['CSF Category'] = value.strip()
                            continue
                        elif self.get_ControlIdentifier_for_lang(identifier='Technology', lang=self.source_language) == attribute : 
                            control['Technology'] = value.strip()
                            continue
                        elif self.get_ControlIdentifier_for_lang(identifier='Maturity Level', lang=self.source_language) == attribute :
                            control['Maturity Level'] = value.strip()
                            continue
                        elif self.get_ControlIdentifier_for_lang(identifier='IPAC', lang=self.source_language) == attribute :
                            regex = re.compile('(?<=\()[IPAC](?=\))') #select the header
                            m = re.findall(regex, header)
                            for match in m:
                                control['IPAC'].append(match)
                            continue
                        elif self.get_ControlIdentifier_for_lang(identifier='Defender', lang=self.source_language) == attribute :
                            for match in value.strip().split(sep=' '):
                                control['Defender'].append(match)
                            continue
                        elif self.get_ControlIdentifier_for_lang(identifier='Prerequisites', lang=self.source_language) == attribute :
                            for match in value.strip().split(sep=' '):
                                control['Prerequisites'].append(match)
                            continue

                self.cbas['Controls'].append(control)

    
    def get_Controls(self) ->list:
        return self.cbas['Controls']

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.cbas, indent = 2, sort_keys = False).strip()

    def to_xml(self):
        return dicttoxml.dicttoxml(self.cbas, attr_type=False).decode('utf-8')

    def to_csv(self):
        # make flat structure first
        cbas_flat = self.make_flat() 

        # ''' Returns CSV '''
        si = StringIO()
        
        writer = csv.DictWriter(si, [self.get_ControlIdentifier_for_lang(identifier = 'Shortcode'), 
                                     self.get_ControlIdentifier_for_lang(identifier = 'Security Function'),
                                     self.get_ControlIdentifier_for_lang(identifier = 'CSF Category'), 
                                     self.get_ControlIdentifier_for_lang(identifier = 'IPAC'),
                                     self.get_ControlIdentifier_for_lang(identifier = 'Technology'), 
                                     self.get_ControlIdentifier_for_lang(identifier = 'Maturity Level'),
                                     self.get_ControlIdentifier_for_lang(identifier = 'Defender'), 
                                     self.get_ControlIdentifier_for_lang(identifier = 'Prerequisites'), 
                                     self.get_ControlIdentifier_for_lang(identifier = 'Description'),
                                     self.get_ControlIdentifier_for_lang(identifier = 'Implementation'), 
                                     self.get_ControlIdentifier_for_lang(identifier = 'Verification'),
                                     self.get_ControlIdentifier_for_lang(identifier = 'References')])
        
        writer.writeheader()
        
        for row in cbas_flat:
            keys = list(row.keys())
            for key in keys:
                row[self.get_ControlIdentifier_for_lang(identifier = key)] = row.pop(key)

        writer.writerows(cbas_flat)

        return si.getvalue()
    
    def control_to_md(self, control: dict) -> dict:

        filename = "{shortcode}.md".format(shortcode=control['Shortcode'])
        md = "---\n\
Security Function: {Security_Function}\n\
Category: {CSF_Category}\n\
Technology: {Technology}\n\
Maturity Level: {Maturity_Level}\n\
IPAC: {IPAC}\n\
Defender: {Defender}\n\
Prerequisite {Prerequisites}:\n\
---\n\
\n\
## Description\n\
\n\
{Description}\n\
\n\
## Implementation\n\
\n\
{Implementation}\n\
\n\
## Verification of Control\n\
\n\
{Verification}\n\
\n\
## References:\n\
\n\
{References}".format(Security_Function = control['Security Function'],
                                 CSF_Category = control['CSF Category'],
                                 Technology = control["Technology"],
                                 Maturity_Level = control['Maturity Level'],
                                 IPAC = ''.join(str(i) for i in control['IPAC']),
                                 Defender = ' '.join(str(d) for d in control['Defender']),
                                 Prerequisites = '- \n'.join(str(p) for p in control['Prerequisites']),
                                 Description = control['Description'],
                                 Implementation = control['Implementation'],
                                 Verification = '\n'.join(str(v) for v in control['Verification']),
                                 References = '\n'.join(str(r) for r in control['References']))
        return {'filename': filename, 'content': md}


    def make_flat(self) -> list :

        cbas_flat = [ ]
        control_flat = {}

        for control in self.cbas["Controls"]:
            control_flat['Shortcode'] = control['Shortcode']
            control_flat['Security Function'] = control['Security Function']
            control_flat['CSF Category'] = control['CSF Category']
            control_flat['Technology'] = control['Technology']
            control_flat['Maturity Level'] = control['Maturity Level']
            control_flat['IPAC'] = "".join(control['IPAC'])
            control_flat['Defender'] = '\n'.join(control['Defender'])
            control_flat['Prerequisites'] = '\n'.join(control['Prerequisites'])

            control_flat['Description'] = control['Description']
            control_flat['Implementation'] = control['Implementation']
            control_flat['Verification'] = '\n'.join(control['Verification'])
            control_flat['References'] = '\n'.join(control['References'])

            cbas_flat.append(copy.copy(control_flat))
            control_flat = {}

        return cbas_flat
    
    def get_ControlIdentifier_for_lang(self, identifier: str, lang = None) -> str:

        if identifier not in self.config.keys():
            return identifier
        return self.config[identifier][self.source_language if lang is None else lang]

