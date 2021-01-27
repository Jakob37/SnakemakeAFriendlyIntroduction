#!/usr/bin/env python3

import re
import argparse


def main():
    args = parse_arguments()

    in_file = args.input
    out_file = args.output

    line_nbr = 0

    with open(in_file, 'r') as in_fh, open(out_file, 'w') as out_fh:
        for line in in_fh:
            line_nbr += 1
            if line_nbr > args.max_entries * 4:
                # print('Reaching max-number of entries, stopping...')
                break
            line = line.rstrip()

            if line_nbr % 4 == 1:
                # Replace leading @-signs with the fasta > sign
                line = re.sub("^@", ">", line)
                # Trim text trailing white-spaces in the header
                line = re.sub(" .*", "", line)

            if line_nbr % 4 in [1,2]:
                print(line, file=out_fh)

    # print('Written {} lines from file {} to file {}'.format(line_nbr, in_file, out_file))


def parse_arguments():
    parser = argparse.ArgumentParser('Provide the needed file paths')
    parser.add_argument('--input', help='Input file', required=True)
    parser.add_argument('--output', help='Output file', required=True)
    parser.add_argument('--max_entries', help='Specify maximum number of used sequences', type=int, default=float('inf'))
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
