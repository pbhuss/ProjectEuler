import pkgutil
import re

import pytest
import problems


def load_solution_modules():
    module_map = dict()
    prefix = problems.__name__ + '.'
    for _, modname, _ in pkgutil.iter_modules(problems.__path__, prefix):
        problem_number = int(re.search('\d+', modname).group())
        module_map[problem_number] = __import__(modname, fromlist=['foo'])
    return module_map


def pytest_addoption(parser):
    solution_modules = load_solution_modules()
    parser.addoption(
        '--problems',
        action='store',
        nargs='*',
        type='int',
        choices=solution_modules.keys(),
        default =solution_modules.keys(),
        help='solution numbers to test (default: all)')


def pytest_generate_tests(metafunc):
    ids = [
        'Problem #%s' % problem_number
        for problem_number in metafunc.config.option.problems
    ]
    metafunc.parametrize('problem', metafunc.config.option.problems, ids=ids)


@pytest.fixture
def solution_modules():
    return load_solution_modules()
