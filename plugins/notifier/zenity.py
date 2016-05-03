name = 'zenity'


def show(content):
    from plugins.common import PyZenity
    PyZenity.InfoMessage(content)
