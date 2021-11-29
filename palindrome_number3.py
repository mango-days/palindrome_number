num = 12321
str_num = str(num)
for index in range ( 0 , int( len( str_num )/2 ) ) :
    if str_num[index] != str_num[ len(str_num)-index-1 ] :
        print ("not a palindrome")
        break
    elif index == int( len( str_num )/2 )-1 :
        print ( "palindrome" )
