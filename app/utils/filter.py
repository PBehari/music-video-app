



def filter_data(data, filter_key='name', filter_val=''):
    """ Filter the data based on the given filter_key and filter_value

    Args:
        data (list): Data received from the API 
        filter_key (str, optional): The column in which we want to search. Defaults to 'name'.
        filter_val (str, optional): The value on which we want to search. Defaults to ''.

    Returns:
        generator object: The items that matches the given filter value
    """
    filtered_data = filter(lambda x: filter_val.lower() in x.get(filter_key, "").lower(), data)

    return filtered_data