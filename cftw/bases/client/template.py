'''
The MIT License (MIT)

Copyright (c) 2016-2017 Vanessa Sochat

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

from cftw.logger import bot
from cftw.utils import (
    read_file,
    write_file,
    mkdir_p,
    get_installdir,
    write_json
)

from glob import glob
import shutil
import sys
import os

here = get_installdir()

def list_templates(template_type="bases"):
    templates_base = "%s/bases/templates/%s" %(here,template_type)
    names = [os.path.basename(x) for x in glob("%s/*" %templates_base)]
    return names


def sub_template(template_file,items):
    '''replace some set of key/value pairs in a
    template file (inplace) with the expectation
    that a key should be within {{ }}'''
    with open(template_file,'r') as filey:
        content = filey.read()
        for key,val in items.items():
            key = "{{ %s }}" %key
            content = content.replace(key,val)

    with open (template_file,'w') as filey:
        filey.writelines(content)
    return template_file


def get_template(template, output_folder, name=None, template_type="bases"):
    '''get_template will copy a template (based on filename off
    of templates) into an output folder.
    '''
    if not os.path.exists(output_folder):
        bot.error("%s does not exist, please create first." %output_folder)
        sys.exit(1)    

    if name is None:
        name = os.path.basename(template)

    templates_base = "%s/bases/templates/%s" %(here,template_type)
    path = "%s/%s" %(templates_base,template)
    finished = "%s/%s" %(output_folder,name) 
    try:
        shutil.copytree(path,finished)
    except FileExistsError:
        bot.error("Folder %s already exists, will not overwrite." %name)
        sys.exit(1)
    return finished
