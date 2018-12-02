def get_box_ids():
  f = open('box_ids.txt', 'r')
  box_ids = [line.strip() for line in f]
  f.close()
  return box_ids
