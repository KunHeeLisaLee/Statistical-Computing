# /src/preprocess.py

import string
import os


def preprocess_text(source: str, from_file: bool = False) -> str:
    """
    Preprocess input text or text loaded from a file
    to meet the requirements:
    1. Convert upper case letters to lower case.
    2. Remove special characters except for spaces.
    3. Convert line breaks to spaces.
    4. Remove consecutive spaces.

    Input
    source: Input text or file path.
    from_file: If True, `source` is treated as a file path.

    Output
    return: Preprocessed and normalized text.
    """
    try:
        # Load text from file if `from_file` is True
        if from_file:
            if not os.path.exists(source):
                raise FileNotFoundError(f"File '{source}' does not exist.")
            with open(source, 'r') as file:
                text = file.read()
        else:
            text = source

        # Validate input text
        if not text.strip():
            raise ValueError("Input text is empty.")

        # 1.Convert to lowercase and 2.Remove special characters
        text = text.lower()
        text = ''.join(c for c in text if c in string.ascii_lowercase + ' ')
        # 3.Convert line breaks to spaces and 4.Remove consecutive spaces
        text = ' '.join(text.split())
        return text
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error reading file: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid text input: {e}")


# Example usage
if __name__ == "__main__":
    # Example: Preprocess text from a file
    processed_file_text = preprocess_text("some_text_encrypted.txt",
                                          from_file=True)
    print("Processed File Text:", processed_file_text)
