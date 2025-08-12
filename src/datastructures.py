"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        new_member = {

            "id": self._generate_id(),
            "first_name": member.get("first_name"),
            "last_name": self.last_name ,
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers")
        }
        self._members.append(new_member)
        return new_member


    def get_member(self, id):
        for member in self._members:
            if id == member["id"]:
                return member, 200
        return None    

    def delete_member(self, id):
        member = self.get_member(id)
        if member:
            self._members.remove(member)
            return {"Done": True}
        return False


    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    


#Tenemos que crear 4 metodos los siguientes:
#-- GET  Obtén todos los miembros de la familia
#-- GET Recupera solo un miembro Devuelve el miembro de la familia para el cual id == member_id.
#-- Añadir (POST) un miembro, Agrega un nuevo miembro a la estructura de datos de la familia.
#ELIMINA un miembro Elimina el miembro de la familia para el cual id == member_id.