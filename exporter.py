import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w", encoding="utf-8", newline='')
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    print(3)
    writer.writerow(list(job.values()))
    print(4)
  return