
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui import gui


def run():
    gui.start()


if __name__ == '__main__':
    run()

# EOF
