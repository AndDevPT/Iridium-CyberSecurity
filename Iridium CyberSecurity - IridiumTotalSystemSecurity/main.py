import threading
import os
from cryptography.fernet import Fernet

def MalwareScanner():
    print("Iridium CyberSecurity MalwareScanner ALL RIGHTS RESERVED COLLABORATION WITH MICROSOFT MRT (MALWARE REMOVAL TOOL) ")

    while True:
        i = input("""What do you wish to do?
        (1) Scan your computer for malware or malicious software
        (2) Help
        (3) Exit this program \n""")

        if i == "1":
            input("Enter to start the scanning process. Remember to activate this script in admin mode")
            os.system("C:\\Windows\\System32\\MRT.exe")
        elif i == "2":
            print("Watch our youtube tutorial!")
            input("Enter to restart the program")
        elif i == "3":
            o = input("""Are you sure?
            (1) Yes!
            (2) No.""")

            if o == "1":
                exit()
            elif o == "2":
                input("Enter to restart the program")
            else:
                print("Invalid Option!")
                input("Enter when you are ready to restart the program")

def PasswordManager():
    print("Iridium CyberSecurity PasswordManager ALL RIGHTS RESERVED")

    from cryptography.fernet import Fernet

    class PasswordManager:

        def __init__(self):
            self.key = None
            self.password_file = 'mypasswords.pass'
            self.password_dict = {}

        def create_key(self, path):
            self.key = Fernet.generate_key()
            with open(path, 'wb') as f:
                f.write(self.key)

        def load_key(self, path):
            with open(path, 'rb') as f:
                self.key = f.read()

        def create_password_file(self, path, initial_values=None):
            self.password_file = path

            if initial_values is not None:
                for key, values in initial_values.items():
                    self.add_password(key, values)

        def load_password_file(self, path):
            self.password_file = path

            with open(path, 'r') as f:
                for line in f:
                    site, encrypted = line.split(":")
                    self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

        def add_password(self, site, password):
            self.password_dict[site] = password

            if self.password_file is not None:
                with open(self.password_file, 'a+') as f:
                    encrypted = Fernet(self.key).encrypt(password.encode())
                    f.write(site + ":"  + encrypted.decode() + "\n")

        def get_password(self, site):
            return self.password_dict[site]

    def main():
        password = {
            "facebook": "12345",
            "google": "345"
        }

        pm = PasswordManager()

        print("""What do you wish to do?
        (1) Create a new key
        (2) Load an existing key
        (3) Create new a new pass
        (4) Load an existing password
        (5) Add a new password
        (6) Get a password
        (q) Quit
        INFO: You can use the Iridium PasswordGenerator first to generate secure passwords
        and to give them a name. You can then secure your passwords here! Just remember to delete
        the passwords after saving them in this password manager from the password_log txt file
        If you need help with the password manager watch our tutorial on youtube!""")

        done = False

        while not done:
            choice = input("Enter your choice: ")
            if choice == "1":
                path = input("Enter path: ")
                pm.create_key(path)
            elif choice == "2":
                path = input("Enter path: ")
                pm.load_key(path)
            elif choice == "3":
                path = input("Enter Path: ")
                pm.create_password_file(path, password)
            elif choice == "4":
                path = input("Enter path: ")
                pm.load_password_file(path)
            elif choice == "5":
                site = input("Enter the site: ")
                password = input("Enter the password: ")
                pm.add_password(site, password)
            elif choice == "6":
                site = input("What site do you want: ")
                print(f"Password for {site} is {pm.get_password(site)}")
            elif choice == "q":
                done = True
                print("Bye")
                input("Enter to restart the program")
            else:
                print("Invalid Option!")

    if __name__ == "__main__":
        main()



