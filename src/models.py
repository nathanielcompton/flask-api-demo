"""
In order to deal with the given API requirements/constraints, we can take advantage of
Python's `dataclass` for efficiency, ordering etc.

Ideally there should be some kind of "Vehicle Inventory" or "Configurables" service to
monitor available Vehicle inventory, min/max size constraints, etc.

Given more time, switch to a dedicated database and  Object-Relational Mapper.
"""
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass(order=True)
class Vehicle:
    """
    Keeping track of an automobile-type of item delivery vehicle.
    """
    name: str
    dimensions: List[Tuple]  # Each Tuple represents a (L,W,H) volume
    max_single_wt: float
    max_total_wt: float
    max_total_vl: float = field(init=False)
    max_total_ht: float = field(init=False)
    longest_side: float = field(init=False)

    def __post_init__(self):
        if len(self.dimensions) > 1:
            self.max_total_vl = sum(dim[0] * dim[1] * dim[2] for dim in self.dimensions)
            self.max_total_ht = max(dim[2] for dim in self.dimensions)
            sides = max([i[0], i[1]] for i in self.dimensions)
            self.longest_side = max(sides)
        else:
            self.max_total_vl = (
                self.dimensions[0][0] * self.dimensions[0][1] * self.dimensions[0][2]
            )
            self.max_total_ht = self.dimensions[0][2]
            self.longest_side = max(self.dimensions[0][0], self.dimensions[0][1])
