'''

test_submission.py: Evaluation of ContainersFTW result

Copyright (c) 2017, Vanessa Sochat. All rights reserved. 

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
import sys
import tarfile
sys.path.append('..') # directory with client

from unittest import TestCase
import shutil
import pandas

here = os.path.dirname(os.path.abspath(__file__))

print("*** RESULT EVALUATION START ***")

class TestSubmission(TestCase):

    def setUp(self):
        self.submission = os.path.join(here,'..','results','submission.csv')

        print("\n# START ###########################################")

    def tearDown(self):
        print("# END #############################################")

    def test_submission_exists(self):
        '''ensure that submission is present
        '''
        
        print("Testing that submission is present")
        self.assertTrue(os.path.exists(self.submission))

        print("Testing load of submission")
        result = pandas.read_csv(self.submission,index_col="id")
        self.assertTrue(isinstance(result,pandas.DataFrame))

        print("Validating header fields")
        required = ['id','prediction']  
        for r in required:
            self.assertTrue(r in result.columns.tolist())


if __name__ == '__main__':
    unittest.main()
