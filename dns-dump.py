import sys
import csv
import time
from dns.resolver import Resolver, NoAnswer, NoMetaqueries, NoNameservers

args = sys.argv
if len(args) < 2:
    print("Usage: python dns-dump.py <domain>")
    sys.exit(1)

domain = args[1]

dns_types = []
# read the DNS-types.csv file
with open('DNS-types.csv', 'r') as file:
    data = csv.reader(file, delimiter=';')
    next(data)
    for row in data:
        dns_types.append(row[0])

resolver = Resolver()
results = []
# For each domain, dump the DNS records
for record_type in dns_types:
    print(f"Dumping DNS records for type {record_type}")
    try:
        answers = resolver.query(domain, record_type)
        for a in answers.rrset:
            results.append({"type": record_type, "result": a})
    except NoAnswer as e:
        print(f"No answer for type {record_type}")
    except NoMetaqueries as e:
        print(f"No metaqueries for type {record_type}")
    except NoNameservers as e:
        print(f"All nameservers failed to answer the query for type {record_type}: {e}")
    time.sleep(.1)


resultfile = open(f'dns-dump-{domain}.txt', 'w')
resultfile.write("type;answer\n")
for result in results:
    resultfile.write(f"{result['type']};{result['result']}\n")
resultfile.close()
