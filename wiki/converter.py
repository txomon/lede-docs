import argparse
import re
import sys

# Limitations
#
# Italic, bold, and underlined text have really simple replace mechanism
#  which doesn't take into consideration linebreaks from docuwiki
#

parser = argparse.ArgumentParser('docuwiki2mediawiki')

parser.add_argument('input_file', help='File to convert')
parser.add_argument('-o', '--output', help='Output file',
                    default=sys.stdout, type=argparse.FileType(mode='wt'))

arguments = parser.parse_args()

input_lines = arguments.input_file.readlines()

in_table = False
row = 0


def replace_headers(line):
    if re.match(r'/^ *======.*====== *$/', line):
        line = re.sub(r'/^ *======/', '=', line)
        line = re.sub(r'/====== *$/', '=', line)
    elif re.match(r'/^ *=====.*===== */', line):
        line = re.sub(r'/^ *=====/', '==', line)
        line = re.sub(r'/===== */', '==', line)
    elif (re.match(r'/^ *====.*==== */', line)):
        line = re.sub(r'/^ *====/', '===', line)
        line = re.sub(r'/==== */', '===', line)
    elif (re.match(r'/^ *===.*=== */', line)):
        line = re.sub(r'/^ *===/', '====', line)
        line = re.sub(r'/=== */', '====', line)
    elif (re.match(r'/^ *==.*== */', line)):
        line = re.sub(r'/^ *==/', '=====', line)
        line = re.sub(r'/== */', '=====', line)
    return line


def replace_bullet_points(line):
    # Bullet list requires spacing by two and one space after the list definitor
    # no brainer implementation because not worth amount of code
    if line.startswith('  * '):
        line = '*' + line[3:]
    elif line.startswith('    * '):
        line = '**' + line[5:]
    elif line.startswith('      * '):
        line = '***' + line[7:]
    return line


def replace_numbered_list(line):
    # Bullet list requires spacing by two and one space after the list definitor
    # no brainer implementation because not worth amount of code
    if line.startswith('  - '):
        line = '#' + line[3:]
    elif line.startswith('    - '):
        line = '##' + line[5:]
    elif line.startswith('      - '):
        line = '###' + line[7:]
    return line


def replace_formatting(line):
    # Italic needs the opening to start with ' //', because else we may end up
    # replacing urls, and the end of italics should be with '// ', for the same
    # reason

    # First some combinations
    prev, this = '', line
    while prev != this:
        prev = this
        this = re.sub(r'/ \/\/\*\*/', " '''''", this)
        this = re.sub(r'/\*\*\/\/ /', "''''' ", this)
        this = re.sub(r'/ \*\*\/\//', " '''''", this)
        this = re.sub(r'/\/\/\*\* /', "''''' ", this)

    # Second simple ones to avoid overlap
    prev = ''
    while prev != this:
        prev = this
        this = re.sub(r'/ \/\//', " ''", this)
        this = re.sub(r'/\/\/ /', "'' ", this)
        this = re.sub(r'/ \*\*/', " '''", this)
        this = re.sub(r'/\*\* /', "''' ", this)

    # There is no underscoring in mediawiki

    prev = ''
    while prev != this:
        prev = this
        this = re.sub(r'/\\\\ /', '<br />', this)

    return this



for line_no, line in enumerate(input_lines):
    if in_table:
        row += 1
    line = replace_headers(line)
    line = replace_bullet_points(line)
    line = replace_numbered_list(line)
    line = replace_formatting(line)




