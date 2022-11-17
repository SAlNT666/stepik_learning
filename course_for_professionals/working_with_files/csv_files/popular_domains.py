import csv


emails = dict()

with open('data.csv', encoding="utf-8") as file_in:
    file_in.readline()
    for row in csv.reader(file_in):
        email_domain = row[2].split('@')[-1]
        emails[email_domain] = emails.get(email_domain, 0) + 1

with open('domain_usage.csv', 'w', newline='') as file_out:
    writer = csv.writer(file_out)
    writer.writerow(('domain', 'count'))
    for i in sorted(emails.items(), key=lambda x: (x[1], x[0])):
        writer.writerow(i)
