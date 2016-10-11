#!/usr/bin/env python
import sys
import folium
import pandas as pd
from config import MAP_PATH, PATH, DC_COORDINATES


def process_result(fname, value):
    json_path = '{}{}.json'.format(PATH['result'], fname)
    psa_data = pd.read_csv('{}{}.csv'.format(PATH['result'], fname))
    psa_processed = psa_data.ix[:, ['PSA', value.upper()]]
    psa_processed.set_index(['PSA'], inplace='True')
    psa_processed.to_json(json_path)
    psa_processed = psa_processed.reset_index()
    return psa_processed, json_path


def create_map(data, json, CENTER=DC_COORDINATES, geojson=MAP_PATH, zoom=11, tileset='Stamen Terrain'):
    crime_map = folium.Map(location=CENTER, zoom_start=zoom, tiles=tileset)
    crime_map.geo_json(geo_path=geojson,
                       data_out='{}{}'.format(PATH['result'], json),
                       data=data,
                       columns=data.columns,
                       key_on='feature.properties.PSA',
                       fill_color='YlOrRd',
                       fill_opacity=0.7,
                       line_opacity=0.2,
                       legend_name='PSA')
    return crime_map


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python gpolicing.py [model_name] [count or relative] [map name]")
        exit()
    (mname, value, mapname) = sys.argv[1:]
    data, json_path = process_result(mname, value)
    crime_map = create_map(data, json_path)
    crime_map.save('{}{}.html'.format(PATH['figs'], mapname))
