"""
This is based largely on principles of charting.
"""
import pandas as pd
import itertools

class Person:
    _has_chart: bool = False
    _is_charted: bool = False
    _is_rep: bool = False
    _is_member: bool = False
    _groups: list = None
    
    # Identifiers:
    _name: str = None
    _first: str = None
    _last: str = None
    _membership_no: str = None

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
    _groups: list = []
    _people: list = []
    _identifiers: list =["_name", "_membership_number"]
    def populate_from_pandas(self, dataframe: pd.DataFrame):
        """
        Looks for a dataframe with the relevant
        """
        for person in dataframe.to_dict(orient="records"):
            print(person)
            self._people.append(Person(**person))

    def assign_groups(self):
        pass

    def check_unique(self, person, identifier):
        _id = getattr(person, identifier)

        matching_ppl = []
        for prsn in self.people:
            if getattr(prsn, identifier) == _id:
                matching_ppl.append(prsn)

        return len(matching_ppl)== 1

    @property
    def people(self):
        return list(itertools.chain.from_iterable([group.people for group in self._groups]) )

    def add_fact(self, list_of_facts: list):
        """
        Add facts to people
        """
        for person in self.people:
            for identifier in self._identifiers:
                if getattr(person, identifier) in list_of_facts:
                    if self.check_unique(person, identifier):
                        person.add_fact(fact, True)
                else:
                    person.add_fact(fact, False)

    def read_fact_file(self, fact_file: str):
        with open(fact_file, 'r') as f:
            fact_list = f.read().splitlines()
            self.add_fact(fact_list)
