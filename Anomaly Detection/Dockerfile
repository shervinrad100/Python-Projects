FROM python:3.7.3

COPY solution.py .
COPY Outliers.csv .
COPY requirements.txt .
COPY rollingWindowLSTM/rollingLSTM .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "solution.py"]