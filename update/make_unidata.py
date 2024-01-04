#!/usr/bin/env python3
'''
Regenerates the uniscripts tables from online unicode specifications
'''
SCRIPTS_PATH='Scripts.txt'
SCRIPT_EXTENSIONS_PATH='ScriptExtensions.txt'
PROPERTY_VALUE_ALIASES_PATH='PropertyValueAliases.txt'

def parse_uni_range(range_str):
    """
    Convert Unicode range notation to Python ranges.

    Single codepoints are converted to single-number ranges. That is:

    '0001..0003' -> range(1, 4)
    '0001' -> range(1, 2)
    """
    start_stop_strs = range_str.split('..')
    start = int(start_stop_strs[0], 16)
    end = int(start_stop_strs[1], 16) if len(start_stop_strs) > 1 else start + 1

    return range(start, end + 1)


def read_script_abbrevs(property_value_aliases_path):
    '''load the script abbreviations from file'''
    script_abbrevs = {}
    with open(property_value_aliases_path, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0 or line[0] == '#':
                continue

            if line[0:2] != 'sc':
                continue

            if '#' in line:
                line = line[0 : line.index('#')]

            fields = line.split(';')
            fields = [field.strip() for field in fields]

            if fields[0] != 'sc':
                continue

            script_abbrevs[fields[1]] = fields[2]

    return script_abbrevs

def read_ranges(scripts_path):
    '''load ranges from file'''
    script_ranges={}

    with open(scripts_path, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if len(line) == 0 or line[0] == '#':
                continue

            if '#' in line:
                line = line[0 : line.index('#')]

            fields = line.split(';')
            fields = [field.strip() for field in fields]

            if fields[1] not in script_ranges:
                script_ranges[fields[1]] = []

            script_ranges[fields[1]].append(parse_uni_range(fields[0]))
    return script_ranges

def read_extensions(script_extensions_path, script_abbrevs, script_ranges):
    '''load additional ranges from script extensions'''
    with open(script_extensions_path, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if len(line) == 0 or line[0] == '#':
                continue

            if '#' in line:
                line = line[0 : line.index('#')]

            fields = line.split(';')
            fields = [field.strip() for field in fields]

            char_range = parse_uni_range(fields[0])
            scripts = fields[1].split()

            for script_shortname in scripts:
                longname = script_abbrevs[script_shortname]
                script_ranges[longname].append(char_range)

def slow_which_scripts(char, script_ranges):
    """Returns a list of scripts that char belongs to."""
    cp = ord(char)
    return [script for script, ranges in script_ranges.items()
            if any(cp in seq for seq in ranges)] or ['Unknown']

def get_bucket_inner_ranges(bucket_range: range, script_ranges):
    """
    Returns a list of ranges and corresponding scripts within the specified range.

    Parameters:
    - bucket_range: The range to analyze.

    Returns:
    A list of tuples containing ranges and scripts.
    """
    range_start = bucket_range.start
    i = range_start
    last_script = None
    ranges = []

    while i < bucket_range.stop:
        script = slow_which_scripts(chr(i), script_ranges)

        if script != last_script:
            if last_script is not None:
                ranges.append([range(range_start, i), last_script])
            range_start = i

        last_script = script
        i += 1

    ranges.append([range(range_start, i), last_script])
    return ranges

def main():
    """
    Main function to generate Unicode lookup data from http://ftp.unicode.org/Public/UNIDATA.
    """

    script_abbrevs = read_script_abbrevs(PROPERTY_VALUE_ALIASES_PATH)
    script_ranges = read_ranges(SCRIPTS_PATH)
    read_extensions(SCRIPT_EXTENSIONS_PATH, script_abbrevs, script_ranges)

    # Facilitate tests later on
    script_ranges.setdefault('Unknown', [])

    print("'''Unicode lookup data generated from http://ftp.unicode.org/Public/UNIDATA'''")
    print("# pylint: disable=too-many-lines, line-too-long")

    print("SCRIPT_ABBREVS  = {")
    for k, v in script_abbrevs.items():
        print(f"    '{k}': '{v}',")
    print("}")

    # Subdivide the Unicode space in increments of 1024
    # This allows an initial fast lookup by dividing the character value
    # by 1024 into the corresponding index, limiting the number of ranges
    # to further search
    nb_buckets = 1024 # must be a power of 2
    bucket_width = 65536 // 1024
    print("BUCKETS = [")
    for bucket_index in range(0, nb_buckets):
        bucket_range = range(bucket_index * bucket_width, (bucket_index + 1) * bucket_width)
        inner_ranges = get_bucket_inner_ranges(bucket_range, script_ranges)
        print(f"    [ # {hex(bucket_range.start)} -> {hex(bucket_range.stop-1)}")
        for ir in inner_ranges:
            print(f"        [ {hex(ir[0].stop-1)}, {sorted(ir[1])}],")
        print("    ],")
    print("]")


if __name__ == "__main__":
    main()
