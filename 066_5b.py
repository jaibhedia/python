import re
phone_regex=re.compile(r'\+\d{12}')
email_regex=re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')
date_regex=re.compile(r'[0-9]+-[0-9]+-[0-9]{3,}')
with open('kar.txt', 'r') as f:
    for line in f:
        matches=phone_regex.findall(line)
        match_email=email_regex.findall(line)
        match_date=date_regex.findall(line)
        for phone,email in zip(matches,match_email):
            print(phone,email)
        for dates in zip(match_date):
            print(match_date)
