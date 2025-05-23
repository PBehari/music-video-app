
class Sorting:

    def sort_data(self, data, sort_by="name", reverse=False):
        """ Sort the data on the given key and sort order

        Args:
            data (generator object): Generator object received from the API
            sort_by (str, optional): Key to sort on. Defaults to "name".
            reverse (bool, optional): Sort order. Defaults to False (Ascending).

        Returns:
            Sorted list: The sorted list based on the given key and sort order
        """
        return sorted(data,
                      key=lambda x: str(x.get(sort_by, "")).strip().lower(),
                      reverse=reverse)