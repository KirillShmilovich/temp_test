#include <iostream>
#include <vector>
#include <Eigen/Dense>
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
namespace py = pybind11;

double f_to_celsius(double f_temp);

double c_to_kelvin(double c_temp);

double f_to_kelvin(double f_temp);

std::vector<double> convert_vector(std::vector<double> &temp_vec);
//std::vector<double> convert_vector(py::list temp_vec);

Eigen::MatrixXd convert_matrix(Eigen::MatrixXd temp_matrix);