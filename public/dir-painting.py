#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from

print('first check')
rootDir = '.\images'


def flist():
  t="dir,name,twi,extra\n"
  for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
     
    for fname in fileList:
        #print('\t%s' % fname)
        t=t+dirName+','+fname+', , ,\n'
  return t

# writing csv
 
pfile = ".\csv\painterlist-01.csv"
fp = open(pfile,'r')
for painter in fp:
    #print painter
    listf = ".\csv\\"+painter+'.csv'
    listf = listf.replace('\n','')
    plistcsv = open(listf,'w')
    print listf
ft = flist()


 