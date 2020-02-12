import os
import json
from time import strftime

a = {}
a["宽度"] = 800
a["高度"] = 600
a["最低透明度"] = 0.6
a["渐变"] = True
a["源语言"] = "en"
a["目标语言"] = "zh-CN"


def doc_create():
    path_dirs = os.listdir()
    if 'vBook.md' not in path_dirs:
        with open('vBook.md', 'a+', encoding='utf-8') as f:
            f.write(' Vacb | 释义 |Time\n')
            f.write(' :-:|:-:|:-:\n')
    if 'history.md' not in path_dirs:
        with open('history.md', 'a+', encoding='utf-8') as f:
            pass
    if 'gtl_config.json' not in path_dirs:
        b = json.dumps(a, indent=8, ensure_ascii=False)
        with open('gtl_config.json', 'w', encoding='utf-8')as f:
            f.write(b)


def write_doc(im, translation):
    translation = translation[4:]
    if len(translation) >= 2:
        if len(im) <= 20:
            with open('vBook.md', 'a+', encoding='utf-8') as f:
                # <font Size=5 face="Arial Rounded MT" color=green>section</font>|<font Size=5 face="华文行楷" color=black>不分</font>|<font Size=4 face="Arial Rounded MT" color=gray>2019/11/10</font>
                f.write(
                    '<font Size=5 face="Arial Rounded MT" color=green>' + im.lower() + '</font>|<font Size=5 face="华文行楷" color=black>' + translation + '</font>|<font Size=4 face="Arial Rounded MT" color=gray>' + strftime(
                        '%Y/%m/%d') + '</font>\n')
            with open('vBook.txt', 'a+', ) as f:
                f.write('[' + strftime('%Y-%m-%d') + ']    ' + im.lower() + ':   ' + translation + '\n')
        with open('history.md', 'a+', encoding='utf-8') as f:
            f.write(
                '<div style="text-align:justify;word-break:break-all;"><font face="华文隶书" Size=5 color=green>&ensp;&ensp;&ensp;&ensp;' + im + '</font></div>\n\n')
            f.write(
                '<div style="text-align:justify;word-break:break-all;"><font Size=5 face="华文行楷" color=black>&ensp;&ensp;&ensp;&ensp;' + translation + '</font></div>\n\n')
            f.write('<div align=right><font Size=4 face="Arial Rounded MT" color=gray>' + strftime(
                '%Y/%m/%d %H:%M') + '</font></div>\n\n')

def load_config():
    with open('gtl_config.json', encoding='utf-8')as f:
        cc = f.read()
    dd = json.loads(cc)
    return dd
