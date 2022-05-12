# Adrián DCG 
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles


from libqtile.config import Screen
from libqtile import bar
#  from libqtile.log_utils import logger
from .widgets import primary_widgets
#  import subprocess

screens = [
    Screen(
        top=bar.Bar(
                primary_widgets,
                24,
                opacity=0.9,
                margin=[3,10,0,10],
                border_width=0,
                background='#FF000000'
        ),
            #status_bar(primary_widgets),
            #wallpaper='~/Pictures/Wallpapers/StarWars/765705.jpg',
            #wallpaper_mode="stretch",
            )
        ]

# Multimonitor support
#  xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"
#
#  command = subprocess.run(
#      xrandr,
#      shell=True,
#      stdout=subprocess.PIPE,
#      stderr=subprocess.PIPE,
#  )
#
#  if command.returncode != 0:
#      error = command.stderr.decode("UTF-8")
#      logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
#      connected_monitors = 1
#  else:
#      connected_monitors = int(command.stdout.decode("UTF-8"))
#
#if connected_monitors > 1:
#    for _ in range(1, connected_monitors):
#        screens.append(Screen(top=status_bar(secondary_widgets)))
