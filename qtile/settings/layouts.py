# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from libqtile.config import Match
from .theme import colors, theme

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['active'],
    'border_normal': colors['dark'],
    'border_width': 3,
    'margin': 6,
    'border_on_single': False,
    'margin_on_single': 0,
    'wrap_focus_columns': True
}

layouts = [
    layout.Columns(num_columns=4, **layout_conf),
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.Floating(**layout_conf)
    #layout.MonadWide(**layout_conf),
    #layout.Bsp(**layout_conf),
    #layout.Matrix(columns=2, **layout_conf),
    #layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors['focus'],
    border_width=0,
)
