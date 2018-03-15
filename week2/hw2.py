while True:
	    numara1 = input("Numara 1: ")
	    numara1 = int(numara1) - 1
	    numara2 = input("Numara 2: ")
	    numara2 = int(numara2)
	    str = input("String: ")
	    str2 = str[numara2:]
	    str = str[:numara1]
	    print (str,str2)
