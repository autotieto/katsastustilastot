import requests

config_url = 'https://trafi2.stat.fi/PXWeb/api/v1/fi/?config'
table_url = 'https://trafi2.stat.fi/PXWeb/api/v1/en/TraFi/Katsastuksen_vikatilastot/010_kats_tau_101.px'
YEAR_VARIABLE = 'Katsastusvuosi'


def save_data(year, data):
    with open(f'./data/01_kats_tau_101_{year}.csv', 'w') as f:
        f.write(data)


def main():
    s = requests.Session()

    data = s.get(table_url).json()
    variables = {v['code']: v for v in data['variables']}
    years = variables[YEAR_VARIABLE]['values']

    for year in years:
        json_data = {
            'query': [
                {
                    'code': YEAR_VARIABLE,
                    'selection': {
                        'filter': 'item',
                        'values': [year]
                    }
                },
            ],
            'response': {'format': 'csv'}
        }
        r = s.post(table_url, json=json_data)
        save_data(year, r.text)

if __name__=='__main__':
    main()
