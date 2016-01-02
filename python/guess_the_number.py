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
        
        def generate():
            """Generate a problem."""
            x = randint(1, 20)
            y = randint(1, 20)
            operation = OPERATIONS[randint(1, 2)]
            problem = (operation, x, y)
            return problem
    
        self.elements = generate()
    
    def calculate(self):
        """Return a dict with the problem info."""
        operator = self.elements[0]
        x = self.elements[1]
        y = self.elements[2]

        if operator == '+':
            answer = x + y
            question_text = 'x + {} = {}'.format(x, y, answer)
            answer_text = '{} + {} = {}'.format(x, y, answer)
        elif operator == '-':
            answer = x - y
            question_text = 'x - {} = {}'.format(x, y, answer)
            answer_text = '{} - {} = {}'.format(x, y, answer)
        return {
            'problem': self.elements,
            'question_text': question_text,
            'answer_text': answer_text,
            'answer': answer
        }
