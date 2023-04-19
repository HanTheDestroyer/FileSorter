import os
import datetime


class Directory:
    def __init__(self, file_type, location, extensions=()):
        self.type = file_type
        self.location = location
        self.extensions = extensions


def sort_folders():
    # noinspection SpellCheckingInspection
    image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico", ".webp", ".tiff", ".svg", ".heif", ".apng",
                        ".raw", ".indd", ".ai", ".eps", ".psd", ".pdd", ".xd", ".xcf")
    # noinspection SpellCheckingInspection
    video_extensions = (".mp4", ".avi", ".mkv", ".wmv", ".flv", ".mov", ".mpg", ".mpeg", ".m4v", ".3gp", ".webm",
                        ".ogv", ".ts", ".mts", ".asf", ".rm", ".swf", ".vob", ".m2ts", ".divx")
    # noinspection SpellCheckingInspection
    audio_extensions = (".mp3", ".wav", ".aac", ".wma", ".m4a", ".flac", ".ogg", ".alac", ".aiff", ".opus", ".amr",
                        ".au", ".cda", ".mid", ".midi", ".ra", ".dts", ".ac3", ".ape", ".cue")
    # noinspection SpellCheckingInspection
    doc_extensions = (".doc", ".docx", ".pdf", ".txt", ".rtf", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".ods",
                      ".odt", ".odp", ".xps", ".epub", ".pages", ".numbers", ".key", ".txt", ".md")
    # noinspection SpellCheckingInspection
    archive_extensions = (".zip", ".rar", ".tar", ".gz", ".bz2", ".7z", ".iso", ".dmg", ".cab", ".jar", ".ace", ".lzh",
                          ".arj", ".gzip", ".uue", ".bzip2", ".z", ".war", ".ear", ".xar")
    # noinspection SpellCheckingInspection
    code_extensions = (".py", ".pyc", ".pyo", ".pyw", ".pyz", ".pyi", ".pyd", ".pyx", ".pxd", ".pxi", ".c", ".cpp",
                       ".cc", ".cxx", ".h", ".hh", ".hpp", ".hxx", ".java", ".class", ".sh")
    # noinspection SpellCheckingInspection
    torrent_extensions = (".torrent", ".tor", ".t", ".tix", ".torrentpart")

    # destinations
    dir1 = Directory("image", r"C:\Users\han\Images", image_extensions)
    dir2 = Directory("video", r"C:\Users\han\Videos", video_extensions)
    dir3 = Directory("audio", r"C:\Users\han\Audios", audio_extensions)
    dir4 = Directory("doc", r"C:\Users\han\Docs", doc_extensions)
    dir5 = Directory("archive", r"C:\Users\han\Archives", archive_extensions)
    dir6 = Directory("code", r"C:\Users\han\Codes", code_extensions)
    destination_directories = [dir1, dir2, dir3, dir4, dir5, dir6]

    # sources
    dir7 = Directory("variety", r"C:\Users\han\Desktop")
    dir8 = Directory("variety", r"C:\Users\han\Downloads")
    source_directories = [dir7, dir8]

    for source in source_directories:
        files = os.listdir(source.location)
        for file in files:
            for destination in destination_directories:
                if file.endswith(destination.extensions):
                    try:
                        os.rename(os.path.join(source.location, file), os.path.join(destination.location, file))
                    except FileExistsError:
                        new_file = "[" + \
                                   str(datetime.datetime.now()).replace(":", "-").replace(" ", "-").replace(".", "-")\
                                   + "]" + file
                        os.rename(os.path.join(source.location, file), os.path.join(destination.location, new_file))
            if file.endswith(torrent_extensions):
                os.remove(os.path.join(source.location, file))


if __name__ == "__main__":
    sort_folders()
