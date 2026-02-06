import lele
from collections.abc import Iterable
from lele.Subprocess import run_shell_command

def run_multiple_shell_commands(list_of_commands):
    if type(list_of_commands) is str: 
        return run_shell_command(cmd=list_of_commands)
    elif isinstance(list_of_commands, Iterable):
        cmd = '&&'.join(list_of_commands)
        return run_shell_command(cmd)


def test_():
    cmds = ("echo Hi!", "echo Hello?")
    assert run_multiple_shell_commands(cmds) == "Hi!\nHello?"
