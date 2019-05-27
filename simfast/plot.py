import json
from pycallisto import fitsread


with open("events.json") as json_file:
    json_str = json_file.read()
    json_data = json.loads(json_str)
for fits_list in json_data:
    if fits_list[0].split('_')[0] == "BLEN7M":
        title_start = '_'.join(fits_list[0].split('_')[:-1])
        freq_band = fits_list[-1].split('_')[-1].split('.')[0]
        title_end = '_'.join([fits_list[-1].split('_')[-2],
                              freq_band])
        title = '_'.join([title_start, title_end])
        hours_xticks = ['13:30', '13:57', '14:24', '14:51', '15:18']
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title, title,
                                                        'en', None, None,
                                                        hours_xticks)
    else:
        title_start = '_'.join(fits_list[0].split('_')[:-1])
        freq_band = fits_list[-1].split('_')[-1].split('.')[0]
        title_end = '_'.join([fits_list[-1].split('_')[-2],
                              freq_band])
        title = '_'.join([title_start, title_end])
        hours_xticks = ['17:30', '17:36', '17:42', '17:48', '17:54', '18:00']
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title, title,
                                                        'en', None, None,
                                                        hours_xticks)
