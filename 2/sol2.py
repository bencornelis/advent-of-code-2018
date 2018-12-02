from box_ids import get_box_ids
import string

ALPHABET = set(string.ascii_lowercase)

def neighbors(box_id):
  for i in range(len(box_id)):
    for l in ALPHABET - { box_id[i] }:
      yield box_id[:i] + l + box_id[i+1:]

def letters_in_common(box_id1, box_id2):
  return ''.join(
    [box_id1[i] for i in range(len(box_id1)) if box_id1[i] == box_id2[i]]
  )

def solution():
  box_ids = set(get_box_ids())
  for box_id in box_ids:
    for neighbor_box_id in neighbors(box_id):
      if neighbor_box_id in box_ids:
        return letters_in_common(box_id, neighbor_box_id)

print(solution())
