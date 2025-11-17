#!/bin/bash

urls=(
    "https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px"
    "https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/020_kats_tau_102.px"
    "https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/040_kats_tau_104.px"
    "https://trafi2.stat.fi/database/TraFi/Katsastuksen_vikatilastot/050_kats_tau_105.px"
)

mkdir -p ./site

echo "Downloading and processing data..."

for url in "${urls[@]}"; do
    filename=$(basename "$url")
    base_name="${filename%.*}"  # Remove .px extension
    echo "Processing $filename..."
    wget -qO "site/$filename" "$url"
    px2csv-go -px "site/$filename" -csv "site/$base_name.csv"
    uv run 02_process_data.py "site/$base_name.csv" "site/$base_name.parquet"
done

zstd -f -v --rm -T0 -19 --long --output-dir-flat ./site/ site/*.px site/*.csv

echo "All files processed successfully!"
