def main():
	phonebook = {'Smith, Jane':'123-4567','Doe, John':'987-6543', 'Baker, David' :'567-8901'}
	reverseTel(phonebook)
def reverseTel(phonebook):
	my_dict2 = dict((y,x) for x,y in list(phonebook.items()))
	print(my_dict2)
