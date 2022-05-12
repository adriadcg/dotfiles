#!/bin/sh
# Window compozitor
picom &
# Welcome sound message
paplay ~/starting.ogg
# Disable DPMS and prevent screen from blancking
xset s off -dpms
# Open ncspot on kitty therminal
kitty -e ncspot &
blueman &
