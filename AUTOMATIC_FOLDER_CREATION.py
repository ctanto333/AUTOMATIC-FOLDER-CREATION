import os
from datetime import datetime, timedelta
import shutil


a = datetime.today() #declaring todays date in a variable 'a';
b = a.strftime('%m.%B') #declaring month in number and in text in a variable 'b'
c = a.strftime('%d.%m.%y')
e = a.strftime('%Y')
yesterday = a - timedelta(days=1)
d = yesterday.strftime('%d.%m.%y') #declaring yesterdays date month and time and stroing it in variable 'd'
empty_folder = (os.path.join(r'Z:\To Anto\\', d))

if not os.path.isdir(os.path.join(r'Z:\DESIGN\Drawings\\', e)):
    os.mkdir(os.path.join(r'Z:\DESIGN\Drawings\\',e))

if not os.path.isdir(os.path.join(r'Z:\DESIGN\Drawings\\', e,b)):
    os.mkdir(os.path.join(r'Z:\DESIGN\Drawings\\',e,b))
    
if not os.path.isdir(os.path.join(r'Z:\DESIGN\Drawings\\', e,b,c)):
    os.mkdir(os.path.join(r'Z:\DESIGN\Drawings\\',e,b,c))
    
if not os.path.isdir(os.path.join(r'Z:\To Anto\\', c)):
    os.mkdir(os.path.join(r'Z:\To Anto\\', c))

if os.path.isdir(os.path.join(r'Z:\To Anto\\', d)):
    files_check = os.listdir(empty_folder)
    if len(files_check) == 0:
        shutil.rmtree(os.path.join(r'Z:\To Anto\\', d))

