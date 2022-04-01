from libqtile.command import lazy

DBUS_MPRIS = 'MediaPlayer2'
DBUS_PLAYER = 'ncspot'
DBUS_MPRIS_DOTS = 'org.mpris.{}'.format(DBUS_MPRIS)
DBUS_MPRIS_SLASH = '/org/mpris/{}'.format(DBUS_MPRIS)
DBUS_CMD_BASE = 'dbus-send --session --type="method_call" --dest={dots}.{player} {slash} {dots}.Player'.format(
        dots= DBUS_MPRIS_DOTS,
        slash= DBUS_MPRIS_SLASH,
        player= DBUS_PLAYER
)
DBUS_METHOS = ['Forward','Next','OpenUri','Pause','Play','PlayPause','Previous','Rewind','Seek','SetPosition','Stop']

def get_cms():
    cmds = {}
    for method in DBUS_METHOS:
        cmds[method] = lazy.spawn('{}.{}'.format(DBUS_CMD_BASE, method))
    return cmds

if __name__ == 'settings.ncspot':
    ncspot_cmds = get_cms()
