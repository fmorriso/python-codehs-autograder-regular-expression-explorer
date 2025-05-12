import os, re, sys
from pathlib import Path
from importlib.metadata import version

from file_input_out_utilities import FileInputOutput


def remove_comments(text: str) -> str:
    """
    Remove all python comments from the specified text and return a string without those comments.
    reference: https://www.codeease.net/programming/python/python-remove-all-comments
    """
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|#[^\r\n]*$)"
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL)
    return regex.sub("", text)


def verify_remove_comments():
    code = """
    # This is a comment
    print("Hello, World!") # This is another comment
    """
    code += '\n"""docstring comment"""'
    print(f'before: {code=}')
    # Remove comments
    code_without_comments = remove_comments(code)
    # Output
    print(f'after: {code_without_comments=}')


def get_python_version() -> str:
    """ the version of python running this program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def get_package_version(package_name: str) -> str:
	return version(package_name)


def verify_text_file_read():
    """Verify that we can read a simple text file"""
    print(f'{Path.home()=}')
    print(f'{os.getcwd()=}')
    filename: str = 'simple.txt'
    full_path: str = f'{os.getcwd()}\\{filename}'
    print(f'{full_path=}')
    lines = FileInputOutput.read_text_file(full_path)
    for line in lines:
        print(line, end='')


def verify_text_file_write():
    """Verify that we can write a text file"""
    input_filename: str = 'simple.txt'
    input_filename_full_path: str = f'{os.getcwd()}\\{input_filename}'
    print(f'{input_filename_full_path=}')
    lines = FileInputOutput.read_text_file(input_filename_full_path)

    output_filename: str = f'simple-modified.txt'
    output_filename_full_path: str = f'{os.getcwd()}\\{output_filename}'
    output_text = """
p2 = Parallelogram()
print(f'{p.side1=}')
print(f'{p.side2=}')
print(f'{p.angle=}')
    """
    output_extra_lines = output_text.splitlines(True)
    print(f'{output_extra_lines=}')
    lines += output_extra_lines
    FileInputOutput.write_text_file(output_filename_full_path, lines)


def created_min_unique_instances(class_name: str, min_instances: int =2) -> bool:
    """return True if the required number of instances of the specified class appear in the code;
    otherwise, return False
    """
    # pattern = r'\b\w+\s*=\s*Parallelogram\s*\('
    pattern = f"\\b\\w+\\s*=\\s*{class_name}\\s*\\("
    # pattern = r'\b\w+\s*=\s*Parallelogram\s*\('
    # read test file of python code stored in a simple text file
    filename = 'simple-modified.txt'
    full_path: str = f'{os.getcwd()}\\{filename}'
    lines = FileInputOutput.read_text_file(full_path)
    # create fake student code without comments
    student_code_with_comments = "".join(lines)
    student_code_without_comments = remove_comments(student_code_with_comments)

    # Find all matches
    matches = re.findall(pattern, student_code_without_comments)
    if re.search(pattern, student_code_without_comments) is None:
        print('The patterns was not found')
    else:
        print(f'Found the pattern {len(matches)} times')

    # Print the matches
    print(f'{matches=}')
    #  logic to see how many unique instances were created
    var_names = {}
    for match in matches:
        pieces = match.split()
        print(f'{pieces=}')
        var_name = pieces[0]
        if var_name in var_names.keys():
            var_names[var_name] += 1
        else:
            var_names[var_name] = 1

    # print(f'{var_names}')
    # print(f'{len(var_names.keys())=}')

    if len(var_names.keys()) >= min_instances:
        msg = f'You created at least {min_instances} unique instances of {class_name} - good work'
        pass_fail = True
    else:
        msg = f'You must create at least {min_instances} unique instances of {class_name}'
        pass_fail = False

    return pass_fail, msg


def created_a_default_instance(class_name: str):
    """check to see there is an instance of the specified class name using the default constructor"""
    pattern = f'\\b\\w+\\s*=\\s*{class_name}\\s*\\(\\s*\\)'

    filename = 'default-constructor-test.txt'
    full_path: str = f'{os.getcwd()}\\{filename}'
    lines = FileInputOutput.read_text_file(full_path)
    # create fake student code without comments
    student_code_with_comments = "".join(lines)
    student_code_without_comments = remove_comments(student_code_with_comments)

    # Search for at least one match
    if re.search(pattern, student_code_without_comments) is None:
        msg = f'You must create at least one instance of {class_name} using the default constructor'
        pass_fail = False
    else:
        msg = f'You created at least one instance of {class_name} using the default constructor - good work'
        pass_fail = True

    return pass_fail, msg


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    print(f'PathLib version {get_package_version("PathLib")}')

    # test_remove_comments()
    # test_file_read()
    # test_file_write()

    result, message = created_min_unique_instances('Parallelogram', 2)
    print(f'{message}  Passed? = {result}')
    
    result, message = created_a_default_instance('Parallelogram')
    print(f'{message}  Passed? = {result}')