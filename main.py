import re
from pathlib import Path

import piexif  # See: https://github.com/hMatoba/Piexif

BASE_DIR = "./disk"

# Regex matching any string starting with four digits
year_regex_pattern = re.compile("^[0-9]{4}")

# All jpg-files in any subdir of BASE_PATH
files = [f for f in Path(BASE_DIR).glob("**/*.jpg")]


def find_year_in_path(path: Path) -> str | None:
    """
    Examines all parts of a filepath and checks for a 4-digit in each of the file's path-parts.
    The parts are examined in a depth first order and returns when a year is found.

    :param path: The path
    :return: year or None
    """
    for part in path.parent.parts:
        # Cycle each of the parts of a file's parent path
        if year_regex_pattern.match(part):
            # Return the 4-digit string when found
            return part[:4]
    return None


def find_year_in_exif(file_path: Path) -> str | None:
    if not file_path.is_file():
        return None

    exif_dict = piexif.load(f"{file_path}")
    if len(exif_dict["Exif"]) <= 1:
        return None

    for tag in exif_dict["Exif"]:
        # Loop all tags in the Exif-data to find the one named DateTimeOriginal
        if piexif.TAGS["Exif"][tag]["name"] == "DateTimeOriginal":
            # print(f"Found tag: {piexif.TAGS['Exif'][tag]['name']} with value: {exif_dict['Exif'][tag]}")
            # Found a date! Exif tag contains byte-coded strings, decode first and grab the first four digits
            return exif_dict["Exif"][tag].decode()[:4]


if __name__ == '__main__':
    for file in files:
        print("---------------------------------------------------------------------------------")
        print(f"Examining file: {file}")
        if year_from_path := find_year_in_path(file):
            print(f"Found year in path: {year_from_path}")

        if year_from_exif := find_year_in_exif(file):
            print(f"Found year in exif: {year_from_exif}")
