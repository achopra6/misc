#This file is a website crawler
#It is used to put in values, submit the form and the save specific parts of the result text into a CSV

import re
from mechanize import Browser
csv = open("MYPATH/CACTI_results.txt","wb")
br = Browser()
br.open("http://quid.hpl.hp.com:9081/cacti/")
# To see element names
# print br.form
a=['32768','65536'];
b=['131072','262144'];
c=['1','2'];
d=['4','8']
l3 = 3.14609266157
i = 0
for j in range(len(a)):
    for k in range(len(b)):
        for l in range(len(c)):
            for m in range(len(d)):

                print i   
                br.form = list(br.forms())[0]
                br.form['cache_size']=a[j]
                br.form['line_size']='64'
                br.form['assoc']=c[l]
                br.form['nrbanks']='1'
                br.form['technode']='90'
                br.submit()
                lines = br.response()
                for line in lines:
                    if 'Total read dynamic power per read port at max freq (W):' in line:
                        real=line[58:-1]        
                        #print real
                    if 'Total standby leakage power per bank (W):' in line:
                        dyn=line[44:-5]
                        #print dyn
                l1=eval(real)+eval(dyn)
                #br.open("http://quid.hpl.hp.com:9081/cacti/")
                br.form = list(br.forms())[0]
                
                br.form['cache_size']=b[k]
                br.form['line_size']='64'
                br.form['assoc']=d[m]
                br.form['nrbanks']='1'
                br.form['technode']='90'
                br.submit()
                lines = br.response()
                for line in lines:
                    if 'Total read dynamic power per read port at max freq (W):' in line:
                        real=line[58:-1]        
                        #print real
                    if 'Total standby leakage power per bank (W):' in line:
                        dyn=line[44:-5]
                        #print dyn
                l2=eval(real)+eval(dyn)
                total=l1+l2+l3
                wr_string = 'c%s' % i+','+a[j]+','+b[k]+','+c[l]+','+d[m]+','+'%s' % total+"\n"
                csv.write(wr_string)
                i=i+1
csv.close()
            #print br.form['cache_size']
