"""
Sentence Counter (Programming Exercise 7)

This program asks the user to enter a paragraph. It uses a regular expression
with the look-ahead to find each sentence in the paragraph, even if
some sentences begin with numbers. Then it displays each sentence and the
total number of sentences.

Student: Maria Galante
Date: 2026-03-17
"""

# Import re
import re



def find_sentences(paragraph):
    """
    Description:
    This function finds each sentence in a paragraph using a regular
    expression with look-ahead.

    Parameters:
    paragraph (str) - paragraph entered by the user

    Variables:
    pattern (str) - regular expression pattern used to find sentences
    sentences (list) - list of sentences found in the paragraph

    Steps:
    1. Create the regex pattern.
    2. Use re.findall() with the right flags.
    3. Return the list of sentences found.

    Returns:
    list - list of sentences
    """

    # Pattern starts reading at a capital letter or number
    # and stops at ., !, or ? only if the next sentence starts
    # with a space and then a capital letter or number, or if
    # the paragraph ends
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Find all matching sentences in the paragraph
    sentences = re.findall(
        pattern,
        paragraph,
        flags=re.DOTALL | re.MULTILINE
    )

    # Return the list of sentences
    return sentences



def display_sentences(sentences):
    """
    Description:
    This function displays each sentence and the total sentence count.

    Parameters:
    sentences (list) - list of sentences found in the paragraph

    Variables:
    count (int) - number of sentences
    sentence (str) - one sentence from the list

    Steps:
    1. Count how many sentences are in the list.
    2. Loop through the list.
    3. Display each sentence.
    4. Display the total count.

    Returns:
    None
    """

    # Count how many sentences were found
    count = len(sentences)

    # Display each sentence on its own line
    print("\nSentences found:")
    for sentence in sentences:
        print(sentence.strip())

    # Display the total number of sentences
    print(f"\nSentence count: {count}")



def main():
    """
    Description:
    This function gets a paragraph from the user, finds the sentences,
    and displays each sentence along with the total count.

    Parameters:
    None

    Variables:
    paragraph (str) - paragraph entered by the user
    sentences (list) - list of sentences found in the paragraph

    Steps:
    1. Ask the user to enter a paragraph.
    2. Find the sentences in the paragraph.
    3. Display each sentence.
    4. Display the total sentence count.

    Returns:
    None
    """

    # Ask the user to enter a paragraph
    paragraph = input("Enter a paragraph: ")

    # Find the sentences in the paragraph
    sentences = find_sentences(paragraph)

    # Display the sentences and total count
    display_sentences(sentences)



# Run the program when the file is executed
if __name__ == "__main__":
    main()