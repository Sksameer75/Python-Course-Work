'''
class Whatsappv1:
    def message(self):
        print("You can send message")

class Whatsappv2(Whatsappv1):
    def status(self):
        print("you can upload status")

class Whatsappv3(Whatsappv2):
    def groups(self):
        print("you can create group and talk with multiple people at same time")

class Whatsappv4:
    def community(self):
        print("you can multiple groups")

class Whatsappv5(Whatsappv4,Whatsappv3,Whatsappv2):
    def channels(self):
        print("you can posy regulary with huge crowd")

sameer = Whatsappv3()
sameer.message()
sameer.status()
sameer.groups()

narayana = Whatsappv3()
narayana.message()
narayana.status()
narayana.groups()

sailesh = Whatsappv5()
sailesh.message()
sailesh.status()
sailesh.groups()
sailesh.community()
sailesh.channels()

'''
class Whatsappv1:
    def message(self):
        print("You can send message")

class Whatsappv2(Whatsappv1):
    def status(self):
        print("you can upload status")

class Whatsappv3(Whatsappv1):
    def groups(self):
        print("you can create group and talk with multiple people at same time")

class Whatsappv4(Whatsappv1):
    def community(self):
        print("you can multiple groups")

class Whatsappv5(Whatsappv1):
    def channels(self):
        print("you can posy regulary with huge crowd")

sailesh = Whatsappv5()
sailesh.message()
sailesh.status()
sailesh.groups()
sailesh.community()
sailesh.channels()


