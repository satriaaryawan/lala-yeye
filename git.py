import webbrowser, subprocess, os

workspace=os.getcwd()

link=['https://github.com/nvnrdhn/SoalShift_modul4_E14',
    'https://github.com/clausaxon/SoalShift_modul4_C12',
    'https://github.com/jihannbl/SoalShift_modul4_E06',
    'https://github.com/paramastri/SoalShift_modul4_F10']

dir_github=[]

for i in link:  
    dir_github.append(i.split('/')[-1])

def open_git():
    for i in link:
        webbrowser.open(i)

def download_git():
    for i in dir_github:
        if os.path.isdir(i):
            os.chdir(i)
            print(i)
            subprocess.call(['git', 'pull'])
            os.chdir(workspace)
        else:
            for i in link:
                subprocess.call(['git', 'clone', i])

def main():
    options=input('open or download: ')
    if options=='open':
        open_git()
    elif options=='download':
        download_git()
    else:
        print('wrong options')

if __name__ == "__main__":
    main()