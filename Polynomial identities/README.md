# Polynomial indentity

## Description

Random algorithm which verifies two polynomials identity. The first polynomial must be in canonical form and the second one must be as factors product.

For exmaple:

The first polynomial could be:

![\Large x^2 + 5x + 6](https://latex.codecogs.com/svg.latex?x^2+5x+6)

And the second one could be:

![\Large (x + 3)(x + 2) ](https://latex.codecogs.com/svg.latex?(x%20+%203)(x%20+%202))


## Usage

### Generals

As am input for programs, you must fed a file to any program, the file format is as described below:

- The first line in the file must contain the canonical polynomial terms comma-separated.

- The second line in the file must contain the factors from factor-form polynomial terms comma-separated.

- The third line is optional, and should contain the number of repetitions for the algorithm. 

### File example

The file test included in this repository is an example of how the file should be structured.

### Implementation

Either python or C++ implementation gets as first (and unique) parameter the filename from where the polynomials will be read. If the number of repetitions is not specified the default value will be the polynomial grade divided by two.

For running the python test you can run next commands:

    $ python poly_identity.py test


For running the C++ test you can run next commands:

    $ g++ poly_identity.cpp -o poly_identity.out
    $ ./poly_identity.out test



