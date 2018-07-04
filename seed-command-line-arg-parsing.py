"""
A seed for command-line argument parsing in Python.

Covers:

* Parsing arguments and options
* Showing help text
* Validating presence/absence of mandatory parameters
* Validating parameter type (e.g. expect a number)
* Handling optional parameters
* Hanlding short (-v) and long (--verbose) version of parameters

It uses argparse because it's available with python. If external depedencies
are not a problem, consider using click (while clint and docopt are also good
options, click makes a compelling case: http://click.pocoo.org/5/why/).

Sources for this code and command-line programs in general:

* https://pyvideo.org/europython-2014/writing-awesome-command-line-programs-in-python.html
* https://docs.python.org/3/library/argparse.html
* https://docs.python.org/3/howto/argparse.html

This program takes two arguments and a few options (argparse gives --help|-h
for free):

   number1 number1 [--operation add|multiply] (default 'add') [--verbose|-v]

The program adds or multiplies the first two numbers, as specified. Verbose
does what is expected: print more information.
"""

from argparse import ArgumentParser


def main():
    ap = ArgumentParser(description='Add or multiply two numbers.')

    # The numbers to operate on - they are positional arguments
    # Note that we rely on argparse for type validation ('type=int')
    ap.add_argument('number1', help='First number', type=int)
    ap.add_argument('number2', help='Second number', type=int)

    # This argument accepts two options and it's optional (if not specified
    # at all [const] or specified but no value is given [default] it will
    # assume the value 'sum')
    operations = ['add', 'multiply']
    ap.add_argument('--operation', choices=operations, nargs='?',
                    const='sum', default='sum',
                    help='Operation to execute on the two numbers')

    # This is a true/false argument ('store_true')
    ap.add_argument('-v', '--verbose', help='Enter verbose mode',
                    action='store_true')

    args = ap.parse_args()

    if args.verbose:
        print('Operation is {}'.format(args.operation))

    answer = args.number1 + args.number2 if args.operation == operations[0] \
        else args.number1 * args.number2
    print('Answer: {}'.format(answer))

if __name__ == '__main__':
    main()
