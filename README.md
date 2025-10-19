# Traficomin katsastustilastot

https://autotieto.github.io/katsastustilastot/010_kats_tau_101.parquet   
https://autotieto.github.io/katsastustilastot/010_kats_tau_101.px.zst   
https://autotieto.github.io/katsastustilastot/010_kats_tau_101.csv.zst

https://autotieto.github.io/katsastustilastot/020_kats_tau_102.parquet   
https://autotieto.github.io/katsastustilastot/020_kats_tau_102.px.zst   
https://autotieto.github.io/katsastustilastot/020_kats_tau_102.csv.zst

https://autotieto.github.io/katsastustilastot/040_kats_tau_104.parquet   
https://autotieto.github.io/katsastustilastot/040_kats_tau_104.px.zst   
https://autotieto.github.io/katsastustilastot/040_kats_tau_104.csv.zst

https://autotieto.github.io/katsastustilastot/050_kats_tau_105.parquet   
https://autotieto.github.io/katsastustilastot/050_kats_tau_105.px.zst   
https://autotieto.github.io/katsastustilastot/050_kats_tau_105.csv.zst


```python
import polars as pl

df = pl.read_parquet('https://autotieto.github.io/katsastustilastot/010_kats_tau_101.parquet')
df.dtypes

df = pl.read_csv('https://autotieto.github.io/katsastustilastot/010_kats_tau_101.csv.zst', separator=';')
df.dtypes
```

## Lähteet

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/020_kats_tau_102.px

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/040_kats_tau_104.px

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/050_kats_tau_105.px

## Työkalut

https://github.com/mikaelhg/px2csv-go

https://mise.jdx.dev/

https://github.com/astral-sh/uv

https://pola.rs/

https://parquet.apache.org/

## Dokumentaatio

https://stat.fi/tup/avoin-data/index.html

https://stat.fi/media/uploads/org/avoindata/pxweb_api-ohje.pdf

https://pxdata.stat.fi/api1.html

