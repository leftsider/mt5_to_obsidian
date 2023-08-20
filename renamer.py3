
import os
import re

def rename_files(directory):
  directory = '../LSDRTest'
  if not os.path.exists(directory):
    print(f'The directory "{directory}" does not exist.')
    return

  for file in os.listdir(directory):
    if not file.endswith('.md'):
      continue

    with open(os.path.join(directory, file), 'r') as f:
      lines = f.readlines()
      basename = None
      for line in lines:
        if line.startswith('BASENAME:'):
          basename = line[10:]
          break

      if not basename:
        print(f'The file "{file}" does not contain a basename.\n')
        continue

      new_name = basename + ".md"
      counter = 1
      while os.path.exists(os.path.join(directory, new_name)):
        new_name = f'{basename} ({counter})'
        counter += 1

      os.rename(os.path.join(directory, file), os.path.join(directory, 
new_name))


if __name__ == '__main__':
  directory = '../LSDRTest/'
  rename_files(directory)

