#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import piexif
import os


class MinoltaDataMemoryCardToEXIF(object):
    """ Simple script to add  ImageDescription EXIF tag to images, based on data store in csv file."""
    def __init__(self):
        self.files = os.listdir()
        self.tag_files()

    def tag_files(self):
        for file in self.files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                print(file)
                exif_dict = piexif.load(file)
                exif_dict['0th'][piexif.ImageIFD.ImageDescription] = self.get_image_description(file)
                print(self.get_image_description(file))
                # exif_bytes = piexif.dump(exif_dict)
                # piexif.insert(exif_bytes, file)

    def get_image_description(self, file):
        return "{}\n{}\n{}\n{}\n{}".format(
            self.get_camera(),
            self.get_lens(file),
            self.get_exposure_data(file),
            self.get_film(),
            self.get_recipe()
        )

    def get_camera(self):
        camera = "Minolta Dynax 7xi"
        return camera

    def get_lens(self, file):
        lens = "AF ZOOM 35-105mm f3.5-4.5 (22)"
        return lens

    def get_exposure_data(self, file):
        exposure_data = "Minolta Data Card (1/180s, f22, 0.0, 35mm)"
        return exposure_data

    def get_film(self):
        film = "AgfaPhoto APX 400 @ 1600"
        return film

    def get_recipe(self):
        recipe = "Foma Fomadon Excel stock for 13min. (20C)"
        return recipe

if __name__ == "__main__":
    MinoltaDataMemoryCardToEXIF()
