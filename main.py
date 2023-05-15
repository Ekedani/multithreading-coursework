from src import TestingHelper

EXECUTE_TESTING = True
TEST_SIZES = [250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 4000]
PARALLELISM = 12
RANDOMIZE_TESTS = False

VISUALIZE_ALGORITHMS = False
VISUALIZATION_SIZE = 42

if __name__ == '__main__':
    # Main testing process
    if EXECUTE_TESTING:
        if RANDOMIZE_TESTS:
            TestingHelper.runRandomTests(TEST_SIZES, parallelism=PARALLELISM)
        else:
            TestingHelper.runPredefinedTests(TEST_SIZES, parallelism=PARALLELISM)
    # Visualization for the additional testing process
    if VISUALIZE_ALGORITHMS:
        TestingHelper.visualizeAlgorithms(VISUALIZATION_SIZE, parallelism=PARALLELISM)
