from urldl import download
from pycallisto import fitsfile


callisto_archives = 'http://soleil80.cs.technik.fhnw.ch/' \
                    'solarradio/data/2002-20yy_Callisto/'
filelist = [
    "BLEN7M_20110216_133009_24.fit.gz", "BLEN7M_20110216_134510_24.fit.gz",
    "BLEN7M_20110216_140011_24.fit.gz", "BLEN7M_20110216_141512_24.fit.gz",
    "BLEN7M_20110216_143014_24.fit.gz", "BLEN7M_20110216_144515_24.fit.gz",
    "BLEN7M_20110216_150016_24.fit.gz", "BLEN7M_20110216_151517_24.fit.gz",
    "BLEN7M_20110216_153019_24.fit.gz"]

for filename in filelist:
    fits_year = filename.split('_')[1][:4]
    fits_month = filename.split('_')[1][4:6]
    fits_day = filename.split('_')[1][-2:]
    fits_url = f'{callisto_archives}/{fits_year}/{fits_month}/' \
               f'{fits_day}/{filename}'
    download(fits_url)

title = "Flare classe M1.6, 16/02/2011 (BLEN7M)"
plot_filename = "for_publication"
fitsfile.ECallistoFitsFile.plot_fits_files_list(filelist,
                                                title=title,
                                                plot_filename=plot_filename,
                                                show=True)
