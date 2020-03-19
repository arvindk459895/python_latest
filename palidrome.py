#!/usr/bin/python3
# function which return reverse of a string
def reverse(s):
    return s[::-1]
#Function checking for Pallidrome
def is_Palindrome(s):
    # Calling reverse function 
    rev = reverse(s)
    # Checking if both string are equal or not
    if (s == rev):
        return True
# Main defination
def main():
	s = "radtr" 
	ret = is_Palindrome(s)

	if ret == True:
    		print("True")
	else:
    		print("False") 

#boiler Plate
if __name__ == "__main__":
	main()
