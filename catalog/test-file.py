import os
from pathlib import Path
# os.mkdir('example')

try:
    Path('example').mkdir()
except FileExistsError as e:
    print(e)
    
Path('example').mkdir(exist_ok=True) 

os.makedirs('2025/03/20', exist_ok=True, mode=0o770)

dirnames = ('2025', '2025/03', '2025/03/20')

filenames = ('hello.txt', 'world.txt', 'random1.txt', 'fpp.txt')

for dirname in dirnames:
    for filename in filenames:
        Path(dirname+'/'+filename).touch()


with os.scandir('2025') as hf:
    for h in hf:
        if h.is_file():
            print(h.name)
            


numbers = [1,2,3,4,5,6,7,8,9]
# print([n**3 for n in numbers])

print([n for n in numbers if n%2 == 0])

for file in [i for i in os.scandir('2025') if os.path.isfile(i)]:print(file.name)

dirname = '2025'

for root, dirs, files in os.walk(dirname):
    for dir_name in dirs:
        print(os.path.join(root, dir_name))
    for file_name in files:
        print(os.path.join(root, file_name))
