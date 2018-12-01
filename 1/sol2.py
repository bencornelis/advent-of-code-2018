from frequency_changes import get_frequency_changes
from itertools import cycle

def solution():
  frequency_changes = get_frequency_changes()
  prev_frequencies = set()
  cur_frequency = 0

  for frequency_change in cycle(frequency_changes):
    if cur_frequency in prev_frequencies:
      return cur_frequency
    else:
      prev_frequencies.add(cur_frequency)
    cur_frequency += frequency_change

print(solution())
