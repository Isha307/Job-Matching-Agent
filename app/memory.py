import json

def save_matching_jobs(jobs):
    if jobs >= 70:
        with open("data/matching_jobs.json", "w") as f:
            json.dump(jobs, f)
            print(f"Saved matching jobs to data/matching_jobs.json")