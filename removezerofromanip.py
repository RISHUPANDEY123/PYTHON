import re
ip = "127.0.0.1"
new_ip = re.sub('\.[0]*', ip)
print(new_ip)