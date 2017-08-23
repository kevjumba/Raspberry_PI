import command_parse
import sys

def exec_cmds(input_string):
    lst = input_string.split(':')
    for cmd in lst:
        output = command_parse.exec_cmd(cmd)
        if(output):
            sys.stdout.write(command_parse.exec_cmd(cmd)+";")
if(__name__ == "__main__"):
    exec_cmds(sys.argv[1])
