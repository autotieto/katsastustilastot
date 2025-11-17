import argparse
import polars as pl
import polars.selectors as cs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('in_file', help="input csv file")
    parser.add_argument('out_file', help="output parquet file")
    return parser.parse_args()


def main(args: argparse.Namespace):
    query = (
        pl.scan_csv(
            args.in_file,
            separator=';',
            null_values=['null', '.'],
        )
        .with_columns(
            cs.string().cast(pl.Categorical),
        )
    )
    query.sink_parquet(args.out_file, compression_level=19)


if __name__=='__main__':
    main(parse_args())
