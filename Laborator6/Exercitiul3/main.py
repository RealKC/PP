import os


class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Format nesuportat")
        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("se canta {} un mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("se canta {} un wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("se canta {} un ogg".format(self.filename))


class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Format necunoscut")
        self.filename = filename

    def play(self):
        print("se canta {} un flac".format(self.filename))


if __name__ == '__main__':
    files = []
    validators = [WavFile, OggFile, FlacFile, MP3File]

    done = False
    while not done:
        filename = input('File: ')

        if not os.path.isfile(filename):
            print(f'File does not exist!! ({filename})')
            continue

        for validator in validators:
            try:
                files.append(validator(filename))
                break
            except Exception:
                continue

        ch = input('Done? [y/n]')
        done = ch == 'y'

    for file in files:
        file.play()