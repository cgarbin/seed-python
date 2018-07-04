"""
A seed for processing files in Python.

Covers:

* Process more than one file with file globbing
* Working with pipes (redirect stdin and stdout)
* Accepting command line options with file names
* Mutually exclusive command line options with a default option

Does NOT cover:

* Non-text (binary) files

Sources for this code:

* https://docs.python.org/3/library/fileinput.html
* The command line parsing seed program (seed-command-line-arg-parsing.py)

Examples:

   file.txt --tolower
   file.txt --toupper
   file.txt (defaults to '--tolower')
   *.txt --tolower  (file globbing)
   cat file.txt | thisscript.py (read from stdin)

Some extended chars to test UTF-8 handling against this source code:
   á Á ñ Ñ - çãü
"""

import fileinput
from argparse import ArgumentParser
import sys


def main():
    ap = ArgumentParser(
        description='Change file contents to all lower or all caps',
        epilog='Reads from stdin if no file is specified')

    # The files to be processsed
    # Use nargs='?' to allow calling without a file name, to read from stdin.
    # "default='-'" is used to make fileinput behave correctly when invoking
    # in a pipe (reading from stdin) with arguments, e.g. "cat somefile.txt
    # | thisscript.py --to lower". If no file name is given fileinput attempts
    # to use the full command line as the parameter. This results in fileinput
    # trying to open the files '--to' and 'lower'. Setting the defailt to '-'
    # points fileinput to stdin in that case.
    ap.add_argument('files', metavar='file1 file2 ...',
                    help='Files to process', nargs='?', default='-')

    # The operation to perform (tolower/toupper) as a set of mutually exclusive
    # options, with default = tolower
    group = ap.add_mutually_exclusive_group()
    group.add_argument('-l', '--tolower', action='store_const', dest='op',
                       const=str.lower, help='Convert to lower case')
    group.add_argument('-u', '--toupper', action='store_const', dest='op',
                       const=str.upper, help='Convert to upper case')
    ap.set_defaults(op=str.lower)

    ap.add_argument('-v', '--verbose', help='Enter verbose mode',
                    action='store_true')

    args = ap.parse_args()

    with fileinput.input(files=(args.files)) as f:
        for line in f:
            # File name is available only after at least one line is read
            if args.verbose and f.isfirstline():
                print('Processing {}'.format(f.filename()), file=sys.stderr)
            print(args.op(line), end='')

if __name__ == '__main__':
    main()
