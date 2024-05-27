from requests import request
import pytest
import sys
import os
from unittest.mock import patch

@pytest.fixture(scope="module")
def pre_run(request, name, ver, nobanner, trace_verbose, silent, trace_trace, tracehub, targets):
    
    # for arg in sys.argv:
    #     print('Ori Arg: ', arg)

    # options = [sys.argv[1], ver, nobanner, trace_verbose, silent, trace_trace, tracehub, targets]
    # args = []

    # for arg in options:
    #     print('options: ', arg, ' Type: ', type(arg))
        
    #     if arg is not False and arg is not None:
    #         args.append(arg)

    # with patch.object(sys, 'argv', args):
    #     for arg in sys.argv:
    #         print('Arg: ', arg)

    

    print('PYTEST_CURRENT_TEST: ', os.getenv('PYTEST_CURRENT_TEST'))

    #https://stackoverflow.com/questions/34504757/get-pytest-to-look-within-the-base-directory-of-the-testing-script
    print('Request: ', request.fspath.dirname)
    temp = request.node.fspath

    if os.path.exists(temp):
        # Ok. The parent of sys.argv[0] might be a root of the Trace Hub software
        candidateDir = os.path.realpath(
            os.path.join(os.path.dirname(temp), r'../'),
        )
        # If it is a candidate, it has a 'bin' subdirectory
        assert os.path.isdir(os.path.join(candidateDir, r'Tutorial'))
            

@pytest.fixture(scope="module")
def pre_test():

    error = 0

    for arg in sys.argv:
        print('Arg (pre_test): ', arg)

    # print ("Name: %s" % name)
    # print ("ver: %s" % ver)
    # print ("nobanner: %s" % nobanner)
    # print ("trace_verbose: %s" % trace_verbose)
    # print ("silent: %s" % silent)
    # print ("trace_trace: %s" % trace_trace)
    # print ("tracehub: %s" % tracehub)
    # print ("targets: %s" % targets)

    if error == 0:
        return 0

def test_run(pre_run, pre_test):
    assert pre_test == 0

    print('Hello')

def test_2(pre_run, pre_test):

    assert pre_test == 0