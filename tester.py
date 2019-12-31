import os
from runpy import run_path
import glob

work_dir = "/home/test_system"

def run_test(task = 1, solution = './solution.py'):
    result = '';
    dirpath = work_dir + f"/tasks/{task}/"
    score = 0
    config_file = dirpath + "config.py"
    settings = run_path(config_file)

    test_dir = dirpath + "tests/"
    test_files = glob.glob(test_dir + "*.txt")
    test_count = int(len(test_files) / 2)
    score_one_test = settings['max_score'] / test_count

    for i in range(test_count):
        solution_result = os.popen(f'python3 {solution} < {test_dir}t{i+1}.txt').read()

        with open(f'{test_dir}a{i+1}.txt', 'r', encoding="utf-8") as solution_answer_file:
            solution_answer = solution_answer_file.read()

        if solution_result == solution_answer:
            score += score_one_test
            result += f"Test {i+1} - OK\n"
        else:
            result += f"Test {i+1} - wrong answer\n"
        
    return result + f"Result score - {score}"