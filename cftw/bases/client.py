#!/usr/bin/env python

'''
client.py: controller for various repo building functions.

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

from glob import glob
import argparse
import sys
import os


def get_parser():
    parser = argparse.ArgumentParser(
    description="Containers For the Win Base Generator")
    subparsers = parser.add_subparsers(help='generation commands',
                                       title='commands',
                                       description='containers-ftw generation commands',
                                       dest="command")
    
    # Generate
    init_parser = subparsers.add_parser("init")

    init_parser.add_argument("--name","-n", dest='name', 
                             help="competition folder name", 
                             type=str, required=True)

    init_parser.add_argument("--template","-t", dest='template', 
                             help="starter template", 
                             type=str, default=None)

    init_parser.add_argument("--out","-o", dest='out', 
                             help="output folder. If not defined, assumes $PWD", 
                             type=str, default=None)
 
    # Build
    build_parser = subparsers.add_parser("add")

    parser.add_argument("--version", dest='version', 
                        help="show software version", 
                        default=False, action='store_true')

    parser.add_argument('--debug', dest="debug", 
                        help="use verbose logging to debug.", 
                        default=False, action='store_true')

    return parser


def main():

    parser = get_parser()

    try:
        args = parser.parse_args()
    except:
        sys.exit(0)


    # if environment logging variable not set, make silent
    if args.debug is False:
        os.environ['MESSAGELEVEL'] = "DEBUG"

    if args.version is True:
        print(cftw.__version__)
        sys.exit(0)

    # Initialize the message bot, with level above
    from cftw.logger import bot
    from cftw.utils import mkdir_p

    if args.command == "init":
        from .init import generate_base

        if args.template is None:
            from .template import list_templates
            available = "\n".join(list_templates())
            subcommand_help("Please provide a base template with --template/-t. Available templates are: \n%s" %available,"init")            

        base = generate_base(template=args.template,
                             output_folder=args.out,
                             name=args.name)      
 


def help():
    parser = get_parser()
    parser.print_help()
    print("For help with an action, type [action] --help")
    sys.exit(1)

def subcommand_help(message,command):
    from cftw.logger import bot
    bot.info(message)
    bot.info("-------------------------------------------------------------")
    bot.info("For help with %s, cftw %s --help" %(command,command))
    sys.exit(1)


if len(sys.argv) == 1:
    help()

if __name__ == '__main__':
    main()
