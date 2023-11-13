"""
This is based largely on principles of charting.
"""

class Person:
    _name: str = None
    _has_chart: bool = False
    _is_charted: bool = False
    _is_rep: bool = False
    _is_member: bool = False
    _group_name: str = None
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value) 

    def add_fact(self, attr, fact):
        setattr(self, attr, fact)


class Group:
    _name: str = None
    _subgroups: list = []
    _parent: str = None
    _people: list = []

    @property
    def people(self):
        ppl = []
        ppl.extend(self._people)
        for group in self._subgroups:
            ppl.extend(group.people)
        return ppl

class Pitch:
    _name: str = None
    _groups: list = None
