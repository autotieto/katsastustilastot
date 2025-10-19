# Traficomin katsastustilastot

```sh
uv run 01_download_data.py \
  --url https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px \
  --file ./site/010_kats_tau_101.parquet

```

```python
import pandas as pd
df = pd.read_parquet('https://autotieto.github.io/katsastustilastot/010_kats_tau_101.parquet')
df.dtypes
```

## Lähteet

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/020_kats_tau_102.px

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/040_kats_tau_104.px

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/050_kats_tau_105.px

## Työkalut

https://pandasdmx.readthedocs.io/en/v1.0/

https://github.com/icane/pyaxis

## Dokumentaatio

https://stat.fi/tup/avoin-data/index.html

https://stat.fi/media/uploads/org/avoindata/pxweb_api-ohje.pdf

http://pxnet2.stat.fi/api1.html
