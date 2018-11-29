--RUNNING THE PROGRAM--

Run `pip3 install .` within the myCminus folder.  This will install the necessary dependencies.

This packages requires 'antlr4-python3-runtime' to run.  If the above install does not work, run `pip3 install antlr4-python3-runtime`

Pass a test file to myCMinus.py to generate a CFG and Live Variable analysis.

To pass a test file run `python3 myCMinus.py inputFile` within the myCMinus/ folder

Default test files are provided in the test_files/ subdirectory

--REPORT--

The listener class labels each of the elementary blocks. As the listener walks the AST, each prints each block with its label.

The GenListenerand KillListener classes are imported from the genSet.py file and generate the gen and kill sets (respectively) which are printed onto the console.

The labeling from the listener class, and the gen and kill sets are then passed onto the analyzer class which generates the live variable equations.

The control flow graph is represented by a set of edges.

All five tests with screenshots are located in the test_files folder. Each of these files represent different functions in our myCminus language.


