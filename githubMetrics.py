import requests
import pandas as pd
import pdb
import utility

r = requests.get('https://api.github.com/repos/omise/omise-go/stats/commit_activity')
activity = r.json()
commits_array = []

for commit in activity:
    temp_commit = {}
    print(commit)
    week = utility.integer_to_datetime(commit["week"])
    time_string = utility.timestamp_for_db(week)
