def isprime(num):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        return False
        break
    else:
        return True
  else:
    return False

if(isprime(96)):
	print("True")
else:
	print("False")