import logging
from typing import List, Dict

from .models import Vehicle
from .settings import VEH_CPT, VEH_SDN, VEH_VAN, VEH_TRK, NO_FIT_FOUND


logger = logging.getLogger()

COMPACT = Vehicle(
    name=VEH_CPT, dimensions=[(24, 24, 36),], max_single_wt=50, max_total_wt=150
)

SEDAN = Vehicle(
    name=VEH_SDN,
    dimensions=[(24, 24, 36), (24, 24, 48)],
    max_single_wt=50,
    max_total_wt=250,
)

VAN = Vehicle(
    name=VEH_VAN, dimensions=[(120, 60, 60),], max_single_wt=70, max_total_wt=500
)

TRUCK = Vehicle(
    name=VEH_TRK, dimensions=[(150, 96, 84),], max_single_wt=500, max_total_wt=2000
)


def find_best_fit(items_list: List[Dict]) -> str:
    """
    This is a maximum dimension constraint validator, and a naive implementation of
    `First Fit Decreasing` Bin Packing Algorithm. As time constraints allow, the first
    TODO item is updating the algorithm.

    Args:
        items_list: Validated request data, a list of items to ship

    Returns:
        The smallest Vehicle that can fit all given shipment items

    Raises:
        ValueError: If any items are too tall or too heavy for the largest Vehicle
    """
    VEH_LIST = [COMPACT, SEDAN, VAN, TRUCK]
    total_wt = 0.0
    total_vl = 0.0
    sides = []
    max_wt_item = max(items_list, key=lambda x: x["weight"])
    max_ht_item = max(items_list, key=lambda x: x["height"])

    # Calculate max dimensions for items_list for comparison
    for i in items_list:
        sides.extend([i["length"], i["width"]])
        total_wt += i["weight"] * i["quantity"]
        total_vl += (i["length"] * i["width"] * i["height"]) * i["quantity"]
    longest_side = max(sides)
    total_wt = float("%.2f" % total_wt)  # TODO: Address floating point precision
    total_vl = float("%.2f" % total_vl)  # TODO: Address floating point precision
    logger.debug(f"Maximums: {max_wt_item}, {max_ht_item}, {total_wt}, {total_vl}")

    if max_wt_item["weight"] > TRUCK.max_single_wt:
        raise ValueError(
            f'Largest Vehicle single weight max exceeded with:{max_wt_item["weight"]}'
        )
    if max_ht_item["height"] > TRUCK.dimensions[0][2]:
        raise ValueError(
            f'Largest Vehicle height max exceeded with: {max_ht_item["height"]}'
        )
    if longest_side > TRUCK.longest_side:
        raise ValueError(
            f'Item with longest side of {longest_side} exceeds largest Vehicle max'
        )
    if total_wt > TRUCK.max_total_wt or total_vl > TRUCK.max_total_vl:
        raise ValueError(f"Items list total weight/vol exceeds largest Vehicle max")

    # Naive "bin packer." Needs eventual proper implementation.
    for vehicle in VEH_LIST[::-1]:
        logger.debug(f"Checking fit for vehicle: {vehicle.name}")
        if (
            max_wt_item["weight"] <= vehicle.max_total_wt
            and max_ht_item["height"] <= vehicle.max_total_ht
            and total_vl <= vehicle.max_total_vl
            and total_wt <= vehicle.max_total_wt
        ):
            logger.debug(f"{vehicle.name} can fit the items")
            best_fit = vehicle.name
    return NO_FIT_FOUND if best_fit is None else best_fit