def disk_encryptor():
    print("Iridium CyberSecurity Disk_Encryptor ALL RIGHTS RESERVED")

    escolha1 = input("""What do you wish to do?
    (1) Encrypt a disk
    (2) Decrypt a disk
    (3) Terms and conditions / help
    (4) Exit the program""")

    if escolha1 == "1":
        print("Encrypt Disk")


        def generate_key():
            return Fernet.generate_key()

        def encrypt_file(file_path, cipher_suite):
            with open(file_path, 'rb') as file:
                file_data = file.read()

            encrypted_data = cipher_suite.encrypt(file_data)

            with open(file_path, 'wb') as file:
                file.write(encrypted_data)

        def encrypt_directory(directory_path, cipher_suite):
            for root, _, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    encrypt_file(file_path, cipher_suite)

        # Generate encryption key
        encryption_key = generate_key()

        # Initialize the Fernet cipher object using the encryption key
        cipher_suite = Fernet(encryption_key)

        # Search for the disk directory dynamically
        disk_directory = '/'
        found_disk = False

        # Search for a specific file or directory that exists on the disk
        target_file_or_directory = input("Choose the disk that you want to encrypt")

        while not found_disk:
            for root, _, files in os.walk(disk_directory):
                if target_file_or_directory in files or target_file_or_directory in os.listdir(root):
                    found_disk = True
                    break
            else:
                # Move to the parent directory
                disk_directory = os.path.dirname(disk_directory)

        # Encrypt the files in the disk directory
        encrypt_directory(disk_directory, cipher_suite)

        print("Folder or disk Decrypted")
        input("Enter to restart the program")

    elif escolha1 == "2":
        print("Decrypt Function")

        def decrypt_file(file_path, cipher_suite):
            with open(file_path, 'rb') as file:
                file_data = file.read()

            decrypted_data = cipher_suite.decrypt(file_data)

            with open(file_path, 'wb') as file:
                file.write(decrypted_data)

            def decrypt_directory(directory_path, cipher_suite):
                for root, _, files in os.walk(directory_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        decrypt_file(file_path, cipher_suite)


                    # Generate encryption key
                    decryption_key = generate_key()

                    # Initialize the Fernet cipher object using the encryption key
                    cipher_suite = Fernet(decryption_key)

                    # Search for the disk directory dynamically
                    disk_directory = '/'
                    found_disk = False

                    # Search for a specific file or directory that exists on the disk
                    target_file_or_directory = input("Choose the disk that you want to decrypt")

                    while not found_disk:
                        for root, _, files in os.walk(disk_directory):
                            if target_file_or_directory in files or target_file_or_directory in os.listdir(root):
                                found_disk = True
                                break
                        else:
                            # Move to the parent directory
                            disk_directory = os.path.dirname(disk_directory)

                    # Encrypt the files in the disk directory
                    encrypt_directory(disk_directory, cipher_suite)

                    print("Folder or disk Decrypted")
                    input("Enter to restart the program")


    elif escolha1 == "3":
        print("""Terms and conditions: By using this part of the program , i the
        user of this software understand that i am the one responsible for any
         data lost and i hereby lose my right to sue Iridium """)
        b = input("""Enter to see the guide on this part of the software""")

        if b == "":
            print("URL DO SITE")
        else:
            print("xixi")

    elif escolha1 == "4":
        input("Restarting Enter to end the process")
        exit()
    else:
        print("Invalid Option! THE PROGRAM WILL RESTART")
        input("Enter to restart")


def VPN ():
    print("Iridium CyberSecurity VPN ALL RIGHTS RESERVED")

    import socket

    def main():
        # Server configuration
        server_ip = '0.0.0.0'
        server_port = 12345

        # Create a server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, server_port))
        server_socket.listen(5)
        print(f"Server listening on {server_ip}:{server_port}")

        while True:
            client_socket, client_addr = server_socket.accept()
            print(f"Accepted connection from {client_addr}")

            # Create a proxy thread to handle the client's traffic
            proxy_thread = ProxyThread(client_socket)
            proxy_thread.start()

    class ProxyThread(threading.Thread):
        def __init__(self, client_socket):
            super().__init__()
            self.client_socket = client_socket

        def run(self):
            while True:
                # Receive data from the client
                client_data = self.client_socket.recv(4096)
                if not client_data:
                    break

                # Simulate processing (e.g., you can add encryption/decryption here)
                server_data = process_data(client_data)

                # Send the processed data to the server
                self.client_socket.send(server_data)

            self.client_socket.close()

    def process_data(data):
        # Simulated processing (in a real VPN, this would involve encryption)
        return data

    if __name__ == '__main__':
        main()


def passwordGen():
    print("Iridium CyberSecurity Password Generator ALL RIGHTS RESERVED")
    lenght = int(input("how many caracters long do you want your password?"))

    input("ENTER to generate the password.")

    import random

    lower_case = "abcdefghijklmnopqrstuvwxyv"
    upper_case = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "@£?#*+\/%"

    ans = lower_case + upper_case + number + symbol

    password: str = "".join(random.sample(ans, lenght))

    print("Your generated password is:", password)
    print("REMINDER: You can store your generated passwords in our included password manager! The password manager encrypts and stores your passwords for extra security!")
    print("Now lets store it in a txt file since you can easily forget and things like that.")

    report = open('Password_Log.txt', 'a')

    report.write(input(
        "what name do you want to your password to have? (usefull for knowing if its for a email etc...)") + " /// " + password)
    report.write('\n')

    report.close()

    print("check 'Password_Log.txt' to see your new generated password")
    while 1 == 1:
        generate_another = input("""do you wish to generate another password?
            (1) Yes 
            (2) Restart The program""").lower()

        if generate_another == "1":
            passwordGen()
        elif generate_another == "2":
            exit()
        else:
            print("Invalid option!")


print("Welcome to the Iridium CyberSecurity TotalSystemSecurity")

while 1==1:
    Menu = input("""What do you wish to do?
    (1) Use the Iridium Password Generator
    (2) Use the Iridium Virtual private Network (VPN)
    (3) Use the Iridium DiskEncryptor
    (4) Use the Iridium Password Manager
    (5) Use the Iridium Malware scanner
    (6) Get to the Iridium WebSite
    (7) Links / Help
    (8) See the current version of this software
    (9) See the next Updates
    (10) Upgrade to an Iridium Pro account
    (11) Create an Iridium Account
    (12) About
    (13) Support
    (14) Exit this Program \n""")

    if Menu == "1":
        passwordGen()
    elif Menu == "2":
        VPN()
    elif Menu == "3":
        disk_encryptor()
    elif Menu == "4":
        PasswordManager()
    elif Menu == "5":
        MalwareScanner()
    elif Menu == "6":
        print("Website currently not available since its in development")
        input("Enter to go to the main option hub")
    elif Menu == "7":
        print("Our discord: https://discord.gg/G3CmFgGy9D ")
        input("Enter to go to the main option hub")
    elif Menu == "8":
        print("Version 0.1 (ALPHA TEST) ")
        input("Enter to go to the main option hub")
    elif Menu == "9":
        print("Update 0.2 : Password manager development completion")
        input("Entre to go to the main option hub")
    elif Menu == "10":
        print("Not ready yet!")
        input("Enter to go to the main option hub")
    elif Menu == "11":
        print("Not ready yet!")
        input("Enter when you are ready to go to the main option hub")
    elif Menu == "12":
        print("""This is a open source program developed by Iridium CyberSecurity.
        This program has no lucrative intentions and the only ones that i has
        is to help people in a daily basis against cyber threats for free.
        This program is only been developed by only one dev - André da Silva João
         Who lives in portugal.""")

        input("Enter when you are ready to go to the main option menu")

    elif Menu == "13":
        print("""Please contact one of our support contacts:
         Phone: +351 927719945
         email: al31883@agr-tc.pt""")
        input("Enter to go to the main option menu")

    elif Menu == "14":
        n = input("""Are you sure that you want to quit
        (1) Yes
        (2) No""")

        if n == "1":
            exit()

        elif n == "2":
            input("Enter yo go to the main option hub")

#This is a note for the guys who tried to brute force this software: Good Job!

