import os

files = []
for file in os.listdir():
    if file.endswith(".py3"):
        files.append(file)
files.remove(os.path.basename(__file__))

for file in files:
    os.system("python {0}".format(file))
print(files)