import json
from urldl import download
from pycallisto import fitsfile

with open("events.json") as json_file:
    json_str = json_file.read()
    json_data = json.loads(json_str)

callisto_archives = 'http://soleil80.cs.technik.fhnw.ch/' \
                    'solarradio/data/2002-20yy_Callisto/'

for fits_list in json_data:
    for filename in fits_list:
        fits_year = filename.split('_')[1][:4]
        fits_month = filename.split('_')[1][4:6]
        fits_day = filename.split('_')[1][-2:]
        fits_url = f'{callisto_archives}/{fits_year}/{fits_month}/' \
                   f'{fits_day}/{filename}'
        download(fits_url)

    fitsfile.ECallistoFitsFile.plot_fits_files_list(fits_list)
