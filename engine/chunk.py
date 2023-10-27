import random

CHUNK_SIZE = 16

class Chunk:
  def __init__(self):
    # Initialize a 3D array of None values
    self.voxels = [[[random.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1), None]) for _ in range(CHUNK_SIZE)]
                        for _ in range(CHUNK_SIZE)] for _ in range(CHUNK_SIZE)]
