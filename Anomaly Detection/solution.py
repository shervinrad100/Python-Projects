# univariate lstm example
from keras.models import  load_model
import pandas as pd 
import numpy as np

def getOutliers(df, outlier=True):
    return df[["Date", "Price"]][df.Anomaly == outlier]

if __name__ == "__main__":

    # split a univariate sequence into samples
    def split_sequence(sequence, n_steps):
        X, y = list(), list()
        for i in range(len(sequence)):
            # find the end of this pattern
            end_ix = i + n_steps
            # check if we are beyond the sequence
            if end_ix > len(sequence)-1:
                break
            # gather input and output parts of the pattern
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)

    # define input sequence
    raw = pd.read_csv("Outliers.csv")

    # choose a number of time steps
    n_steps = 7

    # split into samples
    X, y = split_sequence(raw.Price, n_steps)

    # reshape from [samples, timesteps] into [samples, timesteps, features]
    n_features = 1
    Xreshaped= X.reshape((X.shape[0], X.shape[1], n_features))

    # load trained model and fit data
    reconstructed_model = load_model("rollingLSTM")
    yhats = []
    for window in X:
        yhat = reconstructed_model.predict(window.reshape((1, n_steps, n_features)))[0][0]
        yhats.append(yhat)

    # pad the missing predictions and add to dataframe
    yhats[:0] = [np.nan * n_steps]
    raw["Predictions"] = yhats

    # calculate residuals and add to original dataframe
    raw["Residuals"] = raw.Price - raw.Predictions
    # analyse residuals to find outliers
    resiStats = raw.Residuals.describe()
    IQR = resiStats[6] - resiStats[4]
    lowerBound, upperBound = resiStats[4] - 1.5* IQR, resiStats[6] + 1.5* IQR
    # flag anomalies in original dataframe
    raw["Anomaly"] = (raw.Residuals > upperBound) | (raw.Residuals < lowerBound)

    # return outliers to stdout
    print(getOutliers(raw))
    # write to csv
    getOutliers(raw, False).to_csv("cleanedDataset.csv", encoding="utf-8")
