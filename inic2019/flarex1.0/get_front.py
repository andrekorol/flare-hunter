from urldl import download
from pycallisto import chromosphericevaporation as ce
import json

callisto_archives = 'http://soleil80.cs.technik.fhnw.ch/' \
                    'solarradio/data/2002-20yy_Callisto/'
filename = "ROSWELL-NM_20140329_174500_59.fit.gz"

fits_year = filename.split('_')[1][:4]
fits_month = filename.split('_')[1][4:6]
fits_day = filename.split('_')[1][-2:]
fits_url = f'{callisto_archives}/{fits_year}/{fits_month}/' \
           f'{fits_day}/{filename}'
download(fits_url)

ce_fits = ce.ChromosphericEvaporationFitsFile(filename)
ce_fits.plot_db_above_background(True)
ce_fits.set_fits_linear_regression()
ce_fits.set_fits_linear_regression_function()

inf_time = 17.7805
sup_time = 17.8065
ce_fits.set_front_velocity(inf_time, sup_time)
with open("front-info.txt", "w") as f:
    f.write(json.dumps(ce_fits.get_front()))
    f.write("\n")
