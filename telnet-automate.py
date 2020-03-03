import getpass
import sys
import telnetlib

HOST = "10.24.1.1"
PORT = 23
user = input("Enter your remote account: ")
password = getpass.getpass()

##### Practical Stuff

cursor = ">0000"
F1 = "\0x70"

##### Navigation Options

mainMenu = ['\033[14~','\033[14~','\033[14~','\033[14~']
clearAlertsKeySeq = ['11','6','7']
clearAction = ['\r','C\r','C','\0x70'] 

class backOffice:

    def __init__(self):
        self.tn = telnetlib.Telnet(HOST, PORT)
        self.tn.set_debuglevel(100)

    def login(self):
        self.tn.read_until(b"login: ")
        self.tn.write(user.encode('ascii') + b"\n")
        if password:
            self.tn.read_until(b"Password: ")
            self.tn.write(password.encode('ascii') + b"\n")
        self.tn.read_until(b"QUIT")
        print("Connected")

    def disconnect(self):
        #tn.read_until(b"Transport")
        self.tn.write(b"q\n")
        #print(tn.read_all().decode('ascii'))
        self.tn.close()
        print("Disconnected")
    
    def removeAlert(self):
        print("Removing Alert")
        try:
            response = self.tn.read_until(cursor.encode('ascii'), timeout=15)    #(b"\x3E0000")
        except EOFError as e:
            pass
        else:
            if cursor.encode('ascii') in response:
                self.tn.write(b"\r")
                self.tn.read_until(b"Action:", timeout=15)
                self.tn.write(b"C\r")
                self.tn.read_until(b"Reason:", timeout=15)
                self.tn.write(b"C")
                self.tn.read_until(b"Insert", timeout=15)
                self.tn.write(b"\x70")
                self.tn.read_until(cursor.encode('ascii'), timeout=15)
            else:
                pass

    def navigate(self):
        print("Navigating")
        for i in clearAlertsKeySeq:
            self.tn.write(i.encode('ascii'))
        pass


a = backOffice()
a.login()
a.navigate()
a.removeAlert()
a.disconnect()

'''
0x0D	Enter Key
0x70	F1 key
0x71	F2 key
0x72	F3 key
0x73	F4 key
0x74	F5 key

'''