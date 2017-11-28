
#   Console Input
class ConsoleInput(object):
    def __init__(self,prompt):
        self.prompt = prompt
        self.line = None
        self.args = []
        self.command = None
        self.running = True
        self.commands = {}

        #built-ins
        self.commands["quit"] = self.quit
        self.commands["prompt"] = self.setPrompt
        self.commands["help"] = self.help


    def help(self):
        print "Console Input Help"
        print "Avaliable Commands"
        for comm in self.commands.keys():
            print comm
    
    def addCommand(self,name,fn):
        self.commands[name] = fn

    def setPrompt(self,prompt):
        self.prompt = prompt

    def removeCommand(self,name):
        del self.commands[name]

    def quit(self):
        self.running = False
    
    def input(self):
        while self.running:
            try:
                self.line = raw_input(self.prompt)
                self.args = self.line.split(" ")
                self.command = self.args[0]
                self.params = self.args[1:]
                if self.command in self.commands:
                    try:  
                        self.commands[self.command](*self.params)
                    except TypeError as er:
                        print "Invalid Format",self.command
                else:
                    print "Unknown Command",self.command
            except KeyboardInterrupt:
                print
                break