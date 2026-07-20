from app.jobs import load_jobs

jobs = load_jobs()
print(f"Loaded {len(jobs)} jobs")