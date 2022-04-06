# example 1
class Accident(Exception):
    def __init__(self,msg):
        self.msg= msg
    def print_exception(self):
        print("User defined exception: ", self.msg)


try:
    raise Accident ('crash between two car')
except Accident as e:
    e.print_exception()


# example 2

def process_file():
    try:
        f=open("c:\\data\\funny.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleanig up file")
        f.close()


process_file()