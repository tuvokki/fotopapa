# Filesorter sorts files by year.

## Download this repo to $HOME/projects

unpack to `fotopapa-main` (doubleclick in Finder does this), open a terminal and:

cd `$HOME/projects/fotopapa-main`

### Create virtual environment

    uv sync

### run the script

    uv run main.py

### Output

    ---------------------------------------------------------------------------------
    Examining file: disk/1966Allemaal/article.jpg
    Found year in path: 1966
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/Puppies.jpg
    Found year in path: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/20230207_093811.jpg
    Found year in path: 2023
    Found year in exif: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/Foscam Dome-12212022-0743253908.jpg
    Found year in path: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/20230207_101958.jpg
    Found year in path: 2023
    Found year in exif: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/comelit cam-12212022-0727377907.jpg
    Found year in path: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/20230207_102000.jpg
    Found year in path: 2023
    Found year in exif: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/Foscam Dome-12212022-0739593865.jpg
    Found year in path: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/ONVIF-12212022-0738130071.jpg
    Found year in path: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/20230207_101956.jpg
    Found year in path: 2023
    Found year in exif: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/comelit cam-12212022-0727072672.jpg
    Found year in path: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/2023 Hondjes/comelit cam-12212022-0735595386.jpg
    Found year in path: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/1979/190585831_10225895654077084_2413713328661882472_n.jpg
    Found year in path: 1979
    ---------------------------------------------------------------------------------
    Examining file: disk/geenjaar/20230207_101958.jpg
    Found year in exif: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/geenjaar/20230207_102000.jpg
    Found year in exif: 2023
    ---------------------------------------------------------------------------------
    Examining file: disk/1979/Zomaar wat/7hl_startnummer.jpg
    Found year in path: 1979
    ---------------------------------------------------------------------------------
    Examining file: disk/1979/Zomaar wat/9w6d3irst6971.jpg
    Found year in path: 1979
    ---------------------------------------------------------------------------------
    Examining file: disk/1979/Zomaar wat/275737465_1043426989853865_2536383096811020178_n.jpg
    Found year in path: 1979
    ---------------------------------------------------------------------------------
    Examining file: disk/1979/Zomaar wat/5mt86xife1971.jpg
    Found year in path: 1979
    ---------------------------------------------------------------------------------
    Examining file: disk/1979/Zomaar wat/192389584_4101583403255449_2861368391498317598_n.jpg
    Found year in path: 1979

### Run tests

    uv run -m pytest

### Output
    
    ============================================================================================= test session starts =============================================================================================
    platform darwin -- Python 3.13.1, pytest-9.0.1, pluggy-1.6.0
    rootdir: /Users/tuvokki/projects/filesorter
    configfile: pyproject.toml
    collected 7 items                                                                                                                                                                                             
    
    test_main.py .......                                                                                                                                                                                    [100%]
    
    ============================================================================================== 7 passed in 0.06s ==============================================================================================
