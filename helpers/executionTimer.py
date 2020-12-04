import time

class executionTimer:
    def __init__(self):
        self.initTime = time.time()

    def stopTimer(self):
        stopTime = time.time()
        print('Execution took {0} ms'.format(int((stopTime - self.initTime) * 1000)))
