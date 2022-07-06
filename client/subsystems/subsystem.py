import abc
import queue
import threading
import sys


class Subsystem:
    """
    Subsystem base class.
    """

    def __init__(self):
        self.lock = threading.Lock()
        self.queue = queue.Queue()
        self.worker = threading.Thread(target=self.do_work, name=f'{self.__class__.__name__}_worker')
        self.active = False

    @abc.abstractmethod
    def on_active(self):
        """ called to make the controller ready for tasking."""
        pass

    @abc.abstractmethod
    def do_work(self):
        pass

    @abc.abstractmethod
    def shutdown(self):
        sys.exit()
