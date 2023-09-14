class Mersenne:
  def __init__(self, seed=None):
    self.bitmask_1 = (2 ** 32) - 1  # To get last 32 bits
    self.bitmask_2 = 2 ** 31  # To get 32nd bit
    self.bitmask_3 = (2 ** 31) - 1  # To get last 31 bits
    if seed is None:
      self.seed = int((datetime.utcnow() - datetime.min).total_seconds())
    else:
      self.seed = seed
    self.MT, self.index = self._initalize(seed)
  def _initalize(self, seed):
    "Initialize the generator from a seed"
    # Create a length 624 list to store the state of the generator
    MT = [0 for i in range(624)]
    index = 0
    MT[0] = seed
    for i in range(1, 624):
      MT[i] = ((1812433253 * MT[i - 1]) ^ (
              (MT[i - 1] >> 30) + i)) & self.bitmask_1
    return (MT, index)
  def _generate_numbers(self, MT):
    "Generate an array of 624 untempered numbers"
    for i in range(624):
      y = (MT[i] & self.bitmask_2) + (MT[(i + 1) % 624] & self.bitmask_3)
      MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
      if y % 2 != 0:
        MT[i] ^= 2567483615
    return MT
  def sample(self):
    """
        Extract a tempered pseudorandom number based on the index-th value,
        calling generate_numbers() every 624 numbers
        """
    if self.index == 0:
      self.MT = self.generate_numbers(self.MT)
    y = self.MT[self.index]
    y ^= y >> 11
    y ^= (y << 7) & 2636928640
    y ^= (y << 15) & 4022730752
    y ^= y >> 18

    self.index = (self.index + 1) % 624
    return y

from datetime import datetime
class RANDU:
  def __init__(self, seed=None, c=65539, m=2147483648):
    self.c = c
    self.m = m
    if seed is None:
      self.seed = int((datetime.utcnow() - datetime.min).total_seconds())
    else:
      self.seed = seed
  def sample(self):
    return abs((self.c * self.seed) % self.m)