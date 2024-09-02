class ReverseString:
    def __call__(self, text):
        # Return the reversed version of the string which will be inputed 
        return text[::-1]
    
reverse_string = ReverseString() 

result1 = reverse_string("Joshua")  
print(f"Reversed 'hello': {result1}")

result2 = reverse_string("Ndegwa")  
print(f"Reversed 'Python': {result2}")
