#Create a variable called 'number' and assign it the three-digit number.

#Find the 'number' first digit and assign to x1.

#Find the 'number' second digit and assign to x2.

#Find the 'number' third digit and assign to x3.

#Create a variable called 'answer' and assign it the sum of the three digits.

#print the sum of the three digits.

number=123
n1=number%10
number//=10
n2=number%10
n3=number//10
answer=n1+n2+n3
print(answer)