import copy
from abc import ABC, abstractmethod


class File(ABC):
    title: str = ""
    author: str = ""
    paragraphs: list[str]

    def __init__(self):
        self.paragraphs = []

    @abstractmethod
    def read_file_from_stdin(self):
        self.title = input("title = ")
        self.author = input("author = ")
        self.paragraphs = []
        paragraph_count = int(input("number of paragraphs = "))
        for i in range(paragraph_count):
            self.paragraphs.append(input(f"paragraph #{i + 1} = "))

    @abstractmethod
    def print(self):
        pass


class HTMLFile(File):
    def __init__(self):
        super().__init__()

    def read_file_from_stdin(self):
        super().read_file_from_stdin()

    def print_html(self):
        print(f"""
<html>
    <head>
        <title>{self.title}</title>
    </head>
    <body>
    <h1>{self.title}</h1>
    <h2>by {self.author}</h2>
        """)

        for paragraph in self.paragraphs:
            print(f"    <p>{paragraph}</p><br>")

        print("    </body>\n</html>")

    def print(self):
        self.print_html()


class JSONFile(File):
    def __init__(self):
        super().__init__()

    def read_file_from_stdin(self):
        super().read_file_from_stdin()

    def print_json(self):
        print(f"""
{{
    "title": "{self.title}",
    "author": "{self.author}",
    "paragraphs": [
""")
        first = True
        for paragraph in self.paragraphs:
            print(f'        {"," if not first else ""}\n"{paragraph}"', end="")
            first = False

        print("\n    ]\n}")

    def print(self):
        self.print_json()


class TextFile(File, ABC):
    template: str = ""

    def __init__(self, template):
        super().__init__()
        self.template = template

    def read_file_from_stdin(self):
        super().read_file_from_stdin()

    @abstractmethod
    def print_text(self):
        print(f"Template: {self.template}\nTitlu: {self.title}\nAutor: {self.author}, Continut:")
        for paragraph in self.paragraphs:
            print(paragraph)

    def print(self):
        self.print_text()

    def clone(self):
        return copy.copy(self)


class ArticleTextFile(TextFile):
    def __init__(self):
        super().__init__("Article")

    def print_text(self):
        print(f"\t\t{self.title}")
        print(f"\t\t\tby {self.author}")

        for paragraph in self.paragraphs:
            print(paragraph)


class BlogTextFile(TextFile):
    def __init__(self):
        super().__init__("Blog")

    def print_text(self):
        print(self.title)
        for paragraph in self.paragraphs:
            print(paragraph)
        print()
        print(f"Written by {self.author}")


class FileFactory:
    @staticmethod
    def factory(file_type: str) -> File:
        match file_type:
            case "html":
                return HTMLFile()
            case "json":
                return JSONFile()
            case "article":
                return ArticleTextFile()
            case "blog":
                return BlogTextFile()


def main():
    for ftype in ["html", "json", "article", "blog"]:
        file = FileFactory.factory(ftype)
        file.read_file_from_stdin()
        file.print()


if __name__ == "__main__":
    main()
