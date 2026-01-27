DEBUGGING REPORT – Debugging_Exercise.py

--------------------------------------------------

1. Overview

The purpose of this program is to calculate discount amounts and final prices for a list of products. The program uses two functions: one to calculate the discount amount and another to apply the discount to the original price. During execution, the program crashed due to type mismatches caused by inconsistent data in the product list. The goal of this debugging process was to identify the cause of the errors, fix the issues, improve error handling, and verify that the program works correctly.

--------------------------------------------------

2. Identifying the Error

Initial Error Detection

The program was executed using PyCharm’s Debug mode. A breakpoint was placed on the following line inside the calculate_discount() function:

    discount_amount = price * discount_rate

When execution paused, the debugger showed that the product "Tablet" had a price value of '500', which was stored as a string, while discount_rate was a float value of 0.2. This caused a TypeError because Python cannot multiply a string by a floating-point number.

Figure 1 shows the debugger paused at this line with the variable values displayed.

[INSERT SCREENSHOT 1: Multiplication Error in calculate_discount()]

This confirmed that the root cause of the first crash was a type mismatch between the price and discount_rate variables.

--------------------------------------------------

3. Secondary Error Discovery

After converting price to a float in the calculate_discount() function, the program was run again. This allowed the multiplication step to succeed, but a new error appeared in the apply_discount() function at the following line:

    new_price = price - discount_amount

The debugger revealed that price was still being passed as a string into this function, while discount_amount was a float. This resulted in another TypeError because Python cannot subtract a float from a string.

Figure 2 shows the debugger paused at this subtraction error with the incorrect variable types.

[INSERT SCREENSHOT 2: Subtraction Error in apply_discount()]

This demonstrated that input validation needed to be applied consistently across both functions.

--------------------------------------------------

4. Fixes and Improvements Made

The following changes were implemented to correct the issues:

1. Input Validation and Conversion
   - Both price and discount_rate were converted to float values before calculations.
   - If conversion failed, meaningful error messages were raised.

2. Discount Rate Validation
   - A validation check was added to ensure discount_rate values fall between 0 and 1.

3. Error Handling
   - Try/except blocks were added to prevent the entire program from crashing when invalid input was encountered.
   - Clear error messages were printed when invalid data was detected.

4. Consistent Type Handling
   - The apply_discount() function was updated to convert price to a float before performing subtraction.

These changes ensured the program could safely handle numeric strings such as "500" and reject invalid values without terminating execution.

--------------------------------------------------

5. Testing the Solution

After implementing all fixes, the program was tested using the original product list.

Test Results:

- All products were processed successfully.
- The "Tablet" product was correctly converted from a string to a numeric value.
- No runtime errors occurred.
- The program completed execution normally.

Figure 3 shows the successful console output after the fixes were applied.

[INSERT SCREENSHOT 3: Successful Program Output]

--------------------------------------------------

6. Conclusion

The debugging process identified two related TypeErrors caused by inconsistent data types. By using PyCharm’s debugger, inspecting variable values, and applying proper validation and error handling, both issues were resolved. The final version of the program now runs successfully, handles incorrect input safely, and produces accurate results for all products.

--------------------------------------------------
