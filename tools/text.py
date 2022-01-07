# -*- coding: utf-8 -*-
import random

from .colors import BLINK, BOLD, FG, RESET_ALL, REVERSE

colors_list = [
    FG.orange,
    FG.blue,
    FG.purple,
    FG.cyan,
    FG.yellow,
    FG.pink,
    FG.lightblue,
    FG.lightcyan,
]
colors = random.choice(colors_list)
replace = REVERSE + colors
banner = (
    BLINK
    + f"""{colors}
 ____  ____   _    __  __ __     _____ _____ ____  _____  __
/ ___||  _ \ / \  |  \/  |\ \   / /_ _|_   _|  _ \|_ _\ \/ /
\___ \| |_) / _ \ | |\/| | \ \ / / | |  | | | |_) || | \  / 
 ___) |  __/ ___ \| |  | |  \ V /  | |  | | |  _ < | | /  \ 
|____/|_| /_/   \_\_|  |_|___\_/  |___| |_| |_| \_\___/_/\_\
                                         |_____|                             

{RESET_ALL}"""
)

cursor = BOLD + f"{colors}hack >> "
