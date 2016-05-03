name = 'zenity'


def show(content):
    from common import PyZenity
    PyZenity.InfoMessage(content)
