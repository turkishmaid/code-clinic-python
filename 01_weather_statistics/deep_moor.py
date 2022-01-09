#!/usr/bin/env python
# coding: utf-8

"""
Explore different alternatives to load the data.
"""
# Created: 09.01.22

import json
from datetime import datetime
from pathlib import Path
import csv
from collections import namedtuple
from typing import Any


def data_files() -> list[Path]:
    data_path = Path("..") / "Exercise_Files" / "Ch01" / "resources"
    files = [data_path / f"Environmental_Data_Deep_Moor_{year}.txt" for year in range(2012, 2016)]
    for file in files:
        assert file.exists()
    return files


deep_moor_fields = ['date       time    ', 'Air_Temp', 'Barometric_Press', 'Dew_Point', 'Relative_Humidity', 'Wind_Dir', 'Wind_Gust', 'Wind_Speed']
DeepMoorRow = namedtuple("DeepMoorRow", ['DateTime', 'AirTemp', 'BarometricPress', 'DewPoint', 'RelativeHumidity', 'WindDir', 'WindGust', 'WindSpeed'])


def cook_datetime(s: str) -> datetime:
    s = s.replace("_", "-").replace(" ", "T") + ".000"
    return datetime.fromisoformat(s)


def cook_field(s: str, field: str) -> Any:
    if field == deep_moor_fields[0]:
        return cook_datetime(s)
    else:
        return float(s)

def read_data_stdlib():
    # https://docs.python.org/3.9/library/csv.html
    paths = data_files()
    with open(paths[0], newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(5000))
    data = []
    for path in paths:
        print(path)
        cnt = 0
        with open(path, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.DictReader(csvfile, dialect=dialect)
            cols_fit = False
            for line in reader:
                if not cols_fit:
                    assert reader.fieldnames == deep_moor_fields, str(Path)
                    cols_fit = True
                data.append(DeepMoorRow(*[cook_field(line[f], f) for f in deep_moor_fields]))
                cnt += 1
        print(f"   + {cnt} -> {len(data)}")
    return data


if __name__ == "__main__":
    data = read_data_stdlib()
    pass
