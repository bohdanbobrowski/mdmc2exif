#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import piexif
import csv
import os
import sys

VERSION = "1.2.4"

class MinoltaDataMemoryCardToEXIF(object):
    """Simple script to add  ImageDescription EXIF tag to images, based on data store in csv file."""

    def __init__(self):
        self._print_version()
        if "--version" in sys.argv:
            pass
        elif "--dry-run" in sys.argv:
            self.safe_mode = True
            self.files = os.listdir()
            self.csv_data = self._read_csv()
            self.tag_files()
        elif "--save" in sys.argv:
            self.safe_mode = False
            self.files = os.listdir()
            self.csv_data = self._read_csv()
            self.tag_files()
        else:
            print("--help")
            print("--version")
            print("--dry-run")
            print("--save")

    def _print_version(self):
        print(f"Minolta Data Memory Card To EXIF v.{VERSION}")

    def _read_csv(self):
        csv_data = {}
        with open("data.csv", newline="") as csvfile:
            csv_data_reader = csv.reader(csvfile, delimiter=",")
            for row in csv_data_reader:
                try:
                    csv_data[row[0].lower()] = row[1:]
                except IndexError:
                    pass
        return csv_data

    def tag_files(self):
        for file in self.files:
            if file.lower().endswith((".jpg", ".jpeg")):
                exif_dict = piexif.load(file)
                exif_dict["0th"][
                    piexif.ImageIFD.ImageDescription
                ] = self.get_image_description(file)
                print("\033[1m[" + file + "]\033[0m")
                print(self.get_image_description(file))
                if not self.safe_mode:
                    exif_bytes = piexif.dump(exif_dict)
                    piexif.insert(exif_bytes, file)
                else:
                    print("(safe mode)")

    def get_image_description(self, file):
        return (
            self.get_csv_value("camera")
            + self.get_lens(file.lower())
            + self.get_exposure_data(file.lower())
            + self.get_csv_value("film")
            + self.get_csv_value("recipe").strip()
        )

    def get_csv_value(self, label):
        val = self.csv_data.get(label, "")
        if val and len(val) > 0 and val[0]:
            val = "{}\n".format(val[0])
        return val

    def get_lens(self, file):
        exposure_data = self.csv_data.get(file, "")
        if exposure_data and len(exposure_data) >= 5 and exposure_data[5]:
            return "{}\n".format(exposure_data[5])
        return ""

    def get_exposure_data(self, file):
        data = self.csv_data.get(file, "")
        exposure_data = []
        if data:
            if len(data) > 0 and data[0]:
                exposure_data.append("1/{}s".format(data[0]))
            if len(data) > 1 and data[1]:
                exposure_data.append("f{}".format(data[1]))
            if len(data) > 2 and data[2]:
                exposure_data.append("{}".format(data[2]))
            if len(data) > 3 and data[3]:
                exposure_data.append("{}mm".format(data[3]))
            if len(data) > 6 and data[6]:
                exposure_data.append("program '{}'".format(data[6].upper()))
        if exposure_data:
            return "Minolta Data Card ({})\n".format(", ".join(exposure_data))
        else:
            return ""


def main():
    MinoltaDataMemoryCardToEXIF()


if __name__ == "__main__":
    main()
