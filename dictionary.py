my_dict={'name':'Thisath','age':'12','class':'7'}
print(my_dict['name'])
my_dict['age']=12
print(my_dict)
my_dict['gender']="Male"
print(my_dict)


country_code={'India':'0091','Australia':'0025','Nepal':'0097','New Zealend':'0064','Italy':'0039'}
print("country code for india - ")
print(country_code.get('india','not Found'))
print("Country code for japan - ")
print(country_code.get('japan','not Found'))
print("Country code for australia -")
print(country_code.get('australia', 'not found'))
print("Country code for USA -")
print(country_code.get('USA','not Found'))
print("Country code for nepal -")
print(country_code.get('nepal','not Found'))