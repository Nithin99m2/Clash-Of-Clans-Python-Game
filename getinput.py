import signal

'''To get input from user'''
class getch:
    def __init__(self):
        import tty
        import sys
    def __call__(self):
        import sys
        import tty
        import termios
        fileDescriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fileDescriptor)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fileDescriptor, termios.TCSADRAIN, old_settings)
        return ch

class PingException(Exception):
    pass

def handle_ping(signum, frame):
    raise PingException

def get_input(timeout=0.09):
    signal.signal(signal.SIGALRM, handle_ping)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getch()()
        signal.alarm(0)
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return text
    except PingException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''