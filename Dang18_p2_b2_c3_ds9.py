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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_Dang18_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v0 = random.choice([12, 15, 16, 18, 20])
        m0 = random.choice([1.6, 2.5, 3.2, 4.0])
        E0 = (m0 * (v0**2)) / 2
        str_m0 = str(m0).replace('.', ',')
        str_E0 = str(round(E0, 2)).rstrip('0').rstrip(',').replace('.', ',')

        k_v = random.choice([2, 3, 4])
        k_E = k_v**2

        noidungcauhoi = ('''Vận tốc $v$ ($\text{m/s}$) của một vật đang bay được cho bởi công thức $v = \sqrt{\dfrac{2E}{m}}$, trong đó $E$ là động năng của vật (tính bằng Joule, kí hiệu là $\text{J}$) và $m$ ($\text{kg}$) là khối lượng của vật. Xét tính đúng sai của các mệnh đề sau:''')

        nb_da_1_d = '\\True Với $E \ge 0$ và $m > 0$, công thức vận tốc có thể viết thành $v = \dfrac{\sqrt{2E}}{\sqrt{m}}$'
        nb_da_1_s = 'Với $E \ge 0$ và $m > 0$, công thức vận tốc có thể viết thành $v = \dfrac{2\sqrt{E}}{m}$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Áp dụng quy tắc khai căn bậc hai của một thương với $2E \ge 0$ và $m > 0$, ta có $v = \sqrt{\dfrac{2E}{m}} = \dfrac{\sqrt{2E}}{\sqrt{m}}$.''')

        th_da_1_d = '\\True Khi vật có khối lượng $%s\text{ kg}$ và động năng $%s\text{ J}$ thì tỉ số $\dfrac{2E}{m}$ bằng $%s$' % (str_m0, str_E0, latex(v0**2))
        th_da_1_s = 'Khi vật có khối lượng $%s\text{ kg}$ và động năng $%s\text{ J}$ thì tỉ số $\dfrac{2E}{m}$ bằng $%s$' % (str_m0, str_E0, latex((v0**2) // 2))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thay $m = %s$ và $E = %s$, ta tính được $\dfrac{2E}{m} = \dfrac{2 \cdot %s}{%s} = %s$.'''
                        % (str_m0, str_E0, str_E0, str_m0, latex(v0**2)))

        vd_da_1_d = '\\True Vận tốc bay của vật có khối lượng $%s\text{ kg}$ và động năng $%s\text{ J}$ là $%s\text{ m/s}$' % (str_m0, str_E0, latex(v0))
        vd_da_1_s = 'Vận tốc bay của vật có khối lượng $%s\text{ kg}$ và động năng $%s\text{ J}$ là $%s\text{ m/s}$' % (str_m0, str_E0, latex(v0 + 5))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Vận tốc của vật là $v = \sqrt{%s} = %s\text{ (m/s)}$.'''
                        % (latex(v0**2), latex(v0)))

        vdc_da_1_d = '\\True Nếu giữ nguyên khối lượng $m$ và muốn vận tốc tăng gấp $%s$ lần thì động năng $E$ cần tăng gấp $%s$ lần' % (latex(k_v), latex(k_E))
        vdc_da_1_s = 'Nếu giữ nguyên khối lượng $m$ và muốn vận tốc tăng gấp $%s$ lần thì động năng $E$ cần tăng gấp $%s$ lần' % (latex(k_v), latex(k_v * 2))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Khi $E' = %sE$ và $m' = m$, ta có $v' = \sqrt{\dfrac{2 \cdot %sE}{m}} = \sqrt{%s} \cdot \sqrt{\dfrac{2E}{m}} = %sv$. Vậy động năng cần tăng gấp $%s$ lần.'''
                         % (latex(k_E), latex(k_E), latex(k_E), latex(k_v), latex(k_E)))

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

        list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
        list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
        list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
        list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
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
               '\\end{ex}\n \\end{minipage}\n\n')

    return content
