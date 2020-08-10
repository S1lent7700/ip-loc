from modules.meta._meta import Lists, Dictionaries
from modules.meta.colors import Normal as n


class StringUtil:

    def __init__(self):
        # Editable defaults -- The very first function will not be utilizing these
        # Values.
        self.string = ""
        self.dict = {}
        self.list = []

    def print_all_info(self):
        l = Lists()
        d = Dictionaries()

        for key in l.info_keys:
            # Set the string key value to the key iterated from the info key list
            # This variable value can then be safely supplied to the dictionary to
            # print out that dictionaries key value
            nkey = key
            # Print the key and dictionary value
            print(n.ws + key + ": " + n.ys + d.prog_info_dict[nkey] + n.ce)
