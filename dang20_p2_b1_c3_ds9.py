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


def bt_dang20_p2_b1_c3_ds9(self):
    # Khai báo biến
    can_s = random.choice([4, 5, 6])
    s = can_s**2
    he_so = 15.6
    tich_duoi_can = round(he_so * s, 1)
    str_tich = str(tich_duoi_can).replace('.', ',')
    v_ms = math.sqrt(tich_duoi_can)
    v_ms_tron = round(v_ms, 2)
    str_v_ms = f"{v_ms_tron:.2f}".replace('.', ',')
    str_v_ms_sai = f"{round(v_ms_tron + 0.04, 2):.2f}".replace('.', ',')
    v_kmh = round(v_ms_tron * 3.6, 2)
    str_v_kmh = f"{v_kmh:.2f}".replace('.', ',')
    gioi_han = 50 if v_kmh > 55 else 40

    # Nội dung câu hỏi
    noidungcauhoi = (f'''Khi một ô tô phanh gấp trên mặt đường khô, tốc độ $v$ (tính bằng $\\text{{m/s}}$) của xe ngay trước khi phanh liên hệ với chiều dài vết trượt lốp xe $s$ (tính bằng mét) theo công thức $v = \\sqrt{{15,6s}}$. Tại hiện trường một vụ kiểm tra an toàn giao thông, cảnh sát đo được vết trượt dài $s = {s}\\text{{ m}}$. Xét tính đúng, sai của các khẳng định sau:''')

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = f'\\True Tốc độ của xe ngay trước khi phanh được tính bởi $v = \\sqrt{{{str_tich}}}\\text{{ m/s}}$.'
    nb_da_1_s = f'Tốc độ của xe ngay trước khi phanh được tính bởi $v = {str_tich}\\text{{ m/s}}$.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1_d = f'Thay $s = {s}$ vào công thức ta được $v = \\sqrt{{15,6 \\cdot {s}}} = \\sqrt{{{str_tich}}}\\text{{ m/s}}$.'
    loigiai_nb_1_s = f'Sai. Tốc độ của xe là $v = \\sqrt{{15,6 \\cdot {s}}} = \\sqrt{{{str_tich}}}\\text{{ m/s}}$.'

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = f'\\True Làm tròn đến chữ số thập phân thứ hai, tốc độ của xe là ${str_v_ms}\\text{{ m/s}}$.'
    th_da_1_s = f'Làm tròn đến chữ số thập phân thứ hai, tốc độ của xe là ${str_v_ms_sai}\\text{{ m/s}}$.'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1_d = f'Sử dụng máy tính cầm tay ta có $v = \\sqrt{{{str_tich}}} \\approx {v_ms:.4f}\\dots \\approx {str_v_ms}\\text{{ m/s}}$.'
    loigiai_th_1_s = f'Sai. Ta có $v = \\sqrt{{{str_tich}}} \\approx {v_ms:.4f}\\dots \\approx {str_v_ms}\\text{{ m/s}}$.'

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = f'\\True Đổi sang đơn vị $\\text{{km/h}}$ (với $v \\approx {str_v_ms}\\text{{ m/s}}$ và $1\\text{{ m/s}} = 3,6\\text{{ km/h}}$), tốc độ của xe là ${str_v_kmh}\\text{{ km/h}}$.'
    vd_da_1_s = f'Đổi sang đơn vị $\\text{{km/h}}$ (với $v \\approx {str_v_ms}\\text{{ m/s}}$ và $1\\text{{ m/s}} = 3,6\\text{{ km/h}}$), tốc độ của xe là ${str(round(v_ms_tron / 3.6, 2)).replace(".", ",")}\\text{{ km/h}}$.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1_d = f'Ta có $v \\approx {str_v_ms} \\cdot 3,6 = {str_v_kmh}\\text{{ km/h}}$.'
    loigiai_vd_1_s = f'Sai. Đổi từ $\\text{{m/s}}$ sang $\\text{{km/h}}$ ta nhân với $3,6$: ${str_v_ms} \\cdot 3,6 = {str_v_kmh}\\text{{ km/h}}$.'

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = f'\\True Nếu đoạn đường đó quy định tốc độ tối đa là ${gioi_han}\\text{{ km/h}}$ thì người lái xe đã vượt quá tốc độ cho phép.'
    vdc_da_1_s = f'Nếu đoạn đường đó quy định tốc độ tối đa là ${gioi_han}\\text{{ km/h}}$ thì người lái xe đã chạy đúng tốc độ cho phép.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1_d = f'Vì tốc độ của xe là ${str_v_kmh}\\text{{ km/h}} > {gioi_han}\\text{{ km/h}}$ nên người lái xe đã vượt quá tốc độ cho phép.'
    loigiai_vdc_1_s = f'Sai. Vì ${str_v_kmh}\\text{{ km/h}} > {gioi_han}\\text{{ km/h}}$ nên xe đã chạy quá tốc độ quy định.'

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
