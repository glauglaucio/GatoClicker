import os

absolute_path = os.path.dirname(__file__)

das = os.getcwd()

full_path = os.path.join(absolute_path)

print(das)
print(absolute_path)
print(full_path)