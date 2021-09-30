import os
import sys
import ast
from glob import glob

from nutrients_parser import parse_html

# dynamically generate a test for each of the data files
for filename in sorted(glob(os.path.dirname(__file__) + '/data/html/*.html')):
    prettyname = os.path.basename(filename).replace('.html', '')
    exec("""
def test_%s():
    filename = "%s"
    with open(filename, 'r') as f:
        result = parse_html(f.read())

        outfilename = filename + '.out'
        if os.path.isfile(outfilename):
            with open(outfilename, 'r') as fexpect:
                expected = ast.literal_eval(fexpect.read())
                if result != expected:
                    raise AssertionError(result)
    """ % (prettyname, filename))