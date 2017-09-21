#http://pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/
#http://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
# Import the os module, for the os.walk function
import os
import datetime
import random 
# Set the directory you want to start from

#print('first check')
#rootDir = '.\images'
def getInstr(inum,delta,parr):
    i = inum
    instr = ""
    for i in range(inum,inum+delta):
        i = i + 1
        narr = parr[i].split('\\')
        if  len(narr)>3:
              painter = narr[2]
              name = painter.split('-')
              #painterarr.append(painter)
              lastname = name[-1]
              fullname = painter.replace('-','')
              pic = narr[3]
              pic=  pic.split('.')[0]
              painter = painter.replace('-',' ')
              pic = pic.replace('-',' ')
              #print (painter)
              #print (pic)
              status =  painter+'\n'+pic
              status = status.title()
              #hashstr = '\n#art '+'#painting '+'#'+fullname+' '+'#'+lastname
              #status = status
              desc = painter+' '+pic
              desc = desc.title()
              imgsrc = narr[2]+'/'+narr[3]
              imgsrc = "images/"+imgsrc.replace('\n','')
        
         #print imgsrc
              imgstr = '<li><div  data-alt="'+imgsrc+'" data-description="<h3>'+desc \
                + '</h3>" data-max-width="1800" data-max-height="1350"><div data-src="' \
                +imgsrc+'" data-min-width="1300"></div><div data-src="' \
                +imgsrc+'" data-min-width="1000"></div><div data-src="' \
                +imgsrc+'" data-min-width="700"></div><div data-src="'  \
                +imgsrc+'" data-min-width="300"></div><div data-src="'  \
                +imgsrc+'" data-min-width="200"></div><div data-src="'  \
                +imgsrc+'" data-min-width="140"></div><div data-src="'  \
                +imgsrc+'"></div><div data-src="'+imgsrc+'"></div><noscript><img src="' \
                +imgsrc+'" alt="img03"/></noscript></div></li>'
               
              #print imgstr
              instr = instr+imgstr
    return instr


def ranfile(parr,outhtml,thtml):
    
    fout = open(outhtml,'w')
    
    fhtml = open(thtml,'r')
    htmlstr = fhtml.read()
    sgg = '<ul class="gamma-gallery">'
    tlen = len(sgg)
    mark = htmlstr.find(sgg)+tlen
    instr = ""
    outstr = ""
    #read  template file
    i = 0
    plen = len(parr)
    instr = getInstr(0,1,parr)
    

    

#outstr = '"<div id="gallery" style="display:none;">'+instr+'</div>'
#print mark
    outstr = htmlstr[:mark]+instr+htmlstr[mark:]
    sgg2 = "items = ['"
    tlen2 =len(sgg2)
    mark2 = outstr.find(sgg2)+tlen2
    instr2 = getInstr(1,2,parr)


    outstr = outstr[:mark2]+instr+outstr[mark2:]

    ftemp =  "t-00.html"
    fem = open(ftemp,"w")
    fem.write("<html><ul>"+instr+"2\n"+instr2+"</ul></html>")
    #sgg3 = "</header>"
    #tlen3 =len(sgg3)
    #mark3 = outstr.find(sgg3)+tlen3
    #pailist =""
    #for pai in list(set(painterarr)):
    #    pailist = pailist + ' ' +pai
    #outstr = outstr[:mark3]+pailist+outstr[mark3:]
    fout.write(outstr)




pfile = ".\\csv\\allimages.csv"
fp = open(pfile,'r')
parr = []
for painter in fp:
    parr.append(painter)
#random.shuffle(parr)
parr = sorted(parr)
#print parr
now =  datetime.datetime.now()
timestr = str(now).replace(' ','-').replace(':','-')
#print now
print timestr[0:16]
listf = ".\index-load-01"+'.html'
thtml = "gg-01.html"
ranfile(parr,listf,thtml)





 