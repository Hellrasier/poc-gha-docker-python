def remove_dict_field(attribs: dict, key: str) -> dict:
    """
    Returns new dict without specified key

    Parameters
    ----------
    attribs : dict
        dictionary to remove key from
    key : str
        key of the dictionary to remove

    Returns
    ----------
        dict
            dictionary without specified key
    """
    copied = dict(attribs).copy()
    copied.pop(key, None)
    return copied