import time

from pycallisto import fitsfile
from urldl import download

callisto_archives = "http://soleil80.cs.technik.fhnw.ch/" \
                    "solarradio/data/2002-20yy_Callisto/"
date_xpath = "2011/08/09/"
filename = "BLEN7M_20110809_083004_24.fit.gz"
start = time.time()
download(callisto_archives + date_xpath + filename)
fitsfile.ECallistoFitsFile.plot_fits_files_list([filename], lang="pt")
print("Executed in {:.2f} seconds".format(time.time() - start))
