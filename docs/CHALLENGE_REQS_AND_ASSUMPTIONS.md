# Coding Demo: Business Requirements & Assumptions

## Challenge Description
Create an API which calculates an appropriately sized transport vehicle for a given
array of shipment item ready to be shipped.

For this exercise, assume each shipment item within the input array will have:
* Length, Width and Height, in inches
* Weight, in lbs
* Quantity of that item (> 1 means duplicate items)

Given those inputs, the API server should return the text name of the required
vehicle to transport those items. The enumerated vehicles are as follows:

* Compact
* Sedan
* Van
* Truck

Each vehicle will have internal volumetric maximums, a single item weight maximum
and a total item weight maximum, as follows:

| Name    | Length x Width x Height | Single Item Wt Max | Total Item Wt Max |
| ------- |:-----------------------:|:------------------:|:-----------------:|
| Compact |        24x24x36         |         50         |        150        |
| Sedan   |   24x24x36 + 24x24x48   |         50         |        250        |
| Van     |        120x60x60        |         70         |        500        |
| Truck   |        150x96x84        |        500         |       2000        |

For this exercise, also assume that any "height" must remain non-rotational (i.e. an item's
height must remain upright, while the length and width may interchange.)

An input item with dimensions 12x20x40 and a weight of 51 would go into a Van due to its
single item weight constraint. If the same item had a height of 61, it would go into a
Truck due to the Van's max height constraint.

## Implementation Details & Assumptions

For clarity, let's make a few assumptions:

1. Both the shipment items objects and the shipping vehicles objects have three-dimensional
volumes measured as [parallelpipeds]. Since this is a real world use case, we can safely
assume these are all standard rectangular prisms.
2. This challenge seems to be a modified version of the [Bin Packing Problem]. We'll
need to account for four dimensions: LxWxH volume, and weight.
3. Because this problem is [combinatorial] and [NP-hard], it will be best to choose a
heuristic algorithm. My current plan is to implement a first-fit decreasing algorithm.

[//]: # (These are reference links are hidden during Markdown file build.)

[parallelpipeds]: https://en.wikipedia.org/wiki/Parallelepiped
[Bin Packing Problem]: https://en.wikipedia.org/wiki/Bin_packing_problem
[combinatorial]: https://en.wikipedia.org/wiki/Combinatorics
[NP-hard]: https://en.wikipedia.org/wiki/NP-hardness
