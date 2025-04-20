import numpy as np
import pandas as pd

def run_simulation(settings, infl, years, paths):
    np.random.seed(42)
    results = []
    for _ in range(paths):
        value = settings['starting_value']
        path = []
        for y in range(years):
            value *= 1 + np.random.normal(settings['mu'], settings['sigma'])
            value -= settings['spend'] * (1 + infl)**y
            value = max(value, 0)
            path.append(value)
        results.append(path)
    df = pd.DataFrame(results).T
    percentiles = df.quantile([0.05, 0.10, 0.25, 0.5, 0.75, 0.90], axis=1).T
    return percentiles
