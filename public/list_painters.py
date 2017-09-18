
narr=[]
fo = open('flist-01.csv','r')
for line in fo:
  #nstr =  line['name'].encode('utf-8').replace('\n','')
  narr = line.split('\\')
  #print(len(narr))
  if  len(narr)==4:
    painter = narr[2]
    pic = narr[3]
    pic=  pic.split('.')[0]
    painter = painter.replace('-',' ')
    pic = pic.replace('-',' ')
    print (painter)
    print (pic)
    status =  painter+'\n'+pic
    status = status.title()
    myb = "axufile"
    tmpf = '/tmp/'+narr[2]
#     print(myb,nstr,tmpf)
    #boto3.client('s3').download_file(myb,nstr,tmpf)
    #file = open(tmpf,'rb')
    #api.update_with_media(tmpf, status=status)
    #table.delete_item(
    #     Key={
     #      'name': item['name'],
     #  })
