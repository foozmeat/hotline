import json


class FiveCallsModel:

    def __init__(self, **kwargs):

        if kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def __str__(self):
        """ Returns a string representation of TwitterModel. By default
        this is the same as AsJsonString(). """
        return self.AsJsonString()

    def AsJsonString(self) -> str:
        """ Returns the TwitterModel as a JSON string based on key/value
        pairs returned from the AsDict() method. """
        return json.dumps(self.__dict__, sort_keys=True)


class Issue(FiveCallsModel):
    def __init__(self, **kwargs):
        self.id: str = None
        self.name: str = None
        self.script: str = None
        self.reason: str = None
        self.categories: [dict] = []
        self.contacts: [dict] = []
        self.inactive: bool = True
        self.link: str = None
        self.linkTitle: str = None
        self.slug: str = None

        super().__init__(**kwargs)

    def __str__(self):
        return f"({self.id}) {self.name}"


# class Category(FiveCallsModel):
#
#     def __init__(self):
#         self.name: str = None
#         self.issues = [Issue] = []
#
#         super().__init__()


# class Contact(FiveCallsModel):
#
#     def __init__(self, **kwargs):
#         self.id: str = None
#         self.name: str = None
#         self.phone: str = None
#         self.photoURL: str = None
#         self.party: str = None
#         self.state: str = None
#         self.reason = None
#         self.area = None
#         self.field_offices: [dict] = []
#
#         super().__init__(**kwargs)


# class ContactCache:
#
#     def __init__(self):
#         self.contacts = {}
#
#     def get(self, id: str):
#         return self.contacts.get(id, None)
#
#     def add(self, contact: Contact):
#         if not self.get(contact.id):
#             self.contacts[contact.id] = contact
