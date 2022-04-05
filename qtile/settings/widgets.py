from libqtile.command import lazy
from libqtile import widget
from .theme import colors
from .ncspot import ncspot_cmds
from .apps import launchApp
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(foreground=colors['text'], background=colors['dark']):
    return {
        'foreground': foreground,
        'background': background
    }

def icon(foreground=colors['text'], background=colors['dark'], fontsize=14, text="?",padding=3, fmt='{}'):
    return widget.TextBox(
        **base(foreground, background),
        fontsize=fontsize,
        text=text,
        padding=padding,
        fmt=fmt
    )


def powerline(foreground=colors['text'], background=colors['dark'], tp="split", padding=0, size=22):
    types = {
                "split": {"icon":"", "font": "MesloLGS NF"},
                "start": {"icon":"", "font": 'JetBrainsMono Nerd Font'},
                "end": {"icon":"", "font": 'JetBrainsMono Nerd Font'},
            }
    return widget.TextBox(
        **base(foreground, background),
        text=types[tp]["icon"], 
        fontsize=size,
        padding=padding,
        font=types[tp]["font"],
        margin=3
    )

def get_widgets_colors(widgets_len, colors_list, startColor='', endColor=''):
    colors_len = len(colors_list)
    widgets_colors = []

    for i in range(0, widgets_len):
        color_actual = colors_list[i % colors_len]
        color_before = colors_list[(i - 1) % colors_len] if i > 0 else color_actual
        widgets_colors.append([color_before, color_actual])

    if startColor != '':
       widgets_colors[0][0] = startColor
       widgets_colors.insert(0, [startColor, startColor])
       widgets_colors.pop(len(widgets_colors)-1)

    if endColor != '':
        widgets_colors[len(widgets_colors)-1][1] = endColor
    
    return widgets_colors

def fullbar(widgets, colors_list, startColor="", endColor=""):
    widgets_len = len(widgets)
    widgets_colors = get_widgets_colors(widgets_len, colors_list, startColor=startColor, endColor=endColor)
    full_bar =  []

    for i, w in enumerate(widgets):
        [cb, ca] = widgets_colors[i]
        full_bar.append(powerline(background=None,foreground=ca, tp='start'))
        for sw in w:
            if 'icon' in sw:
                full_bar.append(icon(**sw['icon'], background=ca))
            full_bar.append(sw['widget'](**sw['params'], background=ca))
        full_bar.append(powerline(background=None,foreground=ca, tp='end'))
        if i < widgets_len-1:
            full_bar.append(widget.Sep(background="#FF000000", foreground="#FF000000",linewidth=6))
    return full_bar

def action_icon(icon=' ? ', foreground=colors['text'], callbacks={}, fontsize=14, padding=9):
    return {
        'widget': widget.TextBox,
        'params': {
            'text': icon,
            'foreground': foreground,
            'mouse_callbacks': callbacks,
            'padding': padding,
            'fontsize': fontsize,
            'markup': True
        }
    }

def parseAppName(name):
    apps_to_rename = {
        'Google Chrome': '  ',
        'NVIM': '  ',
        'ncspot': '  ',
        'Personalizar apariencia y comportamiento': '  ',
        'WhatsApp': '  '  
    }
    name = name.split("-")[-1].strip()
    if name in apps_to_rename:
        name = apps_to_rename[name]

    return name 

primary_widgets = fullbar(
    [
        [
            action_icon(
            icon="<span weight='bold'>ADR </span>",# ADR
            foreground=colors['dark'],
            callbacks={
                'Button1': launchApp["apps_menu"],
                'Button3': launchApp["system_info"]
            }
        ),
        {
            'widget': widget.GroupBox,
            'params': {
                'foreground': colors['dark'],
                'active': colors['dark'],
                'inactive': colors['white'],
                'highlight_method': 'line',
                'highlight_color': colors['color1'],
                #  'block_highlight_text_color': colors['color2'],
                #  'urgent_alert_method': 'border',
                #  'urgent_border': colors['urgent'],
                #  'this_current_screen_border': colors['focus'],
                'fontsize': 14,
                #  'this_screen_border':colors['dark'],
                'markup': True,
                'fmt': '<span weight="heavy">{}</span>',
#                  'other_current_screen_border':colors['dark'],
                #  'other_screen_border':colors['dark'],
                'margin': 3,
            }
        }
        ],
        [{
            'widget': widget.TaskList,
            'params': {
                'foreground': colors['text'],
                'icon_size': 0,
                'fontsize': 16,
                'highlight_method': 'block',
                'margin': 0,
                'border': colors['dark'],
                'padding_y': 2,
                'markup_focused': "<span color='"+colors['active']+"' weight='heavy'>{}</span>",
                'markup_normal': "<span weight='bold'>{}</span>",
                'markup_minimized': "<span color='"+colors['inactive']+"' weight='bold' style='italic'>{}</span>",
                'urgent_alert_method': 'text',
                'txt_minimized': ' ',
                'parse_text': parseAppName
            }
        }],
        [
            action_icon(icon='玲',callbacks={'Button1': ncspot_cmds['Previous']}),
            action_icon(icon='', foreground=colors['green'],callbacks={'Button1': ncspot_cmds['PlayPause']}),
            {
                'widget': widget.Mpris2,
                'params': {
                    'display_metadata': ['xesam:title', 'xesam:artist'],
                    'name': 'ncspot',
                    'objname': 'org.mpris.MediaPlayer2.ncspot',
                    'max_chars': 30,
                    'padding':3,
                    'scroll_chars': None,
                    'scroll_wait_intervals': 30,
                    'stop_pause_text': '  ',
                    'mouse_callbacks': { 'Button1': ncspot_cmds['PlayPause'] }
                }
            },
            action_icon(icon=' 怜',callbacks={'Button1': ncspot_cmds['Next']}),
        ],
        [
            {
                'widget': widget.PulseVolume,
                'params': {
                    'volume_down_command':"pactl set-sink-volume @DEFAULT_SINK@ -5%",
                    'volume_up_command':"pactl set-sink-volume @DEFAULT_SINK@ +5%",
                    'foreground': colors['color2'],
                    'fmt': '  {}'
                }
            },
            {
                'widget': widget.CPU,
                'params': {
                    'format': '  {load_percent}%',
                    'foreground': colors['color3']
                }
            },
            {
                'widget': widget.Memory,
                'params': {
                    'format': '  {MemPercent}% ',
                    'foreground': colors['color4']
                }
            },
            {
                'widget': widget.Wallpaper,
                'params': {
                    'foreground': colors['text'] ,
                    'directory':'~/Pictures/Wallpapers/',
                    'label':' ',
                }
            },
            {'widget': widget.CurrentLayoutIcon, 'params': { 'scale': 0.60 }},
            {'widget': widget.Systray, 'params':{'icon_size': 12, 'padding': 6}},
            {'widget': widget.Clock,'params': { 'format':' %H:%M ' }},
            {
                'widget': widget.QuickExit,
                'params': {
                    'default_text':'  ',
                    'countdown_format':'{}',
                    'countdown_start':1,
                    'padding': 3,
                    'foreground':colors['color1']
                }
            },
        ],
    ],
    [colors['color1'], colors['dark'], colors['dark'], colors['dark']],
)

widget_defaults = {
    'font': 'JetBrainsMono Nerd Font',
    'fontsize': 14,
    'padding': 3,
}
extension_defaults = widget_defaults.copy()
