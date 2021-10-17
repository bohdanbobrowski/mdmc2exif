#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import piexif
import csv
import os
import sys


class MinoltaDataMemoryCardToEXIF(object):
    """ Simple script to add  ImageDescription EXIF tag to images, based on data store in csv file."""

    def __init__(self):
        if "--safe-mode" in sys.argv:
            self.safe_mode = True
        else:
            self.safe_mode = False
        self.files = os.listdir()
        self.csv_data = self._read_csv()
        self.tag_files()

    def _read_csv(self):
        csv_data = {}
        with open('data.csv', newline='') as csvfile:
            csv_data_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_data_reader:
                csv_data[row[0].lower()] = row[1:]
        return csv_data

    def tag_files(self):
        for file in self.files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                exif_dict = piexif.load(file)
                exif_dict['0th'][piexif.ImageIFD.ImageDescription] = self.get_image_description(file)
                print("\033[1m" + file + "\033[0m")
                print(self.get_image_description(file))
                if not self.safe_mode:
                    exif_bytes = piexif.dump(exif_dict)
                    # piexif.insert(exif_bytes, file)

    def get_image_description(self, file):
        return "{}{}{}{}{}".format(
            self.get_camera(),
            self.get_lens(file),
            self.get_exposure_data(file),
            self.get_film(),
            self.get_recipe()
        )

    def get_camera(self):
        camera = self.csv_data.get("camera", "")
        if camera and camera[0]:
            camera = "{}\n".format(camera[0])
        return camera

    def get_lens(self, file):
        lens = self.csv_data.get("lens", "")
        if lens and lens[0]:
            lens = "{}\n".format(lens[0])
        return lens

    def get_exposure_data(self, file):
        exposure_data = self.csv_data.get(file, "")
        if exposure_data and len(exposure_data) >= 4:
            exposure_data = "Minolta Data Card (1/{}s, f{}, {}, {}mm)\n".format(
                exposure_data[0],
                exposure_data[1],
                exposure_data[2],
                exposure_data[3]
            )
        return exposure_data

    def get_film(self):
        film = self.csv_data.get("film", "")
        if film and film[0]:
            film = "{}\n".format(film[0])
        return film

    def get_recipe(self):
        recipe = self.csv_data.get("recipe", "")
        if recipe and recipe[0]:
            recipe = "{}\n".format(recipe[0])
        return recipe


def main():
    MinoltaDataMemoryCardToEXIF()


if __name__ == "__main__":
    main()
