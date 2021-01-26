import argparse


def main():
    args = parse_arguments()
    concatenate_files(args.inputs, args.output)


def concatenate_files(in_files, out_file):
    with open(out_file, 'w') as out_filehandle:
        is_first_file = True
        for input_filepath in in_files:
            line_nbr = 0
            with open(input_filepath, 'r') as in_filehandle:
                for line in in_filehandle:
                    line_nbr += 1

                    # Skip header if not first file
                    if line_nbr == 1:
                        if not is_first_file:
                            continue
                        else:
                            is_first_file = False

                    line = line.rstrip()
                    print(line, file=out_filehandle)


def parse_arguments():
    parser = argparse.ArgumentParser('Provide the needed file paths')
    parser.add_argument('--inputs', nargs='+', help='Input files', required=True)
    parser.add_argument('--output', help='Output file', required=True)
    parser.add_argument('--db', help='Provide additional information')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
