#!/usr/bin/env python

import time
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw
from ST7789 import ST7789
import sys

SPI_SPEED_MHZ = 80

image_file = sys.argv[1]

image = Image.open(image_file)
draw = ImageDraw.Draw(image)


st7789 = ST7789(
    height=240,
    rotation=90,  # Needed to display the right way up on Pirate Audio
    port=0,       # SPI port
    cs=1,         # SPI port Chip-select channel
    dc=9,         # BCM pin used for data/command
    backlight=13,
    spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000,
    offset_left=0,
    offset_top=0
)

WIDTH = st7789.width
HEIGHT = st7789.height

image = image.resize((WIDTH, HEIGHT))
st7789.display(image)
