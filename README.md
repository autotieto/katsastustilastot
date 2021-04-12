# Traficomin katsastustilastot

```sh
pip install --user --upgrade pandas pyarrow
```

```python
import pandas as pd
df = pd.read_parquet('https://autotieto.github.io/katsastustilastot/010_kats_tau_101.parquet')
df.dtypes
```

## Lähteet

https://trafi2.stat.fi/PXWeb/pxweb/fi/TraFi/TraFi__Katsastuksen_vikatilastot/?tablelist=true

https://trafi2.stat.fi/PXWeb/pxweb/fi/TraFi/TraFi__Katsastuksen_vikatilastot/010_kats_tau_101.px/

https://trafi2.stat.fi/PXWeb/pxweb/fi/TraFi/TraFi__Katsastuksen_vikatilastot/020_kats_tau_102.px/

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px

https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/020_kats_tau_102.px

## Työkalut

https://pandasdmx.readthedocs.io/en/v1.0/

https://github.com/icane/pyaxis

## Dokumentaatio

http://pxnet2.stat.fi/api1.html

http://www.stat.fi/static/media/uploads/org_en/avoindata/px-web_api-help.pdf

https://www.scb.se/en/services/oppna-data/api-for-the-statistical-database/

https://www.scb.se/contentassets/79c32c72783a4f67b202ad3189f921b9/api-description.pdf
