from collections import Counter
from functools import reduce
from operator import mul
from box_ids import get_box_ids

def checksum(box_ids, counts):
  counter = dict([[count, 0] for count in counts])

  for box_id in box_ids:
    box_id_counter = Counter(box_id)
    for count in counter:
      if count in box_id_counter.values():
        counter[count] += 1

  return reduce(mul, counter.values())

def solution():
  return checksum(get_box_ids(), [2, 3])

print(solution())
