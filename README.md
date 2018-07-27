# seed-python

Seed files for Python code

## [seed-command-line-arg-parsing.py](./seed-command-line-arg-parsing.py)

A seed for command-line argument parsing in Python.

Covers:

* Parsing arguments and options
* Showing help text
* Validating presence/absence of mandatory parameters
* Validating parameter type (e.g. expect a number)
* Handling optional parameters
* Handling short (`-v`) and long (`--verbose`) version of parameters

It uses `argparse` because it's available with python. If external depedencies
are not a problem, consider using [click](http://click.pocoo.org) (while
[clint](https://github.com/kennethreitz/clint) and [docopt](https://github.com/docopt/docopt)
are also good options, [click makes a compelling case for itself](http://click.pocoo.org/5/why/).

Sources for this code and command-line programs in general:

* https://pyvideo.org/europython-2014/writing-awesome-command-line-programs-in-python.html
* https://docs.python.org/3/library/argparse.html
* https://docs.python.org/3/howto/argparse.html

This program takes two arguments and a few options (`argparse` gives `--help|-h`
for free):

    number1 number1 [--operation add|multiply] (default 'add') [--verbose|-v]

The program adds or multiplies the first two numbers, as specified. Verbose
does what is expected: print more information.

## [seed-command-line-file-processing.py](./seed-command-line-file-processing.py)

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
* The command line parsing seed program [seed-command-line-arg-parsing.py](./seed-command-line-arg-parsing.py)

Examples:

    file.txt --tolower
    file.txt --toupper
    file.txt (defaults to '--tolower')
    *.txt --tolower  (file globbing)
    cat file.txt | thisscript.py (read from stdin)
   
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
