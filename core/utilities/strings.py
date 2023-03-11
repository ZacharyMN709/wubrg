def isolate_string(text: str, truncate_from: str = None, truncate_to: str = None):
    """
    Isolates a portion of a string based on the first found instances of a from and to string.
    :param text: The text to isolate a string from.
    :param truncate_from: The string to start isolating from.
    :param truncate_to: The string to isolate up to.
    :return:
    """
    if truncate_from:
        start_idx = text.index(truncate_from) + len(truncate_from)
    else:
        start_idx = None

    if truncate_to:
        end_idx = text.index(truncate_to, start_idx)
    else:
        end_idx = None

    truncated_text = text[start_idx:end_idx].strip()
    return truncated_text
