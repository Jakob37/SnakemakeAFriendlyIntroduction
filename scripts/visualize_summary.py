import argparse
import seaborn as sns
import pandas as pd


def main():
    args = parse_arguments()

    summary_tsv = pd.read_csv(args.input, sep='\t')
    plt = sns.displot(summary_tsv, x='GC', hue='Source')
    plt.savefig(args.output)

def parse_arguments():
    parser = argparse.ArgumentParser('Provide the needed file paths')
    parser.add_argument('--input', help='Input file', required=True)
    parser.add_argument('--output', help='Output file', required=True)
    parser.add_argument('--title', help='Title for output', default='Seaborn chart')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
