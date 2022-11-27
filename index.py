import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','r','S','T','U','V','W','X','Y','Z',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','-','+','=','?',':','~']
print("welcome to the passward genrator!")
nr_letters=int(input(f"how many letters would you like in your password \n"))
nr_numbers=int(input(f"how many numbers would you like \n"))
nr_symbols=int(input(f"how many symbols would you like \n"))

password_list = []
for char in range(1, nr_letters+1):
  password_list.append(random.choice(letters))
  # random_char = random.choice(letters)
  # password += random_char

for char in range(1, nr_symbols+1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers+1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for char in password_list:
  password += char

print(f"Your password is:{password}")