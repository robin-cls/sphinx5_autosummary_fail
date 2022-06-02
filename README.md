Autosummary error with .so files in Sphinx 5.0
==============================================

You need to have an environment with sphinx, pybind and c++ installed

1. generate the .so with pybind
The pybind11 folder contains the [small example](https://pybind11.readthedocs.io/en/stable/basics.html#simple-example) from pybind documentation.

Go in the pybind11 folder and play the following command:
`c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) example.cpp -o example$(python3-config --extension-suffix)`

2. Copy the generated .so in the doc folder

3. Go in doc folder and play `sphinx-build . ../build`
