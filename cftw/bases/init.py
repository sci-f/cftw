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
    mkdir_p,
    tree,
    write_json
)
from .template import (
    get_template,
    sub_template
)

import sys
import os


def generate_base(template, name, output_folder=None):
    '''generation of a base means copying an entire template
    into the user's output folder. If None is specified, $PWD 
    is used
    '''
    if output_folder is None:
        output_folder = os.getcwd()

    bot.newline()
    bot.debug("Starting base generation in %s" %output_folder)
    template = get_template(template,output_folder)
    tree("%s/%s" %(output_folder,template))

    # The result folder is specific to the competition
    results = '%s/analysis/results' %(template)
    mkdir_p(results)
    result_template = get_template(template='leaderboard',
                                   template_type='results',
                                   name=name,
                                   output_folder=results)

    # Substitute competition name in Singularity file,
    # template
    files = [ "%s/Singularity" %template,
              "%s/.travis.yml" %template,
              "%s/index.html" %result_template ]

    for filey in files:
        sub_template(filey,{"COMPETITION_NAME":name})

    bot.debug("Finished generation.")
    return template
