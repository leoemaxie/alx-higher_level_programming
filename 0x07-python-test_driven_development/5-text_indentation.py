#!/usr/bin/python3
"""Text Indentation Module: Defines {text_indentation} function"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', ? and :

    :param text: The text to indent. {text} must be a string, otherwise a
    TypeError exception is raised
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf_text = []
    for c in text:
        buf_text.append(c)
        if c in "?:.":
            print(''.join(buf_text).strip(), end="\n\n")
            buf_text = []

    if text[-1] not in "?:.":
        print(''.join(buf_text).strip())
