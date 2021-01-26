import argparse
import seaborn as sns
import pandas as pd


def main():
    args = parse_arguments()

    summary_tsv = pd.read_csv(args.input, sep='\t')

    # print(summary_tsv[['Source', 'Tcount', 'Ccount', 'Gcount', 'Acount']])
    # grid = sns.PairGrid(summary_tsv, vars=['Tcount', 'Gcount'], hue='Source')
    # plt = grid.map(sns.scatterplot)

    plt = sns.displot(
        summary_tsv,
        x='GC',
        col='Source',
        col_wrap=args.nbr_cols,
        bins=args.nbr_bins
    )

    plt.fig.suptitle(args.title, y=1.05)


    # grid = sns.FacetGrid(summary_tsv, col='')
    # grid = sns.FacetGrid(summary_tsv, col='Source', col_wrap=3, height=2)
    # plt = grid.map(sns.displot, 'GC')
    # plt = sns.displot(summary_tsv, x='GC', hue='Source', row='Source', multiple='dodge')

    plt.savefig(args.output)

def parse_arguments():
    parser = argparse.ArgumentParser('Provide the needed file paths')
    parser.add_argument('--input', help='Input file', required=True)
    parser.add_argument('--output', help='Output file', required=True)
    parser.add_argument('--title', help='Title for output', default='Seaborn title')
    parser.add_argument('--nbr_cols', help='Number columns', default=3, type=int)
    parser.add_argument('--nbr_bins', help='Number bins', default=20, type=int)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
