from subprocess import run, PIPE
import shlex
import shutil


def split_commands(line: str) -> list[list[str]]:
    command_strs = line.split('|')

    split_cmds = map(lambda cmd: shlex.split(cmd), command_strs)
    cmds = map(lambda cmd: [shutil.which(cmd[0])] + cmd[1:], split_cmds)

    return list(cmds)


def execute_commands(cmds: list[list[str]]):
    prev = run(cmds[0], stdout=PIPE)

    for cmd in cmds[1:]:
        prev = run(cmd, input=prev.stdout, stdout=PIPE)

    print(f'{prev.stdout.decode("utf-8")}')


if __name__ == '__main__':
    command = input('> ')
    commands = split_commands(command)
    execute_commands(commands)
