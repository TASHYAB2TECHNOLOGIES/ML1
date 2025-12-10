import numpy as np
import pandas as pd
from scipy.signal import savgol_filter, find_peaks

class SpectralPreprocessor:

    def __init__(self):
        pass

    def baseline_correction(self, y):
        x = np.arange(len(y))
        coeffs = np.polyfit(x, y, 3)
        baseline = np.polyval(coeffs, x)
        return y - baseline

    def smooth_signal(self, y, window=15, poly=3):
        return savgol_filter(y, window_length=window, polyorder=poly)

    def normalize(self, y):
        return (y - min(y)) / (max(y) - min(y))

    def preprocess(self, df):
        x = df['wavelength'].values
        y = df['absorbance'].values

        y = self.baseline_correction(y)
        y = self.smooth_signal(y)
        y = self.normalize(y)

        return x, y
