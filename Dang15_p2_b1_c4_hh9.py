import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

def bt_Dang15_p2_b1_c4_hh9(self):
    def deg_to_dm_str(deg_float):
        total_minutes = int(Decimal(str(deg_float * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        d = total_minutes // 60
        m = total_minutes % 60
        return '%d^{\\circ}%d\'' % (d, m)

    # Khai báo biến
    bo = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
    oh, mh, om = random.choice(bo)
    mn = 2 * mh
    cos_moh = Rational(oh, om)
    tan_omh = Rational(oh, mh)
    goc_moh_deg = math.degrees(math.acos(oh / om))
    goc_mon_str = deg_to_dm_str(2 * goc_moh_deg)

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (O) at (0,0);\n'
        '\\coordinate (M) at (1.5,2);\n'
        '\\coordinate (N) at (1.5,-2);\n'
        '\\coordinate (H) at (1.5,0);\n'
        '\\draw[line width=1pt] (O) circle (2.5);\n'
        '\\draw[line width=1pt] (O)--(M) (O)--(N) (M)--(N) (O)--(H);\n'
        '\\draw[line width=1pt] (1.5,0.25)--(1.75,0.25)--(1.75,0);\n'
        '\\fill (O) circle (1pt) node[left] {$O$};\n'
        '\\fill (M) circle (1pt) node[above right] {$M$};\n'
        '\\fill (N) circle (1pt) node[below right] {$N$};\n'
        '\\fill (H) circle (1pt) node[below right] {$H$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
    )

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho đường tròn $(O; %d\\text{ cm})$ và dây cung $MN$ có khoảng cách từ tâm $O$ đến dây $MN$ là $OH = %d\\text{ cm}$ ($H \\in MN$) như hình vẽ. %s''' % (om, oh, hinh_ve))

    nb_da_1_d = '\\True Độ dài dây cung $MN$ bằng $%d\\text{ cm}$' % mn
    nb_da_1_s = 'Độ dài dây cung $MN$ bằng $%d\\text{ cm}$' % mh
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Xét $\\triangle OMH$ vuông tại $H$, $MH = \\sqrt{OM^2 - OH^2} = \\sqrt{%d^2 - %d^2} = %d\\text{ cm}$. Vì $\\triangle OMN$ cân tại $O$ nên $H$ là trung điểm $MN$, do đó $MN = 2MH = %d\\text{ cm}$.''' % (om, oh, mh, mn))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True $\\cos \\widehat{MOH} = %s$' % latex(cos_moh)
    th_da_1_s = '$\\cos \\widehat{MOH} = %s$' % latex(Rational(mh, om))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $\\cos \\widehat{MOH} = \\dfrac{OH}{OM} = \\dfrac{%d}{%d} = %s$.''' % (oh, om, latex(cos_moh)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True $\\tan \\widehat{OMH} = %s$' % latex(tan_omh)
    vd_da_1_s = '$\\tan \\widehat{OMH} = %s$' % latex(Rational(mh, oh))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $\\tan \\widehat{OMH} = \\dfrac{OH}{MH} = \\dfrac{%d}{%d} = %s$.''' % (oh, mh, latex(tan_omh)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Số đo góc ở tâm $\\widehat{MON}$ làm tròn đến phút bằng $%s$' % goc_mon_str
    vdc_da_1_s = 'Số đo góc ở tâm $\\widehat{MON}$ làm tròn đến phút bằng $%s$' % deg_to_dm_str(goc_moh_deg)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Từ $\\cos \\widehat{MOH} = \\dfrac{%d}{%d}$, bấm máy tính được $\\widehat{MOH} \\approx %s$. Suy ra $\\widehat{MON} = 2\\widehat{MOH} \\approx %s$.''' % (oh, om, deg_to_dm_str(goc_moh_deg), goc_mon_str))
    list_vdc_2 = [loigiai_vdc_1]
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n'
    )
    return content
