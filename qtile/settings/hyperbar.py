from libqtile import widget
from .theme import colors

#==================================================
#                DEFAULTS
#==================================================
DEFAULT_BACKGROUND = colors['background'] or '#1E1E1E'
DEFAULT_FOREGROUND = colors['text'] or '#FFFFFF'
DEFAULT_ICON_FONT = 'JetBrainsMono Nerd Font'
DEFAULT_ICON_SIZE = 14
DEFAULT_TEXT = '?'
DEFAULT_ICON_PADDING=3
DEFAULT_SEPARATE_WIDGETS_GROUPS = True
DEFAULT_SEPARATE_WIDGETS = True
BAR_STYLES = {
    'round': {
        'start': [''],
        'end': [''],
        'divisor': ['', 'MesloLGS NF']
    },
    'simple': {
        'start': None,
        'end': None,
        'divisor': ['', 'MesloLGS NF']
    }
}

def icon(text=DEFAULT_TEXT, foreground=DEFAULT_FOREGROUND, background=DEFAULT_BACKGROUND, size=DEFAULT_ICON_SIZE, padding=DEFAULT_ICON_PADDING, font=DEFAULT_ICON_FONT):
    return widget.TextBox(
        foreground= foreground,
        background= background,
        fontsize=size,
        text=text,
        padding=padding
    )

def hyperbar(bar_background=DEFAULT_BACKGROUND, bar_foreground=DEFAULT_FOREGROUND, style="round", hasGroupsSeparator=True, widgets_groups):
    widgets_bar = []
    len_groups = len(widgets_groups)
    style = style if style in BAR_STYLES else 'round'

    for gi, group in enumerate(widgets_groups):
        group_background = group['background'] or bar_background
        group_foreground = group['foreground'] or bar_foreground
        group_style = group['style'] or style
        len_widgets = len(group['widgets'])

        for wi, w in enumerate(group['widgets']):
            widget_background = w['params']['background'] or group_background
            widget_foreground = w['params']['foreground'] or group_foreground

            if wi == 0:
                widgets_bar.append(icon(text=BAR_STYLES[group_style]['start'], background=None, foreground=widget_background))



## WIDGETS BAR STRUCTURE
#  {
    #  "background": "#FF000000",
    #  "foreground": "#FFFFFF",
    #  "style": "round",
    #  "hasSeparator": True,
    #  "bar": [
    #      {
    #          'background': "#000000",
    #          'foreground': '#FFFFFF',
    #          'style': 'round',
    #          'widgets': [
    #              {
    #                  'widget': 'action_icon',
    #                  'params': {
    #                      'icon': "<span weight='bold'>ADR </span>",
    #                      'foreground': '#FFFFFF',
    #                      'callbacks': {
    #                          'Button1': '',
    #                          'Button3': ''
    #                      }
    #                  }
    #              },
    #              {
    #                  'widget': widget.GroupBox,
    #                  'params': {
    #                      'foreground': colors['background'],
    #                      'active': colors['background'],
    #                      'inactive': colors['light'],
    #                      'highlight_method': 'line',
    #                      'highlight_color': colors['color1'],
    #                      'fontsize': 14,
    #                      'markup': True,
    #                      'fmt': '<span weight="heavy">{}</span>',
    #                      'margin': 3,
    #                  }
    #              }
    #          ]
    #      }
    #  ]
#  }
