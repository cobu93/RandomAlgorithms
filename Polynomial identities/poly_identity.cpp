#include <iostream>
#include <chrono> 
#include <fstream>
#include <string>
#include <random>
#include <vector>
#include <cmath>
#include <sstream>
#include <iomanip>

#define REL_TOL 1e-05
#define ABS_TOL 1e-08

using namespace std; 

void test_polynomial(
    vector<double> canonical, 
    vector<double> factors, 
    double value, 
    double& canonical_result, 
    double& factors_result
    ){
    
    int factors_sign = (int)factors[0];


    int canonical_degree = canonical.size();
    canonical_result = 0;
    factors_result = 1;

    for(int curr_degree=0; curr_degree < canonical_degree; curr_degree++)
        canonical_result += canonical[canonical_degree - curr_degree - 1] * pow(value, curr_degree);

    for(int curr_factor=1;  curr_factor < factors.size(); curr_factor++)
        factors_result *= (value + factors[curr_factor]);

    factors_result *= factors_sign;
    }


void test_identity(
    vector<double> canonical, 
    vector<double> factors, 
    bool& identical,
    double& probability,
    int n_tests=1){

    int polynomial_degree = canonical.size();

    default_random_engine generator;
    uniform_int_distribution<int> distribution(1, 100 * polynomial_degree);

    double c_result, f_result;

    for(int curr_test=0; curr_test < n_tests; curr_test++){
        test_polynomial(canonical, factors, distribution(generator), c_result, f_result);
        
        if (fabs(c_result - f_result) > ABS_TOL + REL_TOL * fabs(f_result)){
            identical = false;
            probability = 1.0;

            return;
        }
    }

    identical = true;
    probability = 1 - 1 / pow(100, n_tests);
    }

void split_transform(string& line, vector<double>& vec){
    stringstream poly(line);
    string segment;
                        
    while(getline(poly, segment, ',')){
        vec.push_back(stod(segment));
    }
}


int main(int argc, char** argv) 
{ 

    if(argc < 2){
        cout << "poly_identity.cpp <input_file>" << endl;
        cout << "poly_identity.cpp: error: the following arguments are required: input_file" << endl;
        return 1;
    }

    auto input_file = argv[1];

    ifstream inputf(input_file, ios::in);
    string line;
    vector<double> canonical_polynomial;
    vector<double> factors_polynomial;
    int n_tests = 0;

    // Read canonical polynomial
    if(!getline(inputf, line)){
        throw "Canonical polynomial not provided";
    }
    else{
        try{
            split_transform(line, canonical_polynomial);
        }
        catch(exception& e){
            throw string("An exception occurred while processing the canonical polynomial: ") + e.what();
        }
    }

    // Factors polynomial
    if(!getline(inputf, line)){
        throw "Factors polynomial not provided";
    }
    else{
        try{
            split_transform(line, factors_polynomial);
        }
        catch(exception& e){
            throw string("An exception occurred while processing the factors-polynomial: ") + e.what();
        }
    }
    
    // Number of tests
    int polynomial_degree = canonical_polynomial.size();
    if(!getline(inputf, line)){
        n_tests = (int)(polynomial_degree / 2);
    }
    else{
        n_tests = stoi(line);
        if(n_tests >= polynomial_degree){
            cout << "[WARN] If number of tests(" << n_tests << ") is greater or equal than degree of polynomial(" << polynomial_degree << ") the algorithm couldn't be as efficient as expected." << endl;
        }

    }

    bool identical;
    double probability;

    auto start_time = chrono::high_resolution_clock::now();
    test_identity(canonical_polynomial, factors_polynomial, identical, probability, n_tests);
    auto end_time = chrono::high_resolution_clock::now();
    chrono::duration<double> time_span = chrono::duration_cast<chrono::duration<double>>(end_time - start_time);
    cout << "Polynomials are" << (identical? "": "n't");
    cout << " identical with probability " << setprecision(10) << probability;
    cout << ". Processing time: " << setprecision(5) << time_span.count() << endl;

    return 0; 
} 



