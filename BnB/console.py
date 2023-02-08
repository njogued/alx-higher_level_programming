#!/usr/bin/python3
'''
Console program
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    Cmd application
    '''
    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quit command to exit the program

        '''
        return True

    def do_EOF(self, line):
        '''Quit command to exit the program

        '''
        return True

    def emptyline(self):
        '''
        Prevent executiong of last command after new line
        '''
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
