from pathlib import Path

from main import find_year_in_path, find_year_in_exif


def test_find_year_in_path():
    # Should find the first 4-digit sequence
    my_path = Path("/Users/wouter/Documents/fotos/1976/Wouter geboren/1506_BLA_iurhga.jpg")
    year = find_year_in_path(my_path)
    assert year == "1976"


def test_find_year_in_path_subdir():
    my_path = Path("/Users/wouter/Documents/fotos/1976 06 15 Wouter geboren/1506_BLA_iurhga.jpg")
    year = find_year_in_path(my_path)
    assert year == "1976"


def test_find_year_in_path_in_both():
    # Should find the first 4-digit sequence
    my_path = Path("/Users/wouter/Documents/fotos/1976/0001 Wouter geboren/1506_BLA_iurhga.jpg")
    year = find_year_in_path(my_path)
    assert year == "1976"


def test_no_year_in_path_in_both():
    # Shouldn't find a year
    my_path = Path("/Users/wouter/Documents/fotos/Wouter geboren/1506_BLA_iurhga.jpg")
    year = find_year_in_path(my_path)
    assert not year
    my_path = Path("/Users/wouter/Documents/fotos/Wouter 1976 geboren/1506_BLA_iurhga.jpg")
    year = find_year_in_path(my_path)
    assert not year
    my_path = Path("/Users/wouter/Documents/fotos/1506_BLA_iurhga.jpg")
    year = find_year_in_path(my_path)
    assert not year


def test_find_year_in_exif():
    file_with_exif = Path("./disk/2023 Hondjes/20230207_093811.jpg")
    year = find_year_in_exif(file_with_exif)
    # exif data contains a date in DateTimeOriginal
    assert year == "2023"


def test_find_year_in_exif_data_no_year():
    file_with_exif = Path("./disk/1979/Zomaar wat/7hl_startnummer.jpg")
    year = find_year_in_exif(file_with_exif)
    # exif data contains no DateTimeOriginal
    assert not year


def test_find_year_in_exif_no_data():
    file_with_exif = Path("./disk/2023 Hondjes/Puppies.jpg")
    year = find_year_in_exif(file_with_exif)
    # no exif data in file
    assert not year
