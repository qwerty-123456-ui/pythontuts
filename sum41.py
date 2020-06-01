import os
# os.getcwd()
# os.chdir(r"E:")
print(os.getcwd())
# os.mkdir('movies')
# print(os.path.exists('movies'))
if os.path.exists('movies'):
    print('already exists')
else:
    os.mkdir('movies')
open('file.txt','a').close()

print(os.listdir())

print(os.listdir(r'E:'))
for item in os.listdir():
    print(os.path.join(os.getcwd(),item))
