from urldl import download
from pycallisto import fitsfile


callisto_archives = 'http://soleil80.cs.technik.fhnw.ch/' \
                    'solarradio/data/2002-20yy_Callisto/'

filename = "OOTY_20140824_044459_59.fit.gz"
fits_year = filename.split('_')[1][:4]
fits_month = filename.split('_')[1][4:6]
fits_day = filename.split('_')[1][-2:]
fits_url = f'{callisto_archives}/{fits_year}/{fits_month}/' \
           f'{fits_day}/{filename}'
download(fits_url)
fits_file = fitsfile.ECallistoFitsFile(filename)
fits_file.plot_db_above_background(True)
start_time = 4.90896
start_freq = 300
end_freq = 400
title = "Circular-Ribbon Flare classe C5.5, 24/08/2014 (OOTY)"
plot_filename = "for_publication"
fitsfile.ECallistoFitsFile.plot_fits_files_list([filename],
                                                title=title,
                                                plot_filename=plot_filename,
                                                start_time=start_time,
                                                start_freq=start_freq,
                                                end_freq=end_freq)
