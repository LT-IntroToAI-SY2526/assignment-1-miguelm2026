# Assignment 1: AI-Generated Python Problems
# Name: Miguel Martinez

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning the basics of python as a high schooler in class, can you generate me 5-7 basic problems that cover true and false?

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
Write a Python program that checks if a number is positive. If it is, print True, otherwise print False.

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""
print("Testing Problem 1:")
number = 10  # Example value

is_positive = number > 0
print("Is the number positive?", is_positive)


print("\nTesting Problem 2:")
number = 7  # Example value

is_even = number % 2 == 0
print("Is the number even?", is_even)


print("\nTesting Problem 3:")
a = 5
b = 5  # Try changing to a different number to test

are_equal = a == b
print("Are the two numbers equal?", are_equal)


print("\nTesting Problem 4:")
age = 16  # Example age

is_teenager = age >= 13 and age <= 19
print("Is the person a teenager?", is_teenager)


print("\nTesting Problem 5:")
number = 15  # Example value

in_range = number > 10 and number < 20
print("Is the number > 10 and < 20?", in_range)
