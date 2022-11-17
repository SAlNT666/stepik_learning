import csv
import json
from datetime import datetime


with open('exam_results.csv', encoding='utf8') as jf_in:
    results = list(csv.DictReader(jf_in))

best_scores = dict()
for row in results:
    if best_scores.get(row['email'], {}).get('best_score', 0) < int(row['score']) or\
       (best_scores.get(row['email'], {}).get('best_score', 0) == int(row['score']) and
        datetime.fromisoformat(best_scores[row['email']]['date_and_time']) < datetime.fromisoformat(row['date_and_time'])):
        row['best_score'] = int(row.pop('score'))
        best_scores[row['email']] = row

with open('best_scores.json', 'w', encoding='utf8') as jf_out:
    json.dump([best_scores[i] for i in sorted(best_scores)], jf_out, ensure_ascii=False, indent=3)
