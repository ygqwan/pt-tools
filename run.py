import sys


if __name__ == '__main__':
    project = sys.argv[1]
    action = sys.argv[2]

    if project == 'nexusphp':
        from NexusPHP.tasks.say_thanks import main as saythanks
        from NexusPHP.tasks.sign_in import main as signin
        eval('%s()' % action)
    else:
        print('命令参数1 不正确!')