import json
from pycallisto import chromosphericevaporation as ce


filename = "BLEN7M_20131025_150000_25.fit.gz"
ce_fits = ce.ChromosphericEvaporationFitsFile(filename)
# ce_fits.plot_db_above_background(True)

ce_fits.set_fits_linear_regression()
ce_fits.set_fits_linear_regression_function()

inf_time = 15
sup_time = 15.0479
ce_fits.set_front_velocity(inf_time, sup_time)
with open("LHCP-front-info.txt", "w") as f:
    f.write(json.dumps(ce_fits.get_front()))
    f.write("\n")
