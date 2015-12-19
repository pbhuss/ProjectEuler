import yaml


def load_answers():
    with open('data/answers.yaml') as fp:
        return yaml.load(fp)


answers = load_answers()


def test_solutions(problem, solution_modules):
    assert solution_modules[problem].main() == answers[problem]
