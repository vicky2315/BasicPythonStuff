import camelcase

x = camelcase.CamelCase()

n = int(input("Enter the number of names"))
print("Enter the list of names which first letters need to be capitalized")
names = [None] * n
for i in range(0,n):
    names[i] = input()
    names[i] = x.hump(names[i])

print("The capitalized names are")
for i in range(0,n):
    print(names[i])



