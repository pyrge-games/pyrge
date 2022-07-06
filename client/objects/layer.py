import queue
import threading

class Layer:

    # todo where entity positions are static, blit them onto a common canvas.

    def __init__(self, name: str = "NewLayer"):
        self.name = name
        self.queue = queue.Queue()
        self.entities = []
        self.lock = threading.Lock()

    def clear(self):
        with self.lock:
            self.entities = []
            self.queue = queue.Queue()

    def insert(self, entity):
        with self.lock:
            self.entities.append(entity)
