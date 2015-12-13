import pkgutil
import re

import pytest
import yaml

import problems


def load_answers():
    with open('data/answers.yaml') as fp:
        return yaml.load(fp)


@pytest.fixture
def solution_modules():
    module_map = dict()
    prefix = problems.__name__ + '.'
    for _, modname, _ in pkgutil.iter_modules(problems.__path__, prefix):
        problem_number = int(re.search('\d+', modname).group())
        module_map[problem_number] = __import__(modname, fromlist=['foo'])
    return module_map


def test_answer_config(solution_modules):
    '''Check that we have answers for all solved problems.'''
    assert set(load_answers().keys()).issuperset(solution_modules.keys())


answers = sorted(
    load_answers().items(),
    key=lambda (problem_number, answer): problem_number)
ids = ['Problem #%s' % problem_number for (problem_number, answer) in answers]


@pytest.mark.parametrize('problem_number,answer', answers, ids=ids)
def test_solutions(solution_modules, problem_number, answer):
    assert solution_modules[problem_number].main() == answer
