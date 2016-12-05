Running the test environments:

1. Automated Test Execution (requires Python 2.7):

Requires files test_cases.py, interface.py and run.py

To execute all tests, execute the run.py file for example via terminal:

	python run.py

The results will be shown after full execution (about 2-3 minutes)

2. TorXakis:

Requires files scanflow_procdef.txs

To execute tests, run torxakis on the file, specify what model
and SUT to use and specify how many tests to run:

	torxakis scanflow_procdef.txs
	tester Mod Sut
	test x

Where x is desired amount of tests