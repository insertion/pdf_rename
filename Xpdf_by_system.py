# -*- coding: utf-8 -*-
"""
Attention: 
    only work in python2!!
    if you want it work in python3,you need to change the code by yourself;
    this program is write only for papers not for all pdf files
usage:
    you can put this file in the folder which your pdf files locate,
    or you can change the path in the code.
    this program needs pdftotext.exe,the exe file also need be put in the same folder
    you can download xpdf in this page http://www.foolabs.com/xpdf/download.html

    just open your cmd,and type 

            python xpdf_by_system.py

Created on 2016-11-1 14:43:46

@author: wlei

"""

import os 
for fileName in os.listdir('.'):
    try:
        if fileName.lower()[-3:]!='pdf':
            continue
        tempfilename = 'temp.txt'
        cmd = 'pdftotext.exe -q ' + fileName + ' '+tempfilename
        os.system(cmd)
        temp = open(tempfilename,'rb')
        title = temp.readline()
        while title[:-1].strip() == '':
            title = temp.readline()
        if title[:5] =='arXiv':
            title = temp.readline()
            while title[:-1].strip() == '':
                title = temp.readline()
        trgtfilename = title[:-1].strip().replace(' ','_') + '.pdf'
        trgtfilename = trgtfilename.replace(':', '_')
        trgtfilename = trgtfilename.replace('*', '_')
        trgtfilename = trgtfilename.replace('/', '_') 
        trgtfilename = trgtfilename.replace('?', '_')
        temp.close()
    except:
        print '\n## ERROR ## Unknown fault'
        pass

    try:
        print trgtfilename
        os.rename(fileName,trgtfilename)
        print ''
    except:
        print fileName, ' could not be renamed!'
        print '\n## ERROR ## Maybe the filename already exists or the document is already opened!'
    
os.remove(tempfilename)
print 'Done!' 