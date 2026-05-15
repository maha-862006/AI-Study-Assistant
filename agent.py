from tools.calculator import calculate
from tools.file_reader import read_file

class Agent:
    def process(self, user_input):
        
        if "calculate" in user_input:
            expression = user_input.replace("calculate", "").strip()
            return calculate(expression)

        elif "read file" in user_input:
            file_path = user_input.replace("read file", "").strip()
            return read_file(file_path)

        else:
            return "Try: 'calculate 2+3' or 'read file notes.txt'"