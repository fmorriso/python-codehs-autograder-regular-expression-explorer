from pathlib import Path


class FileInputOutput:
    """A class to help make reading and writing text files in Python a little less complex/daunting"""

    @staticmethod
    def write_text_file(filename: str, lines: list[str]) -> None:
        """write the list of text to the specified output file which will be overwritten each time """
        with open(filename, 'w') as f:
            f.writelines(lines)

    @staticmethod
    def read_text_file(filename: str) -> list[str]:
        """read the specified text file and return its contents as a list of strings"""
        lines: list[str] = []
        with open(filename, 'r') as f:
            print(f'{Path(f.name)}')
            while True:
                line: str = f.readline()
                if len(line) == 0:
                    break
                else:
                    lines.append(line)

        return lines
