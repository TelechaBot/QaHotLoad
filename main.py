# -*- coding: utf-8 -*-
# @Time    : 8/26/22 5:27 PM
# @FileName: main.py.py
# @Software: PyCharm
# @Github    ：sudoskys


import StarPuller

from StarPuller import Worker


# 这是定时热载的示例...

def run_timer():
    from StarPuller import Worker
    Worker().get_index()
    timer()


def timer():
    from threading import Timer
    t = Timer(100, run_timer, args=[])
    t.start()
