from urllib.request import urlopen
import smtplib
import json


with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
#                 """To: dmytro.slobodenyuk@gmail.com
#                 From: soothsayer@example.org
#
#                 Beware the Ides of March.
#                 """)
# server.quit()