"""
Spam Score Analyzer (Programming Exercise 2)

Student: Maria Galante
Date: 2026-02-12

Program Description:
This program asks the user to enter an email message, scans the message for
30 common spam words and phrases, calculates a spam score based on how many
are found, and then displays the score, the likelihood the message is spam,
and which words or phrases triggered the score.
"""

# Import re tool to search for spam keywords
import re

# Import typing tools for clearer function definitions
from typing import Dict, List, Tuple


def get_spam_triggers() -> List[str]:
    """
    Returns a list of 30 common words/phrases found in spam messages.

    Parameters:
    None

    Variables:
    triggers (list of str): The spam words/phrases list.

    Logic:
    1. Create a list of commonly used spam keywords and phrases.
    2. Return the list so it can be used to scan the user's message.

    Return:
    list[str]: The spam trigger words/phrases.
    """

    # Store commonly used spam words/phrases for scanning messages
    triggers = [
        "free",
        "free gift",
        "winner",
        "you are a winner",
        "prize",
        "congratulations",
        "urgent",
        "act now",
        "limited time",
        "offer expires",
        "last chance",
        "today only",
        "risk-free",
        "guaranteed",
        "buy now",
        "click here",
        "cash bonus",
        "make money",
        "get paid",
        "work from home",
        "credit",
        "loan",
        "debt",
        "no obligation",
        "verify your account",
        "password reset",
        "account suspended",
        "gift card",
        "wire transfer",
        "cryptocurrency",
    ]

    # Return the triggers so the analyzer can scan the user's message
    return triggers


def analyze_message(message: str, triggers: List[str]) -> Tuple[int, Dict[str, int]]:
    """
    Scans the user's message for spam trigger words and calculates a spam score.

    Parameters:
    message (str): The email message entered by the user.
    triggers (list[str]): The list of spam words/phrases to scan for.

    Variables:
    normalized (str): Lowercased version of the message for case-insensitive match.
    matches (dict[str, int]): Stores which spam words were found and how often.
    score (int): Accumulator that keeps track of total spam points.
    trigger (str): Individual spam trigger being checked.
    pattern (re.Pattern): Regex pattern used to search for matches.

    Logic:
    1. Convert message to lowercase for case-insensitive matching.
    2. Loop through each spam trigger word/phrase.
    3. Count how many times each appears in the message.
    4. Add each occurrence to the spam score.
    5. Store matches in a dictionary.
    6. Return the score and matches.

    Return:
    tuple[int, dict[str, int]]: Total spam score and dictionary of matches.
    """

    # Convert message to lowercase so matching works regardless of capitalization
    normalized = message.lower()

    # Dictionary stores which triggers appear and how many times
    matches: Dict[str, int] = {}

    # Accumulator for spam score
    score = 0

    # Loop through each trigger and count how many times it appears
    for trigger in triggers:
        # Escape special characters to keep trigger matching safe in regex
        escaped = re.escape(trigger.lower())

        # Build regex pattern to match full word/phrase only
        pattern = re.compile(rf"\b{escaped}\b")

        # Count how many times trigger appears
        count = len(pattern.findall(normalized))

        # Only record triggers that actually appear
        if count > 0:
            # Store count for this trigger
            matches[trigger] = count

            # Add occurrences to total spam score
            score += count

    # Return total score and matched triggers
    return score, matches


def rate_spam_likelihood(score: int) -> str:
    """
    Determines how likely a message is spam based on its spam score.

    Parameters:
    score (int): Total spam score calculated from triggers.

    Variables:
    None

    Logic:
    1. Compare score against threshold ranges.
    2. Return a descriptive likelihood message.

    Return:
    str: Spam likelihood rating.
    """

    # Determine spam likelihood using score ranges
    if score <= 2:
        return "Low likelihood of spam."
    if score <= 6:
        return "Moderate likelihood of spam."
    if score <= 10:
        return "High likelihood of spam."
    return "Very high likelihood of spam."


def get_user_message() -> str:
    """
    Collects a multi-line email message from the user.

    Parameters:
    None

    Variables:
    lines (list[str]): Stores each line entered by the user.
    line (str): A single line of user input.

    Logic:
    1. Prompt the user to enter an email message.
    2. Keep reading lines until the user enters a blank line.
    3. Combine all lines into one message string.
    4. Return the full message.

    Return:
    str: Complete email message entered by user.
    """

    # Prompt the user so they know how to enter and finish their message
    print("Enter the email message below.")
    print("Press ENTER on a blank line to finish.\n")

    # List stores each line so users can enter multi-line email content
    lines: List[str] = []

    # Continue reading input until user submits blank line
    while True:
        line = input()

        # Blank line means user finished typing message
        if line.strip() == "":
            break

        # Add line to list of message lines
        lines.append(line)

    # Combine all lines into one string so the analyzer can scan it
    message = " ".join(lines)

    # Return the full combined email message
    return message


def main() -> None:
    """
    Runs the spam analyzer program.

    Parameters:
    None

    Variables:
    message (str): Message entered by user.
    triggers (list[str]): Spam trigger list.
    score (int): Total spam score.
    matches (dict[str,int]): Words that triggered spam score.
    rating (str): Spam likelihood rating.

    Logic:
    1. Get message from user.
    2. Load spam trigger list.
    3. Analyze message and calculate score.
    4. Rate spam likelihood.
    5. Display results including matched triggers.

    Return:
    None
    """

    # Get email message from user
    message = get_user_message()

    # Stop program if user entered nothing
    if message.strip() == "":
        print("No message entered. Exiting program.")
        return

    # Load the list of spam trigger words and phrases
    triggers = get_spam_triggers()

    # Analyze message and calculate spam score
    score, matches = analyze_message(message, triggers)

    # Determine spam likelihood rating
    rating = rate_spam_likelihood(score)

    # Display the final results for the user
    print("\n--- Spam Analysis Results ---")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {rating}")

    # Show which trigger words/phrases trigger the spam score
    if matches:
        print("\nTriggers found:")

        # Sort results so output is easier to read
        for trigger, count in sorted(matches.items()):
            print(f"- {trigger} (count: {count})")
    else:
        # Print message when no triggers are found
        print("\nNo spam triggers were found in the message.")


# Run main only when file is executed directly
if __name__ == "__main__":
    main()
