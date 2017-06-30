'''
data.py: container competition data reading functions

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

# NOTE to competition holders - you can update these functions as appropriate
# for your competition.

from .logger import bot
import os

DATABASE = os.environ.get("CONTAINERSFTW_DATA",
                          "/data/input")


def list_data(data_base=None):
    '''list the data, and return lookup to user'''

    bot.info("Valid datasets include:")
    if data_base is None:
        data_base = DATABASE

    # TODO: this should be generated from a json that is derived automatically
    valid_datasets = {'training':'%s/training.csv' %data_base,
                      'test':'%s/test.csv' %data_base,
                      'checking': '%s/checking.csv' %data_base}

    for title,path in valid_datasets.items():
        bot.debug("%s : %s" %(title,path))

    return valid_datasets


def load_data(name=None,index_col=None):
    '''load_dataset will return some data provided for the competition
    '''
    if index_col is None:
        index_col = "id" 

    filename = get_datafile(name=name)
    data = None
    if filename is not None:
        data = pandas.read_csv(filename, index_col=index_col)
    return data



def get_datafile(name=None):
    '''get_data_file returns the file for the dataset, or None if doesn't exist
    '''

    valid_datasets = list_data()

    if name is not None:

        # In case the user gave an extension
        name = os.path.splitext(name)[0].lower()
        if name in valid_datasets:
            return valid_datasets[name]

    bot.info("Valid datasets include: %s" %(','.join(list(valid_datasets.keys()))))
    return None
