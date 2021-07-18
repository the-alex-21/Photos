import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml

# Scikit-Learn provides many helper functions to download popular datasets.MNIST is one of them.
 mnist = fetch_openml('mnist_784', version=1)
