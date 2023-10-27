from .chunk import Chunk

class World:
  def __init__(self):
    self.chunks = {(0, 0, 0): Chunk()}

  def get_chunk(self, x, y, z):
    return self.chunks.get((x, y, z))
