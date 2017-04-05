def fizz_buzz(number):
  returnvalue = number
  if number % 3 == 0:
    returnvalue = 'Fizz'
  if number % 5 == 0:
    if isinstance(returnvalue,str):
      returnvalue += 'Buzz'
    else:
      returnvalue = 'Buzz'
      
  return returnvalue

print fizz_buzz(15)
