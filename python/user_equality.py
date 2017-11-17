# TODO: Implement a User class which satisfies the below requirements.

u1 = User(
    name="Kevin Zhang", 
    fieldOfStudy="EECS",
)

u2 = User(
    name="K. Zhang", 
    fieldOfStudy="EECS",
)

u3 = User(
    name="K. Smith", 
    fieldOfStudy="EECS",
)

assert u1 == u2, "you should implement a __eq__ op which handles first names and initials"
assert u1 != u3, "but require the last name to match exactly"
