# Minolta Data Memory Card to EXIF

Simple script to add specific ImageDescription EXIF tag to images, based on data stored in csv file.

It was made to speedup upload process to my <a href="https://flickr.com/photos/bodzio">flickr account</a>, and was inspired by Minolta Data Memory Card. 

## Installation

    pip install git+https://github.com/bohdanbobrowski/mdmc2exif

## Usage

Run command in directory where images and required **data.csv** file is stored:

    mdmc2exif

Or with optional parameter **--safe-mode**, which disables writing:

    mdmc2exif --safe-mode

## What the hell is Minolta Data Memory Card?

It is already quite obsolete accessory for the first Minolta Dynax cameras. These cameras allowed the use of cards extending their functions, and one of them was "Minolta Data Memory Card" - which allowed to record:
- shutter speed, 
- aperture value, 
- exposure compensation, 
- lens focal length (for zoom lenses - actual value), 
- maximum aperture value (at this focal length).

And it stored maximum those values for maximum 40 pictures (usually, one 35mm film casette can store 36 pictures). So total capacity of this card was around 1 Kilobyte.

The card itself looks like this:

<img src="minolta_data_memory_card.gif" />

## Documentation used

Based on: https://exiftool.org/TagNames/EXIF.html

## ImageDescription example:

    Minolta Dynax 7xi
    AF ZOOM 35-105mm f3.5-4.5 (22)
    Minolta Data Card (1/180s, f22, 0.0, 35mm)
    AgfaPhoto APX 400 @ 1600
    Foma Fomadon Excel stock for 13min. (20C)

## Required csv structure:

CSV can contain 4 types of data, and it's declared by first column value: 

1. "camera" - camera manufacturer, and model type
2. "film" - film manufacturer and type
3. "recipe" - recipe used to develop this film
4. pictures metadata:
    

    [file name], [shutter speed], [aperture value], [exposure compensation], [focal length], [maximum aperture], [lens manufacturer and model]


### Example:

    camera,Minolta Dynax 7xi
    film,AgfaPhoto APX 400 @ 1600
    recipe,Foma Fomadon Excel stock for 13min. (20C)
    36.jpg,1500,4,0.0,210,4,Minolta AF ZOOM 70-210mm f4 (32)
