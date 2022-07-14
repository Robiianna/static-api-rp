
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name, members):
        self.last_name = last_name
        for member in members:
            self.add_member(member)

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if 'id' not in member or member["id"] < 1:
            member['id'] = self._generateId()
        if not hasattr(self, "_members"):
            self._members = []
        
        return self._members.append(member)
        

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member 

    def get_all_members(self):
        return self._members
