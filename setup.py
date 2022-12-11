import os

for day in range(1, 26):
    folder_path = ".\\0" + str(day)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        open(f'{folder_path}\\day_{day}.py', 'a').close()
        open(f'{folder_path}\\day_{day}_2.py', 'a').close()