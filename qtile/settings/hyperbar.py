from libqtile import widget
from .theme import colors

#==================================================
#                DEFAULTS
#==================================================
DEFAULT_BACKGROUND = colors['dark'] || '#1E1E1E'
DEFAULT_FOREGROUND = colors['white'] || '#FFFFFF'


BAR_START_ICON = ''
BAR_END_ICON = ''
SECTION_SEPARATOR = ''


def base(foreground=colors['text'], background=colors['bg']):
    return {
        'foreground': foreground,
        'background': background
    }

def icon(text='?', foreground, background, fontsize=14, padding=3, font=''):
    return widget.TextBox(
        **base(foreground, background),
        fontsize=fontsize,
        text=text,
        padding=padding
    )

def hyperbar(style):

# Estilos de barras
# - triangle_left
# - triangle_right
# - round
styles = {
    'round': {
        'start_icon': '',
        'end_icon': ''
    }
}
hyperbar(
    style='round',

)
