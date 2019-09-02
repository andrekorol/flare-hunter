from urldl import download
from pycallisto.fitsfile import ECallistoFitsFile
from pycallisto import chromosphericevaporation as ce
import json


callisto_archives = 'http://soleil80.cs.technik.fhnw.ch/' \
                    'solarradio/data/2002-20yy_Callisto/'
filename = "BLEN7M_20110216_143014_24.fit.gz"

fits_year = filename.split('_')[1][:4]
fits_month = filename.split('_')[1][4:6]
fits_day = filename.split('_')[1][-2:]
fits_url = f'{callisto_archives}/{fits_year}/{fits_month}/' \
           f'{fits_day}/{filename}'
download(fits_url)

ECallistoFitsFile.plot_fits_files_list([filename])

ce_fits = ce.ChromosphericEvaporationFitsFile(filename)
#  ce_fits.plot_db_above_background(True)
ce_fits.set_fits_linear_regression()
ce_fits.set_fits_linear_regression_function()

inf_time = 14.5479
sup_time = 14.6725
ce_fits.set_front_velocity(inf_time, sup_time)
with open("front-info.txt", "w") as f:
    f.write(json.dumps(ce_fits.get_front()))
    f.write("\n")

#  filelist = [
#      "BLEN7M_20110216_133009_24.fit.gz", "BLEN7M_20110216_134510_24.fit.gz",
#      "BLEN7M_20110216_140011_24.fit.gz", "BLEN7M_20110216_141512_24.fit.gz",
#      "BLEN7M_20110216_143014_24.fit.gz", "BLEN7M_20110216_144515_24.fit.gz",
#      "BLEN7M_20110216_150016_24.fit.gz", "BLEN7M_20110216_151517_24.fit.gz",
#      "BLEN7M_20110216_153019_24.fit.gz"]
#  for filename in filelist:
#      fits_year = filename.split('_')[1][:4]
#      fits_month = filename.split('_')[1][4:6]
#      fits_day = filename.split('_')[1][-2:]
#      fits_url = f'{callisto_archives}/{fits_year}/{fits_month}/' \
#                 f'{fits_day}/{filename}'
#      download(fits_url)

#  ECallistoFitsFile.plot_fits_files_list(filelist, show=True)

#  inf_time = 305.648
#  inf_time = 466.507
#  lin_reg_fn = ECallistoFitsFile.fits_list_linear_regression(filelist)
# TODO model doesn't work for a list of files...
#  dummy_file = ce.ChromosphericEvaporationFitsFile(filelist[0])
#  dummy_file.set_front_velocity(inf_time, sup_time, lin_reg_fn)
#  with open("front-info.txt", "w") as f:
#      f.write(json.dumps(dummy_file.get_front()))
#      f.write("\n")
