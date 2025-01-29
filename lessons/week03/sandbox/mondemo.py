def main()-> None:
    """ driver function of the program """
    # Example usage
    user_input = int(input("\t Enter a number: "))
    result = is_prime(user_input)
    if result:
        print(f"\t {user_input}: Prime number")
    else:
        print(f"\t {user_input}: Not a prime number")
# end of main()

# place at bottom of the file
# main() # call the main() function


def is_prime(number: int) -> bool:
    """ Determine primality: return 0 and 1"""
    # Handle special cases for 0 and 1
    if number < 2:
        return False

   # Iterate from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        # If the number is divisible
        # by any value in the range, it's not prime
        if number % i == 0:
            return False

   # If no divisors are found, the number is prime
    return True
# end of is_prime()
main()

def squareArea(s: float ) -> float:
    """ determine area f square""" 
    return s * s  # area of square s s*s
# end of squareArea() 

print(squareArea(1+3j))

def main() -> None: 
	sideLength = 5
	# Testing value
	print(f"Length {sideLength}")
	print(f" Area: {squareArea(sideLength)}")

    # These inputs work 
	testValues_list = [2, 0, -3, 2 + 5j]
    # why will these inuts not work?
	# testValues_list = [True, "radius"]
    # print(f"\n Iterating over the list.") 
	 
	for val in testValues_list: # iterati
		print(f" Length {val}, Area: {squareArea(val)}") 
	# end main()

main()
