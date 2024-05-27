import pytest

@pytest.fixture
def input_value():
    input = 39
    return input

def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="default name")
    parser.addoption('--ver', action='store_true', help='Display version of ITH')
    parser.addoption('--nobanner', action='store_true', help='Disable display of banner.')
    parser.addoption('--trace_verbose', action='store_true', help='Extremely detailed tracing information is enabled.')
    parser.addoption('--silent', action='store_true', help=('Nearly silent, progress information only about the tracehub detection procedure.'))
    parser.addoption('--trace_trace', action='store_true', help='Stack Debug Trace information is enabled.')
    parser.addoption('--tracehub',
            help=(
                'Select a specific installed instance of the TraceHub software. TRACEHUB is the '
                'root directory which is the parent of both "bin" and "targets". This optional '
                'value overrides first a check of the NPK_ROOT environment variable and then a'
                ' search of PATH (using PATHEXT on Windows).'
            ), default=None)
    parser.addoption('--targets', help=("Add an additional targets folder to include in the PVSS tree."), default=None)

def pytest_generate_tests(metafunc):
    
    options = {
        "name" : metafunc.config.option.name,
        "ver" : metafunc.config.option.ver,
        "nobanner" : metafunc.config.option.nobanner,
        "trace_verbose" : metafunc.config.option.trace_verbose,
        "silent" : metafunc.config.option.silent,
        "trace_trace" : metafunc.config.option.trace_trace,
        "tracehub" : metafunc.config.option.tracehub,
        "targets" : metafunc.config.option.targets
    }
    
    for key in options.keys():
        if key in metafunc.fixturenames and options.get(key) is True:
            metafunc.parametrize(key, ["--" + key], scope="module")
        elif key in metafunc.fixturenames and options.get(key) is not None:
            metafunc.parametrize(key, [options.get(key)], scope="module")
        elif key in metafunc.fixturenames and options.get(key) is None:
            metafunc.parametrize(key, [None], scope="module")
        

    # option_value = metafunc.config.option.name

    # print('value: ', option_value)

    # if 'name' in metafunc.fixturenames and option_value is not None:
    #     metafunc.parametrize("name", [option_value])

def pytest_report_header(config):
    return "project deps: mylib-1.1"



# https://stackoverflow.com/questions/69501136/how-to-customize-the-passed-test-message-in-a-dynamic-way
# def pytest_report_teststatus(report, config):
#     if report.when == 'call':
#         short_outcome = f'{percentage * 100}%'
#         long_outcome = f'SQUEEZED BY {percentage * 100}%'
#         return report.outcome, short_outcome, long_outcome

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_logstart(nodeid, location):

#     print()


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# #@pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):

#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "teardown":
#         if rep.failed:
#             return ("FAILED____________________")
#         elif rep.passed:
#             return ("PASSED____________________")

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):

#     outcome = yield
#     report = outcome.get_result()

#     report.nodeid = report.nodeid[-5:]

import itertools as it
import re


def grouper(item):
    return item.nodeid#[:item.nodeid.rfind('[')]

def pytest_collection_modifyitems(items):

    max = 0

    for item in items:
        nodeid = item.nodeid
        nodeid = nodeid.split("[")[0]
        nodeid = nodeid.rpartition("::")[2]
        
        if len(nodeid) > max:
            max = len(nodeid)
            #     print(max)

    for item in items:
        nodeid = nodeid.ljust(max + 10, " ")
        item._nodeid = nodeid

    # for _, group in it.groupby(items, grouper):
            # nodeid = item.nodeid
            # nodeid = nodeid.split("[")[0]
            # nodeid = nodeid.rpartition("::")[2]

            # if len(nodeid) > max:
            #     max = len(nodeid)
            #     print(max)

            #item._nodeid = name
            #re.sub(r'\[.*\]', '_{:02d}'.format(i + 1), item.nodeid)