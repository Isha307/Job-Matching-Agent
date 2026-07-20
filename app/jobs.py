import json

def load_jobs():
    with open("data/jobs.json", "r") as f:
        jobs = json.load(f)
    return jobs