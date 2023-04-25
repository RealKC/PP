import os
from typing import Iterator, Tuple


def only_files_that_exist(file_paths: Iterator[str]) -> Iterator[str]:
    for path in file_paths:
        if os.path.exists(path):
            yield path


def only_text_files(file_paths: Iterator[str]) -> Iterator[str]:
    for path in file_paths:
        if path.endswith(".txt"):
            yield path


def count_lines(file_paths: Iterator[str]) -> Iterator[Tuple[str, int]]:
    for path in file_paths:
        with open(path) as file:
            yield path, sum(1 for _ in file)


def print_files(files: Iterator[Tuple[str, int]]):
    for file in files:
        print(f"{file[0]}: {file[1]}")


if __name__ == '__main__':
    paths = ["file1.txt", "file2.txt", "file3.txt"]
    print_files(
        count_lines(
            only_text_files(
                only_files_that_exist(
                    paths
                )
            )
        )
    )
    pass
