import os
import json
from pycallisto import fitsread

indexes = []
root_dir = 'flares'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'fits_files.json':
            with open(os.path.join(root, file)) as json_file:
                json_str = json_file.read()
                json_data = json.loads(json_str)
                for fits_list in json_data:
                    # Define plot's title
                    title_start = '_'.join(fits_list[0].split('_')[:-1])
                    freq_band = fits_list[-1].split('_')[-1].split('.')[0]
                    title_end = '_'.join([fits_list[-1].split('_')[-2],
                                         freq_band])
                    title = '_'.join([title_start, title_end])

                    # Define plot filename to be saved
                    filename = os.path.join(root, title)

                    # Plot and save the figure
                    print(filename)
                    fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list,
                                                                    title,
                                                                    filename)
