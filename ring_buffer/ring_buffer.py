class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass

  def get(self):
    new_storage = []
    for i in range(len(self.storage)):
      if self.storage[i] is not None:
        new_storage.append(self.storage[i])
    
    return new_storage