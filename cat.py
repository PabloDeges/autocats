from instagrapi import Client
import accdata
import random
import datetime
import time
import os
import requests
import pdb


cl = Client()
cl.login(accdata.username, accdata.password)
meows = ["mow", "meow", "mreoww", "meep", "miau", "mauu"]
rr = random.randint(0,5)

while True:
	# make cat api request and download
	
	page = requests.get("https://cataas.com/cat")

	f_ext = os.path.splitext("https://cataas.com/cat")[-1]
	f_name = 'cat_img{}'.format(f_ext)
	with open(f_name, 'wb') as f:
            f.write(page.content)


	# upload cat image
	try:
            print("called me")
            cl.photo_upload("/Users/pdeges/Desktop/code/python/igcats/cat_img", meows[rr])
            print("upload at " + str(datetime.datetime.now()) + " successful")
	except Exception as e:
            print("something went wrong :'3")
            if str(type(e)) == "<class 'instagrapi.exceptions.UnknownError'>":
                
                print(e)
                continue
                time.sleep(120)


	# 60 sec buffer
	time.sleep(60)

