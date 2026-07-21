from app.jobs import load_jobs
from app.scorer import score_jobs
from app.memory import save_matching_jobs
import json

jobs = load_jobs()
with open("data/user_profile.json", "r") as f:
    profile = json.load(f)

score_jobs = score_jobs(jobs, profile)
print(f"Loaded {len(jobs)} jobs")
save_matching_jobs(score_jobs)
