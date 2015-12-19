import yaml


ANSWERS_PATH = 'data/answers.yaml'


def load_answers():
    with open(ANSWERS_PATH) as fp:
        return yaml.load(fp)


answers = load_answers()


def test_solutions(problem, solution_modules):
    if problem not in answers:
        raise Exception('Missing answer for problem {} in {}'.format(
            problem, ANSWERS_PATH))
    assert solution_modules[problem].main() == answers[problem]
