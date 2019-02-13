print ("Menentukan Bilangan Terbesar Dari 3 Bilangan\n")
print ("Masukan bilangan yang di inginkan\n")

A = int (input ("Masukan bilangan pertama : "))
B = int (input ("Masukan bilangan kedua   : "))
C = int (input ("Masukan bilangan ketiga  : "))

if A > B > C :
    print ("\nBilangan pertama adalah bilangan terbesar = %s" % A)
elif B > C :
    print ("\nBilangan kedua adalah bilangan terbesar = %s" % B)
else:
    print ("\nBilangan ketiga adalah bilangan terbesar =%s" % C)