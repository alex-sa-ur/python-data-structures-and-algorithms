"""
Author: Alejandro Sanchez Uribe
Date: 13 Dec 19
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def de_group(group):
    all_users = []

    for sub_group in group.get_groups():
        all_users.extend(de_group(sub_group))

    all_users.extend(group.get_users())

    return all_users


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user: user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True

    all_members_in_sub_groups = de_group(group)
    return user in all_members_in_sub_groups


# test cases below

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent))
# returns True since the user is in the sub_child group, which is a subgroup of parent
print(is_user_in_group(sub_child_user, child))
# returns True since the user is in the sub_child group, which is a subgroup of child
print(is_user_in_group(sub_child_user, sub_child))
# returns True since the user is in the sub_child group
print(is_user_in_group('', parent))
# returns False since the user does not exist
print(is_user_in_group(None, sub_child))
# returns True since the user does not exist
print(is_user_in_group(1000, sub_child))
# returns True since the user does not exist
