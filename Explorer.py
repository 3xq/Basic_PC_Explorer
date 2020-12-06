import os
array=False
def Explorer():
    dir=input('Directory: ').replace('\\','\\\\')
    array=os.listdir(dir)
    expint=1
    for x in array:
        print(f'{expint}. {x}')
        expint=expint+1
    Explorer()
Explorer()
