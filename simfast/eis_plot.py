import h5py
import numpy as np
from matplotlib import pyplot as plt


class EISHDF5:
    def __init__(self, data_file, header_file):
        self.hdf5_data = h5py.File(data_file, "r")
        self.hdf5_header = h5py.File(header_file, "r")

    def __del__(self):
        self.hdf5_data.close()
        self.hdf5_header.close()


def plot_eis(data_file, header_file, spectral_window):
    # Read the level-1 data from the spectral window
    hdf5_data = h5py.File(data_file, "r")
    print(hdf5_data)
    window_data = np.array(hdf5_data[f"level1/win{spectral_window}"])
    hdf5_data.close()

    # Get data from the header file
    hdf5_header = h5py.File(header_file, "r")
    # number of arcsec per step in the raster
    (x_scale,) = hdf5_header["pointing/x_scale"]
    # byte array containing date of the observation
    (obs_date,) = hdf5_header["index/date_obs"]
    # decoded observation date
    obs_date_str = obs_date.decode("utf-8")
    # array of wavelengths of a given spectral window
    wavelength = np.array(hdf5_header[f"wavelength/win{spectral_window}"])
    # pre-flight calibration curve for the given data window (RADarCALibration)
    radcal = np.array(hdf5_header[f"radcal/win{spectral_window}_pre"])
    hdf5_header.close()

    raster = np.sum(window_data, axis=2)
    plot_range = np.percentile(raster, (1, 99))
    plot_range = plot_range[1] * np.array([1.0e-2, 1.0])
    scaled = np.log10(np.clip(raster, plot_range[0], plot_range[1]))

    plt.imshow(scaled, origin="lower", aspect="auto", cmap="gray")
    plt.title(obs_date_str)
    plt.show()
    # ix =


data_file = "eis_20131025_143333.data.h5"
header_file = "eis_20131025_140333.head.h5"

# Read the level-1 data from the spectral window 7 (containing Fe XII 195.12 Å)
plot_eis(data_file, header_file, "07")
