# How to run

## docker
To grab image from the repo and run a container instance run the following:

    `docker run -it --name main-container shervinrad100/outlier-detection-test /bin/bash`

Downloading and extracting the image may take a few min depending on your internet and system spec as it's 2.8GB.
Once you have attached the container to your CLI run:

    `source run_solution.sh`

This will set up a python virtual environment on the container and install all the python packages needed. 
It will then run the solution.py script and output the anomalous data to stdout and write a csv of the cleaned dataset. 
To read the cleanedDataset.csv run:

    `cat cleanedDataset.csv`

You can also copy this file to your directory using:

    `docker cp main-container:"cleanedDataset.csv" .`

If you did not name your container find the containerID by running `docker container  ls -a` in another shell and replace  
"main-container" with that ID. 

## windows
Assuming you have python3 installed, simply run the "run_solution.bat". 
I have put pauses in the script so you can see what is happening at each step, just keep pressing enter until you get the 
    final output and see cleanedDataset.csv created in the directory. 

## Linux/MacOS
Similar to windows, if you have python3 installed, run the script "run_solution.sh". 


# Choosing the model

Probability Based Approaches: generally look at standard deviation and mean and for that it uses forawrd bias because it 
    looks at the data as a whole. 


Forecasting Based Approaches: we forecast the series and evaluate the residuals. If the residuals are exceptionally high 
    then they must be anomalies (assuming that the model is accurately fit)
Had the option to use:
    ARIMA - There was no autocorrelation in the dataset and we had a breakpoint which made this very cumbersome. 
    LSTM - easy to implement and very accurate forecasting tool 
Other solutions like fbprophet is also very accurate and efficient but the module is no longer available in windows which 
    causes compatibility issues so we will not use that. 


Clustering Algorithms: 
Isolation Forest - also very effective but the downside is that you need to know the percentage of anomalies that is in 
    your dataset.
Also there are other issues such as bias when branching takes place and so when evaluating the effectiveness of the model 
    in an anomally score heat map, there are regions where the algorithm ignores anomalies. To tackle this we must use 
    Extended Isolation Forest which I did not have time to do unfortunately. 
Finally, isolation forest also has a forward bias in the training set due to the optimisation of the parameters.  


# The model

I have set up a 5 day rolling window which uses the past 5 days to forecast the next data point. It optimises the network 
    weights based only on previous data and therefore does not have forward bias unlike isolation forest. Once the rolling 
    window reaches the end of the series, we then calculate the residuals between the predictions and the observations and 
    remove points whose residuals are outside 1.5 times the Inter Quartile Range (IQR). 
Disadvantage of the rolling window method is that it has missed the anomalies in the initial period. But the only way we can 
    tell that there are anomalies at the start of the series is using forward bias. 
(You can have a look at the steps in the notebook in the rollingWindowLSTM folder)

# Evaluation

The model did not perform well when there were huge spikes in the data or where there was a breakpoint. This reduced the 
    sensitivity to 67% (although the anomalies in the first window has a direct effect on this number as well).
Total of 10 false positives were shown because the model based its predictions on anomalous data. To tackle this we can 
    remove anomaly before predicting the next points by evaluating the distance from mean and observation (this method highly 
    depends on the window size).
Despite missing the first few anomalies and some false negatives, the model can be generally accepted for this dataset with 
    good specifity of 98.3% (finding 98% of anomalies), discovered most of the anomalies present in the dataset