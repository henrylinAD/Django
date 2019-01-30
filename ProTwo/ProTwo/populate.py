import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()


# FAKE POP SCRIPT
import random
from AppTwo.models import AccessRecord,Webpage,Topic,User 
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace','News','Games']

def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5): 

	for entry in range(N): 
		fake_name = fakegen.name().split()
		fake_first_name = fake_name[0]
		fake_last_name = fake_name[1]
		fake_email = fakegen.email()

		user = User.objects.get_or_create(first_name=fake_first_name, 
										  last_name=fake_last_name,
										  email=fake_email)[0]
		# #get the topic for the entry
		# top = add_topic()

		# #create the fake data for that entry 
		# fake_url = fakegen.url()
		# fake_date = fakegen.date()
		# fake_name = fakegen.company()

		# #create the new webpage entry
		# webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

		# #create a fake access record for that webpage
		# acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__': 
	print("populating data!")
	populate(20)
	print("populating complete!")