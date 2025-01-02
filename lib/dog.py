APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 1 and 25 characters in length"""
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
