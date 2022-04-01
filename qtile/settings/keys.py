# Gabriel Guerra (Thank you Antonio Sarosi)
# -- Gabriel Guerra links --
# http://github.com/AlphaTechnolog/
# http://github.com/AlphaTechnolog/dotfiles
# -- Antonio Sarosi links --
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy
from util import local_bin
from datetime import datetime
from .apps import launchApp # Go to define defaul apps
from .ncspot import ncspot_cmds

mod = "mod4"
keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------
    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    # Change window position (Columns)
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    ([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    # Grow window
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),
    ([mod, "control"], "n", lazy.layout.normalize()),
    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),
    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),
    # Kill window
    ([mod], "w", lazy.window.kill()),
    # Switch focus of monitors
    #([mod], "period", lazy.next_screen()),
    #([mod], "comma", lazy.prev_screen()),
    # Qtile management
    ([mod, "shift"], "r", lazy.restart()),
    ([mod, "shift"], "q", lazy.shutdown()),

    # ------------ Quick actions ------------
    # Screenshot
    ([], "Print", launchApp["screenshot"]), # Take full screenshot
    ([mod], "Print", launchApp["screenshot_select"]), # Take screenshot from selected area

    # ------------ App Configs ------------
    # Menu
    ([mod], "r", launchApp["apps_menu"]),#launch("apps_menu")),
    # Browser
    ([mod], "b", launchApp["browser"]),
    # Terminal
    ([mod], "t", launchApp["terminal"]),
    # Spotify client
    ([mod], "s", launchApp["music_player"]),
    # Whatsapp webapp
    ([mod], "m", launchApp["whatsapp"]),
    # File Manager
    ([mod], "f", launchApp["file_manager"]),
    # Audio manager
    ([mod], "v", launchApp["volume"]),

    # ------------ Hardware Configs ------------
    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    ([], "XF86AudioNext", ncspot_cmds["Next"]),
    ([], "XF86AudioPrev", ncspot_cmds["Previous"]),
    ([], "XF86AudioPlay", ncspot_cmds["PlayPause"]),
]]
