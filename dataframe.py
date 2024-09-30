# from google.cloud import bigquery
# import os

# # make sure to put the json file in the same directory as this script
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'big-query-creds.json'

# client = bigquery.Client()

# query = """
# SELECT subject_id, hadm_id, gender, age, icu_los, diagnosis, heart_rate, blood_pressure
# FROM `physionet-data.mimiciii_clinical.icustays`
# WHERE diagnosis = 'Sepsis';
# """

# query_job = client.query(query)
# df = query_job.to_dataframe()

# print(df.head())


from google.cloud import bigquery

client = bigquery.Client()

query = """
SELECT name, year, number
FROM `bigquery-public-data.usa_names.usa_1910_2013`
WHERE state = 'TX'
LIMIT 10
"""

query_job = client.query(query)
rows = query_job.result()

for row in rows:
    print(f"Name: {row.name}, Year: {row.year}, Number: {row.number}")
