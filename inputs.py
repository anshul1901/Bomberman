"""Taking input."""

import signal
import sys
import tty
import termios


class Get:
    """Class get."""

    def __init__(self):
        """Initialise."""

    def __call__(self):
        """."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class AlarmException(Exception):
    """Raise an exception."""

    pass


def alarmHandler(signum, frame):
    """Raise an exception."""
    raise AlarmException


getch = Get()


def input_to(timeout=0.1):
    """Take input."""
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
