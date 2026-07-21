
def score_jobs(jobs, profile):
    score = 0
    for job in jobs:
        matching_skills = set(job["skills"]) & set(profile["skills"])
        score += len(matching_skills) * 1
        if job["location"] == profile["location"]:
            score += 10
        if job["title"] == profile["title"]:
            score += 40
    return score