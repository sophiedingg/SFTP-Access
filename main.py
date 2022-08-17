# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#test

import pysftp

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # with pysftp.Connection('hostname', username='user', password='secret') as sftp:
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection('sftp.itd.umich.edu', username='sophding', password='cinderblockgarden', cnopts=cnopts) as sftp:
        dirs = sftp.listdir('Public/html')
        with sftp.cd('/afs/umich.edu/group/acadaff/natlpc/Public/html/newsite'):  # temporarily chdir to public

            currentfile = sftp.get('index.html')

        print(dirs)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
