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
    fitsread.ECallistoFitsFile.plot_fits_files_list(fits_list, title,
                                                    title, 'en', None,
                                                    None)
