import os

def main():
    os.system("git add .")
    os.system(r'git commit -m "danielcommit"')
    os.system("git push")

if __name__ == '__main__':
    main()
    
