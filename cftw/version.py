'''
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

__version__ = "0.0.2"
AUTHOR = 'Vanessa Sochat'
AUTHOR_EMAIL = 'vsochat@stanford.edu'
NAME = 'cftw'
PACKAGE_URL = "https://github.com/containers-ftw/cftw"
KEYWORDS = 'open source, containers, reproducible, crowd sourced, science'
DESCRIPTION = "containers for the win is a module for container competitions"
LICENSE = "LICENSE"

INSTALL_REQUIRES = (

    ('requests', {'min_version': '2.12.4'}),
    ('retrying', {'min_version': '1.3.3'}),
    ('selenium', {'min_version': '3.0.2'}),
    ('simplejson', {'min_version': '3.10.0'}),
    ('six', {'min_version': '1.10'}),
    ('pygments', {'min_version': '2.1.3'}),
    ('python-dateutil',{'min_version': None }),
    ('urllib3',{'min_version': "1.15" }),
    ('validator.py',{'min_version': None })
 

)
