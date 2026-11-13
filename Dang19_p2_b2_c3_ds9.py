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


def bt_Dang19_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = 4
        can_k = 2
        heso_C = 5
        x0 = randint(7, 14)
        S0 = k * (x0**2)
        dai_0 = k * x0

        noidungcauhoi = ('''Một mảnh đất hình chữ nhật có chiều dài gấp $%s$ lần chiều rộng. Gọi chiều rộng của mảnh đất là $x$ ($\text{m}$, $x > 0$) và diện tích của mảnh đất là $S$ ($\text{m}^2$). Xét tính đúng sai của các mệnh đề sau:'''
                         % (latex(k)))

        nb_da_1_d = '\\True Diện tích $S$ của mảnh đất tính theo $x$ là $S = %sx^2$ ($\text{m}^2$)' % (latex(k))
        nb_da_1_s = 'Diện tích $S$ của mảnh đất tính theo $x$ là $S = %sx$ ($\text{m}^2$)' % (latex(k))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Chiều dài của mảnh đất là $%sx$ ($\text{m}$). Diện tích mảnh đất là $S = x \cdot %sx = %sx^2$ ($\text{m}^2$).'''
                        % (latex(k), latex(k), latex(k)))

        th_da_1_d = '\\True Chiều rộng $x$ của mảnh đất được biểu diễn theo diện tích $S$ là $x = \dfrac{\sqrt{S}}{%s}$ ($\text{m}$)' % (latex(can_k))
        th_da_1_s = 'Chiều rộng $x$ của mảnh đất được biểu diễn theo diện tích $S$ là $x = \dfrac{\sqrt{S}}{%s}$ ($\text{m}$)' % (latex(k))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Từ $S = %sx^2 \Rightarrow x^2 = \dfrac{S}{%s}$. Vì $x > 0$ nên $x = \sqrt{\dfrac{S}{%s}} = \dfrac{\sqrt{S}}{\sqrt{%s}} = \dfrac{\sqrt{S}}{%s}$ ($\text{m}$).'''
                        % (latex(k), latex(k), latex(k), latex(k), latex(can_k)))

        vd_da_1_d = '\\True Chu vi của mảnh đất tính theo diện tích $S$ là $C = %s\sqrt{S}$ ($\text{m}$)' % (latex(heso_C))
        vd_da_1_s = 'Chu vi của mảnh đất tính theo diện tích $S$ là $C = %s\sqrt{S}$ ($\text{m}$)' % (latex(heso_C * 2))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Chu vi mảnh đất là $C = 2(x + %sx) = %sx = %s \cdot \dfrac{\sqrt{S}}{%s} = %s\sqrt{S}$ ($\text{m}$).'''
                        % (latex(k), latex(2 * (k + 1)), latex(2 * (k + 1)), latex(can_k), latex(heso_C)))

        vdc_da_1_d = '\\True Khi diện tích mảnh đất bằng $%s\text{ m}^2$, chiều dài của mảnh đất là $%s\text{ m}$' % (latex(S0), latex(dai_0))
        vdc_da_1_s = 'Khi diện tích mảnh đất bằng $%s\text{ m}^2$, chiều dài của mảnh đất là $%s\text{ m}$' % (latex(S0), latex(x0))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Khi $S = %s\text{ m}^2$, chiều rộng là $x = \dfrac{\sqrt{%s}}{%s} = \dfrac{%s}{%s} = %s\text{ (m)}$. Chiều dài mảnh đất là $%s \cdot %s = %s\text{ (m)}$.'''
                         % (latex(S0), latex(S0), latex(can_k), latex(can_k * x0), latex(can_k), latex(x0), latex(k), latex(x0), latex(dai_0)))

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
