"""
Regular Expression Validator (Programming Exercise 6)

This program asks the user to enter a phone number, social security number,
and ZIP code. It uses regular expressions to check if the values are in the
correct format.

Student: Maria Galante
Date: 2026-02-25
"""

# Import the regular expression module so it can check patterns
import re



def validate_phone(phone_number):
    """
    This function checks if the phone number is in the format ###-###-####.

    Parameters:
    phone_number (str) - phone number entered by the user

    Variables:
    pattern (str) - regular expression pattern for a phone number

    Steps:
    1. Create the phone number regex pattern.
    2. Use re.fullmatch() to check the entire input.
    3. Return True if valid, otherwise return False.

    Returns:
    True if valid, False if invalid.
    """

    # Regex pattern for a phone number
    pattern = r"\d{3}-\d{3}-\d{4}"

    # Makes sure the whole string follows the pattern
    if re.fullmatch(pattern, phone_number):
        return True
    else:
        return False



def validate_ssn(ssn):
    """
    This function checks if a social security number is valid.
    The correct format is ###-##-####.
    Parameters:
    ssn (str) - social security number entered by the user

    Variables:
    pattern (str) - regular expression pattern for a social security number

    Steps:
    1. Create the SSN regex pattern.
    2. Use re.fullmatch() to check the entire input.
    3. Return True if valid, otherwise return False.

    Returns:
    True if valid, False if invalid.
    """

    # Regex pattern for SSN
    pattern = r"\d{3}-\d{2}-\d{4}"

    # Check if the whole string matches the pattern
    if re.fullmatch(pattern, ssn):
        return True
    else:
        return False



def validate_zip(zip_code):
    """
    This function checks if a ZIP code is valid.

    It allows:
    ##### or #####-####

    Parameters:
    zip_code (str) - ZIP code entered by the user

    Variables:
    pattern (str) - regular expression pattern for ZIP codes

    Steps:
    1. Create the ZIP code regex pattern.
    2. Use re.fullmatch() to check the entire input.
    3. Return True if valid, otherwise return False.

    Returns:
    True if valid, False if invalid.
    """

    # Regex pattern for ZIP codes
    pattern = r"\d{5}(-\d{4})?"

    # Check if the ZIP code matches the pattern
    if re.fullmatch(pattern, zip_code):
        return True
    else:
        return False



def main():
    """
    Description:
    This function gets user input and displays whether the phone number,
    social security number, and ZIP code are valid.

    Parameters:
    None

    Variables:
    phone_number (str) - phone number entered by the user
    ssn (str) - social security number entered by the user
    zip_code (str) - ZIP code entered by the user

    Steps:
    1. Ask the user to enter a phone number.
    2. Ask the user to enter a social security number.
    3. Ask the user to enter a ZIP code.
    4. Validate each input.
    5. Display whether each input is valid or invalid.

    Returns:
    None
    """

    # Ask the user for a phone number
    phone_number = input("Enter a phone number (###-###-####): ")

    # Ask the user for a social security number
    ssn = input("Enter a social security number (###-##-####): ")

    # Ask the user for a ZIP code
    zip_code = input("Enter a ZIP code (##### or #####-####): ")

    print()

    # Check phone number
    if validate_phone(phone_number):
        print("Phone number is valid.")
    else:
        print("Phone number is not valid.")

    # Check SSN
    if validate_ssn(ssn):
        print("SSN is valid.")
    else:
        print("SSN is not valid.")

    # Check ZIP code
    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is not valid.")



# Run the program
if __name__ == "__main__":
    main()