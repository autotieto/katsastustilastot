#!/usr/bin/python3

import argparse
from pyaxis import pyaxis
import pandas as pd


URL = 'https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px'


def parse_args():
    parser = argparse.ArgumentParser(description='Download data.')
    parser.add_argument('--url', default=URL)
    parser.add_argument('--file', default='./data/010_kats_tau_101.parquet')
    return parser.parse_args()


def main(args):
    px = pyaxis.parse(args.url, encoding='windows-1252')
    df = px['DATA']
    del px
    for k in df.keys():
        if k in ['Katsastusvuosi']:
            df[k] = df[k].astype('int64')
        elif k in ['DATA']:
            df[k] = df[k]
        else:
            df[k] = df[k].astype('category')
    df.to_parquet(args.file, compression='brotli')


if __name__=='__main__':
    main(parse_args())
