def get_frequency_changes():
  f = open('frequency_changes.txt', 'r')
  frequency_changes = [int(line.strip()) for line in f]
  f.close()
  return frequency_changes
