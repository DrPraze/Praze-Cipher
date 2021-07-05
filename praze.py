"""Created and written by: Praise James"""


def clean_data(data): 
	global data_
	digit_list = []
	for e in data:
		digit_list.extend(ord(num) for num in e)
	data_ = digit_list
	print(str(data_))
	return data_

def convert_to_char(data):
	secret = []
	for l in data:
		for e in l:
			secret.extend(chr(int(e)))
	secret_ = ""
	for x in secret:
		secret_ += x
	print(secret_)
	return secret_

def __encrypt__(key1, key2, text = "Praze cipher"):
	global encryption, result, crack, password
	clean_data(text)
	result, crack = [], []
	for i in range(len(data_)//2):
		try:
			x = data_.pop(0)
			y =	data_.pop(1)
		except IndexError:
			print('\nfinished analyzing data\n')
		encrypt(x, y, key1, key2)
		result.append(encryption)
		crack.append([B, a_, password])
		print(result)
		# print(crack)
		i += 1
	return encryption, result, crack, password

def __decrypt__(encryption, result, crack):
	global outcome
	output, outcome = [], []
	for j in range(len(crack)):
		key = crack[j][0]
		# print(key)
		password = crack[j][2]
		# print(password)
		encryption = result[j]
		# print(encryption)
		FEK = crack[j][1]
		# print(FEK)
		decrypt(key, password, encryption, FEK)
		output.append(final)
	output = convert_to_char(output)
	outcome.append(output)
	print(outcome)
	return outcome

def encrypt(x, y, a, b):
	global B, password, lst, a_, encryption
	A = [x*a, x*b]
	B = [y*a, y*b] #key
	lst = [A[0]*B[0], A[0]*B[1], A[1]*B[0], A[1]*B[1]]
	lst.pop(1);lst.pop(2)
	encryption = [lst[0], lst[1]]
	password = A[1]*B[0]
	a_ = a

	# print("encryption: "+str(encryption))
	return encryption, password

def decrypt(key, password, encryption, FEK):
	global final
	_x_ = encryption[0]/key[0]
	_y_ = encryption[1]/key[1]
	print(key)
	output = (_x_, _y_)
	final = [_x_/FEK, key[0]/FEK]
	# print(output)
	print(final)
	return final

##==============TESTS=================
# encrypt(19, 27, 34, 78)
# decrypt(B, password, lst, a_)
# encrypt(2, 3, 4, 7)
# decrypt(B, password, lst, a_)
# encrypt(2, 2, 2, 2)
# decrypt(B, password, lst, a_)
# encrypt(3,3,3,3)
# decrypt(B, password, lst, a_)

# clean_data('schrodingers cat, quantum physics, my password is OldSpeedyThug404!')
# convert_to_char(data_)

##Note: you have to encrypt the data  decrypt it and encrypt it again, to keep the text in
##good piece, make sure you use the same key1 and key2 in the encrypting twice
##make sure 2 spaces are added to the data you're encrypting, and ignore the last letter of any decrypted result
# __encrypt__(key1 = 2, key2 = 3, text = "This is a test encryption (636543291) $%^&, yeah, it works  ")
# __decrypt__(encryption, result, crack)
# __encrypt__(key1 = 2, key2 = 3, text = outcome)

# __decrypt__(encryption, result, crack)

__encrypt__(key1 = 117233, key2 = 2398449, text = """**PRAZE CIPHER ALGORITHM**
My algorithm for encryption, the praze cipher
'How do you tell  someone you know 
a secret without saying the secret?'
mathematically, let's say, given 3*7 = 21, you can 
easily get back 3 if it was missing i.e x*7 = 21,
 x = 21/7 = 3. But how about something you can multiply
 but not get back to.
So here's the algorithm:

let's say (x, y)(a, b) = (f, g), if you don't know (x, y)
you can't get it, like this

let's say x = 2, y = 3, a = 6, b = 1

(2, 3)(6, 1) = (f, g)
let's say
(2(6, 1)), (3(6, 1))
(12, 2), (18, 3)
216, 36, 36, 6
 Note: following the algorithm, there will always be 2 alike
numbers, regardless of the numbers being used
the next part of the algorithm eliminates the 2 alike numbers
thus

(2, 3)*(6, 1) = (216, 6)
 where (2, 3) is the secret, (6, 1) is the key and (216, 6) is the encrypted data
if you're to look for (x, y) i.e:
(x, y)*(6, 1) = (216, 6)
x, y, cannot be found!

Unless you are given the value of B where B = [y*a, y*b], the value of
the alike number, the value of the encrypted data and the value of a

which is what is needed to decrypt the data, this would be the algorithm to 
decrypt it (written in python):

_x_ = 216/B[0]
_y_ = 6/B[1]
out = (_x_, _y_)
final = [_x_/a, B[0]/a]

this would result the initial secret
final = (2, 3)

here is the source code to a python implementation of the algorithm>>>
https://github.com/Trojan-Cipher/Praze-Cipher

the source code (and perhaps the algorithm) would be upgraded from time to time. feel free to test the cipher, try hacking the cipher or use it in your cryptographic projects :) ,
a detailed and better explanation would be pondered on my whitepaper which you should expect
soon! :D
i'll love your feedbacks  
""")
__decrypt__(encryption, result, crack)
__encrypt__(key1 = 117233, key2 = 2398449, text = outcome)

__decrypt__(encryption, result, crack)


