import numpy as np
import argparse
import sys
import time

def test_polynomial(canonical, factors, value):
    factors_sign = factors[0]


    canonical_degree = canonical.shape[0]
    canonical_result = 0
    factors_result = 1

    for curr_degree in range(canonical_degree):
        canonical_result += canonical[-curr_degree - 1] * (value ** curr_degree)

    for curr_factor in range(1, factors.shape[0]):
        factors_result *= (value + factors[curr_factor])

    factors_result *= factors_sign

    return canonical_result, factors_result


def test_identity(canonical, factors, n_tests=1):
    polynomial_degree = canonical_polynomial.shape[0]
    test_values = np.random.rand(n_tests) * 100 * polynomial_degree

    for curr_test in range(n_tests):
        c_result, f_result = test_polynomial(canonical, factors, test_values[curr_test])
        if not np.isclose(c_result, f_result):
            return False, 1.0

    return True, 1 - 1 / (100 ** n_tests)



parser = argparse.ArgumentParser(description='Verify polynomial identity.')
parser.add_argument('input_file', metavar='input_file', type=str, help='File describing process')
args = parser.parse_args()

input_file = args.input_file

with open(input_file, 'r') as inputf:
    # Read canonical polynomial
    line = inputf.readline()
    if not line.strip():
        raise ValueError('Canonical polynomial not provided')
    else:
        try:
            canonical_polynomial = np.array([float(val) for val in line.split(',')])
        except Exception as e:
            raise ValueError('An exception occurred while processing the canonical polynomial: {}'.format(e))
    # Factors polynomial
    line = inputf.readline()
    if not line.strip():
        raise ValueError('Factors polynomial not provided')
    else:
        try:
            factors_polynomial = np.array([float(val) for val in line.split(',')])
        except Exception as e:
            raise ValueError('An exception occurred while processing the factors-polynomial: {}'.format(e))
    # Number of tests
    line = inputf.readline()
    polynomial_degree = canonical_polynomial.shape[0]
    
    if not line.strip():
        n_tests = int(polynomial_degree / 2)
    else:
        n_tests = int(line)
        if n_tests >= polynomial_degree:
            print('[WARN] If number of tests({}) is greater or equal than degree of polynomial({}) the algorithm couldn\'t be as efficient as expected.'.format(n_tests, polynomial_degree))






#canonical_polynomial = np.array([1, 0, -4])
#factors_polynomial = np.array([1, 2, -2])
start_time = time.time()
identical, probability = test_identity(canonical_polynomial, factors_polynomial, n_tests)
end_time = time.time()
print('Polynomials are{} identical with probability {:.10f}. Processing time: {:.5f}'.format('' if identical else 'n\'t', probability, end_time - start_time))


