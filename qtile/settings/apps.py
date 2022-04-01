from libqtile.command import lazy

PLAY_SOUND_CMD = 'paplay'
PLAY_SOUND_PATH = '/usr/share/sounds/freedesktop/stereo/'
PLAY_SOUND_DEFAULT = 'window-attention.oga'

# --------- My default apps ---------
my_apps = {
    "apps_menu": {
        "type": "single",
        "cmd": "rofi -show drun"
    },
    "terminal": {
        "type": "single",
        "cmd": "kitty",
    },
    "browser": {
        "type": "single",
        "cmd": "google-chrome-stable"
    },
    "ide": {
        "type": "single",
        "cmd": "code"
    },
    "music_player": {
        "type": "terminal",
        "cmd": "ncspot"
    },
    "file_manager": {
        "type": "terminal",
        "cmd": "ranger"
    },
    "volume": {
        "type": "terminal",
        "cmd": "ncpamixer"
    },
    "whatsapp": {
        "type": "webapp",
        "cmd": "https://web.whatsapp.com"
    },
    "screenshot": {
        "type": "single",
        "cmd": "scrot -e 'mv $f Pictures/Screenshots/'"
    },
    "screenshot_select": {
        "type": "single",
        "cmd": "scrot -s -e 'mv $f Pictures/Screenshots/'"
    },
    "system_info": {
        "type": "single",
        "cmd": "neofetch"
    },
    "resources_monitor": {
        "type": "single",
        "cmd": "btop"
    }
}

def launch(appName):
    app = my_apps[appName]

    if app["type"] == "terminal":
        cmd = '{} -e {}'.format(my_apps["terminal"]["cmd"], app["cmd"])
    elif app["type"] == "webapp":
        cmd = 'qutebrowser -C .config/qutebrowser/webapp_config.py {}'.format(app["cmd"])
    else:
        cmd = app["cmd"]

    if "sound" in app:
        if app["sound"] == 'default':
            cmd = '{} {}{} && {} &'.format(PLAY_SOUND_CMD, PLAY_SOUND_PATH, PLAY_SOUND_DEFAULT, cmd)
    return lazy.spawn(cmd)

def get_launch_apps():
    apps_launchers = {}
    for k in my_apps.keys():
        apps_launchers[k] = launch(k)
    return apps_launchers

if __name__ == 'settings.apps':
    launchApp = get_launch_apps()
