from tools.calculator import calculate
from tools.file_reader import read_file

class Agent:

    def process(self, user_input):

        command = user_input.lower().strip()

        if command.startswith("calculate"):
            expression = user_input[len("calculate"):].strip()
            return calculate(expression)

        elif command.startswith("read file"):
            file_path = user_input[len("read file"):].strip()
            return read_file(file_path)

        else:
            return (
                "Unsupported command.\n"
                "Try:\n"
                "- calculate 2+3\n"
                "- read file notes.txt"
            )