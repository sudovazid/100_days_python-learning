class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"Plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")
    
    def speaks(self):
        print(self.name,"says how are you ?")

tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()


maria = Human("maria sharapova", "tennis player")
maria.do_work()
maria.speaks()