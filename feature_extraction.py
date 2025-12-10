import numpy as np
from scipy.signal import find_peaks
from sklearn.decomposition import PCA

class FeatureExtractor:

    def __init__(self):
        pass

    def detect_peaks(self, y):
        peaks, _ = find_peaks(y, height=0.1, distance=10)
        peak_heights = y[peaks]
        return len(peaks), np.mean(peak_heights), np.max(peak_heights)

    def statistical_features(self, y):
        return np.mean(y), np.std(y), np.max(y), np.min(y)

    def pca_features(self, spectra, n=5):
        pca = PCA(n_components=n)
        return pca.fit_transform(spectra)

    def extract(self, x, y):
        p_count, p_mean, p_max = self.detect_peaks(y)
        mean, std, mx, mn = self.statistical_features(y)

        return np.array([
            p_count, p_mean, p_max,
            mean, std, mx, mn
        ])
