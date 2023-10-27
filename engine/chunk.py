CHUNK_SIZE = 16

class Chunk:
  def __init__(self):
    # Initialize a 3D array of None values
    # None = empty voxel
    # Replace None with actual voxel data later
    self.voxels = [[[None for _ in range(CHUNK_SIZE) for _ in range(CHUNK_SIZE)] for _ in range(CHUNK_SIZE)]
