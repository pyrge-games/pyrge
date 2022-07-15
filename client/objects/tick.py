import queue


class Tick:
    def __init__(self):
        self.rate = 0 # should be in ms
        self.run_count = 0
        self.jobs = []
        self.queue = queue.Queue