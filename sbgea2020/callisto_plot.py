from urldl import download
from pycallisto import fitsfile


flare_x17_band_24_files = [
    # "BLEN7M_20131025_074322_24.fit.gz",
    "BLEN7M_20131025_075822_24.fit.gz",
    # "BLEN7M_20131025_081322_24.fit.gz"
]

flare_x17_band_25_files = [
    # "BLEN7M_20131025_074500_25.fit.gz",
    "BLEN7M_20131025_080000_25.fit.gz",
    # "BLEN7M_20131025_081500_25.fit.gz"
]

flare_x21_band_24_files = [
    "BLEN7M_20131025_150438_24.fit.gz"
]

flare_x21_band_25_files = [
    # "BLEN7M_20131025_144501_25.fit.gz",
    "BLEN7M_20131025_150000_25.fit.gz",
]

plot_list = [flare_x17_band_24_files, flare_x17_band_25_files,
             flare_x21_band_24_files, flare_x21_band_25_files]

# callisto_archives = "http://soleil80.cs.technik.fhnw.ch/" \
#                     "solarradio/data/2002-20yy_Callisto/"

# date_xpath = "2013/10/25/"

# for fits_list in plot_list:
#     for filename in fits_list:
#         download(callisto_archives + date_xpath + filename)

date_str = "October 25th, 2013"
location = "BLEN7M"
instrument = "Phoenix-4"
titles = [
    f"Flare X1.7 - {date_str} ({location}) ({instrument} RHCP)",
    f"Flare X1.7 - {date_str} ({location}) ({instrument} LHCP)",
    f"Flare X2.1 - {date_str} ({location}) ({instrument} RHCP)",
    f"Flare X2.1 - {date_str} ({location}) ({instrument} LHCP)"
]

for fits_list in plot_list:
    title = titles.pop(0)
    fitsfile.ECallistoFitsFile.plot_fits_files_list(fits_list, title, title)
