import zipfile
import rarfile

def crack_zip():
	zip_fil = input('Enter your zip file name: ')
	wordlist = 'wordlist.txt'

	with zipfile.ZipFile(zip_fil) as ZF:
		with open(wordlist, 'r') as WL:
			for line in WL:
				password = line.strip()
				try:
					ZF.extractall(pwd=password.encode('utf-8'))
					print(f'\nzip password is creacked ! \nPassword:{password}')
					break
				except:
					print('Error to crack !')



def crack_rar():
	rar_file = input('Enter your rar file name: ')
	wordlist = 'wordlist.txt'

	with rarfile.RarFile(rar_file) as RF:
		with open(wordlist, 'r') as WL:
			for line in WL:
				password = line.strip()
				try:
					RF.extractall(pwd=password)
					print(f'\nRar password is creacked\npassword:{password}')
					break
				except rarfile.BadRarFile:
					print('Bad rar file error !')
					break
				except rarfile.PasswordRequired:
					continue
				except Exception as e:
					print(f'Error: {e}')



File_type = input('Whats your file type [1]Zip, [2]Rar:  ')

if int(File_type) == 1:
	crack_zip()

elif int(File_type) == 2:
	crack_rar()

else:
	print('Undefined !!!')

