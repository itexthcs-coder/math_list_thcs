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


def bt_dang2_p2_b1_c3_ds9(self):
    # Khai báo biến
    a_num = random.choice([12.4, 14.8, 17.2, 18.5, 21.3, 23.6])
    tu = random.choice([11, 13, 15, 17, 19])
    mau = random.choice([6, 7, 8, 9])
    while math.gcd(tu, mau) != 1:
        mau = random.choice([6, 7, 8, 9])

    val_a = math.sqrt(a_num)
    val_b = math.sqrt(tu / mau)
    tron_a = round(val_a, 2)
    tron_b = round(val_b, 2)
    tron_m = round(val_a - val_b, 2)

    str_a = str(a_num).replace('.', ',')
    str_tron_a = f"{tron_a:.2f}".replace('.', ',')
    str_tron_a_sai = f"{round(tron_a + 0.02, 2):.2f}".replace('.', ',')
    str_tron_b = f"{tron_b:.2f}".replace('.', ',')
    str_tron_b_sai = f"{round(tron_b + 0.01, 2):.2f}".replace('.', ',')
    str_tron_m = f"{tron_m:.2f}".replace('.', ',')
    str_tron_m_sai = f"{round(tron_m - 0.02, 2):.2f}".replace('.', ',')

    # Nội dung câu hỏi
    noidungcauhoi = (f'''Cho biểu thức $M = \\sqrt{{{str_a}}} - \\sqrt{{\\dfrac{{{tu}}}{{{mau}}}}}$. Sử dụng máy tính cầm tay để tính toán và xét tính đúng, sai của các khẳng định sau:''')

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = f'\\True Giá trị của $\\sqrt{{{str_a}}}$ làm tròn đến chữ số thập phân thứ hai là ${str_tron_a}$.'
    nb_da_1_s = f'Giá trị của $\\sqrt{{{str_a}}}$ làm tròn đến chữ số thập phân thứ hai là ${str_tron_a_sai}$.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1_d = f'Bấm máy tính cầm tay ta được $\\sqrt{{{str_a}}} \\approx {val_a:.5f}\\dots$, làm tròn đến chữ số thập phân thứ hai là ${str_tron_a}$.'
    loigiai_nb_1_s = f'Sai. Bấm máy tính cầm tay ta được $\\sqrt{{{str_a}}} \\approx {val_a:.5f}\\dots$, làm tròn đến chữ số thập phân thứ hai phải là ${str_tron_a}$.'

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = f'\\True Giá trị của $\\sqrt{{\\dfrac{{{tu}}}{{{mau}}}}}$ làm tròn đến chữ số thập phân thứ hai là ${str_tron_b}$.'
    th_da_1_s = f'Giá trị của $\\sqrt{{\\dfrac{{{tu}}}{{{mau}}}}}$ làm tròn đến chữ số thập phân thứ hai là ${str_tron_b_sai}$.'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1_d = f'Bấm máy tính cầm tay ta được $\\sqrt{{\\dfrac{{{tu}}}{{{mau}}}}} \\approx {val_b:.5f}\\dots$, làm tròn đến chữ số thập phân thứ hai là ${str_tron_b}$.'
    loigiai_th_1_s = f'Sai. Bấm máy tính cầm tay ta được $\\sqrt{{\\dfrac{{{tu}}}{{{mau}}}}} \\approx {val_b:.5f}\\dots$, làm tròn đến chữ số thập phân thứ hai phải là ${str_tron_b}$.'

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = f'\\True Số ${str_a}$ có hai căn bậc hai gần đúng (làm tròn đến hàng phần trăm) là ${str_tron_a}$ và $-{str_tron_a}$.'
    vd_da_1_s = f'Số ${str_a}$ chỉ có một căn bậc hai gần đúng là ${str_tron_a}$.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1_d = f'Vì ${str_a} > 0$ nên số ${str_a}$ có hai căn bậc hai đối nhau là $\\sqrt{{{str_a}}} \\approx {str_tron_a}$ và $-\\sqrt{{{str_a}}} \\approx -{str_tron_a}$.'
    loigiai_vd_1_s = f'Sai. Số dương ${str_a}$ có hai căn bậc hai đối nhau là ${str_tron_a}$ và $-{str_tron_a}$.'

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = f'\\True Giá trị của $M$ làm tròn đến hàng phần trăm bằng ${str_tron_m}$.'
    vdc_da_1_s = f'Giá trị của $M$ làm tròn đến hàng phần trăm bằng ${str_tron_m_sai}$.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1_d = f'Ta có $M = \\sqrt{{{str_a}}} - \\sqrt{{\\dfrac{{{tu}}}{{{mau}}}}} \\approx {val_a:.5f} - {val_b:.5f} = {val_a - val_b:.5f}\\dots$, làm tròn đến hàng phần trăm được ${str_tron_m}$.'
    loigiai_vdc_1_s = f'Sai. Tính trực tiếp trên máy tính cầm tay ta được $M \approx {val_a - val_b:.5f}\\dots \approx {str_tron_m}$.'

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

    loigiai_nb_1 = loigiai_nb_1_d if '\\True' in nb_da_1 else loigiai_nb_1_s
    loigiai_th_1 = loigiai_th_1_d if '\\True' in th_da_1 else loigiai_th_1_s
    loigiai_vd_1 = loigiai_vd_1_d if '\\True' in vd_da_1 else loigiai_vd_1_s
    loigiai_vdc_1 = loigiai_vdc_1_d if '\\True' in vdc_da_1 else loigiai_vdc_1_s

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')

    return content
