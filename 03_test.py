import polars as pl

df = pl.read_parquet('https://autotieto.github.io/katsastustilastot/010_kats_tau_101.parquet')
print(df)
