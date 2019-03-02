import json
def isi_bio():
	json_dict={}
	name=str(input("masukkan nama: "))
	address=str(input("masukkan alamat: "))
	temp=int(input('masukkan jumlah hobi anda: '))
	hobbies=[]
	school={'highSchool':'None','university':'None'}
	skills={}
	for x in range(temp):
		inp=str(input("masukkan hobby anda: "))
		hobbies.append(inp)
	bol_married=False
	is_married=str(input("apakah sudah menikah? Y/N: "))
	if is_married=='Y':
		bol_married=True
	elif is_married=='N':
		print()
	else :
		print("Input anda salah")
	high_school=str(input("masukkan highschool kamu: "))
	school['highSchool']=high_school
	university_=str(input("masukkan university kamu: "))
	school['university']=university_
	temp=int(input('masukkan jumlah skill anda: '))
	for x in range(temp):
		skill_val=[]
		key=str(input("skill "+str(x)+" anda :"))
		temp__=int(input("berapa jumlah skill "+key+" anda:"))
		for j in range(temp__):
			value=str(input("masukkan skill "+key+" anda:"))
			skill_val.append(value)
		skills[key]=skill_val
	json_dict['name']=name
	json_dict['address']=address
	json_dict['hobbies']=hobbies
	json_dict['is_married']=bol_married
	json_dict['school']=school
	json_dict['skills']=skills
	return_info=json.dumps(json_dict)
	return print(return_info)

isi_bio()

		