from src import TestingHelper

TEST_SIZES = [250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 4000]
PARALLELISM = 8
RANDOMIZE_TESTS = False

if __name__ == '__main__':
    # Main testing process
    if RANDOMIZE_TESTS:
        TestingHelper.runRandomTests(TEST_SIZES, parallelism=PARALLELISM)
    else:
        TestingHelper.runPredefinedTests(TEST_SIZES, parallelism=PARALLELISM)
    # Visualization for the additional testing process
    # if VISUALIZE_RESULTS:
    #     TestingHelper.renderGraph(graph, 'original', node_color='green')
    #     TestingHelper.renderGraph(mst_ser, 'mst_ser', node_color='red')
    #     TestingHelper.renderGraph(mst_par, 'mst_par', node_color='blue')
