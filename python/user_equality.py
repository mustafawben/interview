# TODO: Implement a User class which satisfies the below requirements.

import string
import itertools

class User(object):
    def __init__(self, name, fieldOfStudy):
        self.name = name
        self.fieldOfStudy = fieldOfStudy

    def examine_name(u1, u2):
        #splits into a list seperated by spaces
        u1_name_split = u1.name.rsplit(' ', 1)
        u2_name_split = u2.name.rsplit(' ', 1)
        
        #grabs the last name
        u1_last_name = u1_name_split[-1]
        u2_last_name = u2_name_split[-1]
        
        #compares lowercase last names
        if u1_last_name.lower() == u2_last_name.lower():
            if u1_name_split[0][0] == u2_name_split[0][0]:
                return True
        return False


    def __eq__(self, u2):
        """Override the default Equals behavior"""


        return User.examine_name(self, u2)


    def __ne__(self, u2):
        """Override the default Unequal behavior"""
        return not User.examine_name(self, u2)

assert u1 == u2, "you should implement a __eq__ op which handles first names and initials"
assert u1 != u3, "but require the last name to match exactly"
