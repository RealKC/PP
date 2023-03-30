import os
import string

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUGGING = False


class GenericFile:
    def get_path(self):
        raise NotImplementedError(f'get_path() not implemented')

    def get_freq(self):
        raise NotImplementedError(f'get_freq() not implemented')


class TextASCII(GenericFile):
    def __init__(self, path, freq):
        self.path_absolut = path
        self.frecvente = freq

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class TextUNICODE(GenericFile):
    def __init__(self, path, freq):
        self.path_absolut = path
        self.frecvente = freq

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class Binary(GenericFile):
    def __init__(self, path, freq):
        self.path_absolut = path
        self.frecvente = freq

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente


class XMLFile(TextASCII):
    def __init__(self, path, freq, contents: bytes):
        super().__init__(path, freq)

        first_tag_start = contents.find(ord('<'))
        first_tag_end = contents.find(ord('>'), first_tag_start) + 1

        self.first_tag = contents[first_tag_start:first_tag_end]

    def get_first_tag(self):
        return self.first_tag


class BMPFile(Binary):
    def __init__(self, path, freq, contents):
        super().__init__(path, freq)

        # https://en.wikipedia.org/wiki/BMP_file_format#File_structure

        if len(contents) < 47:
            raise RuntimeError(f'File too small to be BMP (got {len(contents)})')

        if contents[0:2] != b'BM':
            raise RuntimeError(f'Did not find BM header (got {contents[0:2]}')

        self.width = int.from_bytes(contents[18:22], byteorder='little')
        self.height = int.from_bytes(contents[22:26], byteorder='little')
        self.bpp = int.from_bytes(contents[26:28], byteorder='little')

    def show_info(self):
        print(f'BMP file {self.width}x{self.height} with bpp={self.bpp}')


def compute_frequencies(contents: bytes):
    table = [0] * 256

    for idx in range(len(contents)):
        table[contents[idx]] += 1

    return table


def get_file_type_from_frequencies(freq, path, contents):
    total = sum(freq)

    if total == 0:
        return None

    printable_freq = 0
    nonprintable_freq = 0
    notascii_freq = 0
    for idx in range(len(freq)):
        if freq[idx] == 0:
            continue

        if idx > 128:
            notascii_freq += 1
        elif chr(idx) in string.printable:
            printable_freq += 1
        else:
            nonprintable_freq += 1

    if DEBUGGING:
        print(f'for {path} printable={printable_freq}, nonprintable={nonprintable_freq}, not ascii={notascii_freq}')

    # "recvențe mari pentru caractere în limitele {9,10,13,32...127} și
    # frecvențe foarte mici pentru caractere în limitele {0...8,11,12,14,15...31, 128...255}"
    if printable_freq / 2 > (nonprintable_freq + notascii_freq):
        if freq[ord('<')] > 5 and freq[ord('<')] == freq[ord('>')]:
            # probably an xml file
            return XMLFile(path, freq, contents)
        return TextASCII(path, freq)

    if 0.25 <= (freq[0] / total) <= 0.35:
        return TextUNICODE(path, freq)

    try:
        bmp = BMPFile(path, freq, contents)
        return bmp
    except RuntimeError as e:
        if DEBUGGING:
            print(e)

        return Binary(path, freq)


def main():
    result_files = []

    for root, subdirs, files in os.walk(ROOT_DIR):
        for file in os.listdir(root):
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                f = open(file_path, 'rb')
                try:
                    content = f.read()
                    freq = compute_frequencies(content)
                    result_files.append(get_file_type_from_frequencies(freq, file_path, content))
                finally:
                    f.close()

    for idx in range(len(result_files)):
        if result_files[idx] is None:
            continue

        print(f'{type(result_files[idx]).__name__}: {result_files[idx].path_absolut}')

        if isinstance(result_files[idx], BMPFile):
            print('\t', end='')
            result_files[idx].show_info()
        elif isinstance(result_files[idx], XMLFile):
            print(f'\t with first tag: {result_files[idx].get_first_tag()}')


if __name__ == "__main__":
    main()
