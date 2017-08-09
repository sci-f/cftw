'''
results.py: container competition results helper functions

Copyright (c) 2017 Vanessa Sochat

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

from .logger import bot
import pandas
import os

RESULTBASE = os.environ.get("CONTAINERSFTW_RESULT",'/code/results')

def save_result(result,result_type=None,sep=None,result_base=None):
    '''save a result required for the competition'''

    if result_type is None:
        result_type = "submission"

    if sep is None:
        sep = ','

    filename = get_resultfile(name=result_type,
                              result_base=result_base)

    if filename is not None:
        if isinstance(result,pandas.DataFrame):
            result.to_csv(filename,index=False,sep=sep)
        else:
            bot.error("%s is not a valid result type." %result_type)
    return filename


def list_results(result_base=None):
    '''list the results that a complete model must provide'''

    if result_base is None:
        result_base = RESULTBASE

    # TODO: this should also be generated from a json that is derived automatically
    results = {'submission':'%s/submission.csv' %result_base}

    for title,path in results.items():
        bot.debug("%s : %s" %(title,path))

    return results



def get_resultfile(name=None,result_base=None):
    '''get_resultfile returns the file for the result, or None if 
    not defined
    '''
    results = list_results(result_base)

    if name is not None:
        name = os.path.splitext(name)[0].lower()
        if name in results:
            return results[name]

    bot.info("Results required include: %s" %(','.join(list(results.keys()))))
    return None
