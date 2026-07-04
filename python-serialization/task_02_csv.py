#!/usr/bin/env python3
"""Module converts CSV Data to JSON Format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Function that converts a CSV file to JSON."""

    try:
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            with open("data.json", "w") as json_file:
                json.dump(list(reader), json_file)
            return True
    except Exception:
        return False
