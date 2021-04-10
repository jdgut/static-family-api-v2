from random import randint

class FamilyStructure:
    
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        
        #example list of members
        self._member = {
                "id" :  self._getRandomId(),
                "first_name" : first_name,
                "last_name" : last_name,
                "age"   : age,
                "children" : []
            }

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _getRandomId(self):
        return randint(0, 99999999)

    def getAllMembers(self):
        return [ self._members ]

    def getSingleMember(self, id):
        #write a loop that will loop through self._members
        for member in self._members:
            #write a conditional to check that member['id'] matches id passed
            if member['id'] == id:
                return member

        return None

    def getData(self):
       return self._member

    def addChild(self, childData):
        self._member['children'].append(childData)
        return