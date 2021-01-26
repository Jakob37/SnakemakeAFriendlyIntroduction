import argparse


def main():

    args = parse_arguments()

    in_fp = args.input
    out_fp = args.output

    line_nbr = 0
    with open(in_fp, 'r') as in_fh, open(out_fp, 'w') as out_fh:
        print('Source\tID\tlength\tGC\tAcount\tTcount\tCcount\tGcount', file=out_fh)
        for line in in_fh:
            line_nbr += 1

            header = line.rstrip()[1:]
            sequence = next(in_fh).rstrip().upper()

            out_string = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                in_fp, header, len(sequence), get_gc(sequence),
                sequence.count('A'),
                sequence.count('T'),
                sequence.count('C'),
                sequence.count('G')
            )
            print(out_string, file=out_fh)

    print('Read {} entries from file {}, writing to file {}'.format(line_nbr, in_fp, out_fp))


def get_gc(nucl_str):
    gc_nbr = nucl_str.count('C') + nucl_str.count('G')
    at_nbr = nucl_str.count('A') + nucl_str.count('T')
    return gc_nbr / (gc_nbr + at_nbr)


def parse_arguments():
    parser = argparse.ArgumentParser('Provide the needed file paths')
    parser.add_argument('--input', help='Input file', required=True)
    parser.add_argument('--output', help='Output file', required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
