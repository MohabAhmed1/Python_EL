
def Check_vowel(l):
    if l == 'a' or l == 'e' or l == 'o' or l == 'i' or l == 'u':
        return True
    else:
        return False

l = input("Enter the Letter to check : ")

if Check_vowel(l) == True:
    print('The Letter is Vowel')
else:
    print('The Letter is not Vowel')

