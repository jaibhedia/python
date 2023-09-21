import re

phone_regex = re.compile(r'\+\d{12}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')
date_regex = re.compile(r'[0-9]+-[0-9]+-[0-9]{3,}')

# Open the input file (EXAMPLE.TXT in this case)
with open('EXAMPLE.TXT', 'r') as f:
    for line in f:
        line = line.strip()  # Remove leading/trailing whitespace
        matches = phone_regex.findall(line)
        match_email = email_regex.findall(line)
        match_date = date_regex.findall(line)

        # Join the matches into a single string separated by tabs
        phone_str = "\t".join(matches)
        email_str = "\t".join(match_email)
        
        print(f"{line}\t{email_str}\t{phone_str}")

        for date in match_date:
            print(f"\t\t\t{date}")
