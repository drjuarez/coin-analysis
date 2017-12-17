import pdb
import pandas as pd

def create_headers(title, periods):
    return [title + '- ' + str(x) + 'days' for x in periods]

def moving_average(dataset, period):
    moving_window = dataset.rolling(period, min_periods=period)
    return moving_window.mean()

def deviation_calc(dataset, mean, period):
    deviations = []
    for row in dataset:
        deviations.append(row - mean)
    return deviations

def run_calculations(data, periods):
    means = {}
    moving_avg_df = pd.DataFrame()
    deviation_df = pd.DataFrame()

    for period in periods:
        means[period] = data[-period:].mean()
        moving_avg_df[period] = moving_average(data, period)
        deviation_df[period] = deviation_calc(data, means[period], period)

    deviation_df.columns = create_headers('Deviation', periods)
    moving_avg_df.columns = create_headers('SMA', periods)
    return pd.concat([moving_avg_df, deviation_df], axis=1)
