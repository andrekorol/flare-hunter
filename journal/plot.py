import json
from pycallisto import fitsread


with open("events.json") as json_file:
    json_str = json_file.read()
    json_data = json.loads(json_str)
for fits_list in json_data:
    # Define plot's title
    title = fits_list[0].split('_')[0]

    # Plot and save the figure
    print(title)
    if title == "HUMAIN":
        hours_xticks = ['14:00',  '14:00', '14:12', '14:24', '14:36', '14:48',
                        '15:00', '15:12', '15:24', '15:36', '15:36']
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title,
                                                        title, 'en', 100, 350,
                                                        hours_xticks)

    elif title == "INPE":
        hours_xticks = ['14:00', '14:11', '14:23', '14:35', '14:46', '14:58',
                        '15:10', '15:21', '15:33']
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title,
                                                        title, 'en', 100, 350,
                                                        hours_xticks)

    elif title == "TRIEST":
        hours_xticks = ['14:00', '14:11', '14:23', '14:35', '14:46', '14:58',
                        '15:10', '15:21', '15:33']
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title,
                                                        title, 'en', None, 390,
                                                        hours_xticks)

    elif title == 'SWMC' or title == 'UNAM' or title == 'BIR':
        hours_xticks = ['14:00', '14:11', '14:23', '14:35', '14:46', '14:58',
                        '15:10', '15:21', '15:33']
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title,
                                                        title, 'en', None,
                                                        None, hours_xticks)
    elif title == "BLEN7M":
        hours_xticks = ['14:00', '14:11', '14:23', '14:35', '14:46', '14:58',
                        '15:10', '15:21', '15:33']
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title,
                                                        title, 'en', 100, 420,
                                                        hours_xticks)

    elif title == "OSRA":
        hours_xticks = ['14:00', '14:11', '14:23', '14:35', '14:46', '14:58',
                        '15:10', '15:21', '15:33']
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title,
                                                        title, 'en', None, 420,
                                                        hours_xticks)

    else:
        fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title,
                                                        title, 'en', None,
                                                        None)
