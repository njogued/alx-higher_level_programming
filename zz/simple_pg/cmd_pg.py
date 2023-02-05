#!/usr/bin/python3
'''
Using cmd in commandline programs
'''
import cmd
import time
create_user = __import__(users).User

class ConsolePg(cmd.Cmd):
    print("STARTING THE PROGRAM\n---------------------")
    ct = f"(({time.ctime()}))>>> "
    prompt = ct
    def do_greet(self, line):
        '''Greets a person'''
        print("hello ", line)

    def do_create(self, line):
        print("Calling the {} class".format(line))
        time.sleep(2)
        print(f"Class {line} has not been created yet")

    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    ConsolePg().cmdloop()
