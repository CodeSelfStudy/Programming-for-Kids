"""Gives simple algebra problems to kids."""
from random import randint


OPERATIONS = {
    1: '+',
    2: '-'
}

class Problem():
    """Represents a basic algebra problem."""

    def __init__(self):
        """Initialize the algebra problem."""
        self.raw_data = self._calculate()

    def _generate(self):
        """Generate a problem."""
        x = randint(1, 20)
        y = randint(1, 20)
        operation = OPERATIONS[randint(1, 2)]
        problem = (operation, x, y)
        return problem
    
    def _calculate(self):
        """Return a dict with the problem info."""
        elements = self._generate()
        operator = elements[0]
        x = elements[1]
        y = elements[2]

        if operator == '+':
            answer = x + y
            question_text = 'x + {} = {}'.format(y, answer)
            answer_text = '{} + {} = {}'.format(x, y, answer)
        elif operator == '-':
            answer = x - y
            question_text = 'x - {} = {}'.format(y, answer)
            answer_text = '{} - {} = {}'.format(x, y, answer)
        return {
            'problem': elements,
            'question_text': question_text,
            'answer_text': answer_text,
            'answer': answer,
            'is_correct': None
        }

    @property
    def operator(self):
        return self.raw_data['problem'][0]

    @property
    def x(self):
        return self.raw_data['problem'][1]

    @property
    def y(self):
        return self.raw_data['problem'][2]

    @property
    def answer(self):
        return self.raw_data['answer']

    @property
    def answer_text(self):
        return self.raw_data['answer_text']

    @property
    def question_text(self):
        return self.raw_data['question_text']

    @property
    def is_correct(self):
        return self.raw_data['is_correct']

    def grade(self, user_answer):
        self.raw_data['is_correct'] = int(user_answer) == self.x

def main():
    problems = [Problem() for _ in range(10)]
    for p in problems:
        print(p.__dict__)
    print('____')

p = Problem()
current_answer = input('What is x in "{}"? '.format(p.question_text))
p.grade(current_answer)
print('Were you right? ({})'.format(p.is_correct))
print('The answer to "{}" is "{}".'.format(p.question_text, p.answer_text))


if __name__ == '__main__':
    main()
