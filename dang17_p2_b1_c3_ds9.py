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


def bt_dang17_p2_b1_c3_ds9(self):
    # Khai báo biến
    bo_pythagore = [(5, 3, 4), (10, 6, 8), (13, 5, 12)]
    L, x_dep, h_dep = random.choice(bo_pythagore)
    L2 = L**2
    x_le = 2 if L == 5 else 4
    h_le_sq = L2 - x_le**2
    h_le_val = math.sqrt(h_le_sq)
    moc_ss = round(h_le_val + 0.05, 1)
    str_moc_ss = str(moc_ss).replace('.', ',')
    str_h_le = f"{h_le_val:.2f}".replace('.', ',')

    # Nội dung câu hỏi
    noidungcauhoi = (f'''Một chiếc thang dài ${L}\\text{{ m}}$ được đặt dựa vào một bức tường thẳng đứng, chân thang cách chân tường một khoảng $x\\text{{ (m)}}$ ($0 < x < {L}$). Gọi $h\\text{{ (m)}}$ là chiều cao từ mặt đất lên tới đầu thang chạm tường. Xét tính đúng, sai của các khẳng định sau:''')

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = f'\\True Biểu thức tính chiều cao $h$ theo $x$ là $h = \\sqrt{{{L2} - x^2}}$.'
    nb_da_1_s = f'Biểu thức tính chiều cao $h$ theo $x$ là $h = \\sqrt{{{L2} + x^2}}$.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1_d = f'Áp dụng định lí Pythagore cho tam giác vuông tạo bởi thang, tường và mặt đất, ta có $h^2 + x^2 = {L}^2 \\Rightarrow h = \\sqrt{{{L2} - x^2}}$.'
    loigiai_nb_1_s = f'Sai. Theo định lí Pythagore, $h^2 = {L}^2 - x^2$ nên $h = \\sqrt{{{L2} - x^2}}$.'

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = f'\\True Biểu thức $\\sqrt{{{L2} - x^2}}$ xác định khi $-{L} \\le x \\le {L}$.'
    th_da_1_s = f'Biểu thức $\\sqrt{{{L2} - x^2}}$ xác định với mọi số thực $x$.'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1_d = f'Biểu thức $\\sqrt{{{L2} - x^2}}$ xác định khi ${L2} - x^2 \\ge 0 \\Leftrightarrow x^2 \\le {L2} \\Leftrightarrow -{L} \\le x \\le {L}$.'
    loigiai_th_1_s = f'Sai. Nếu $|x| > {L}$ thì ${L2} - x^2 < 0$ nên căn thức không xác định.'

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = f'\\True Khi chân thang cách chân tường ${x_dep}\\text{{ m}}$ thì đầu thang ở độ cao ${h_dep}\\text{{ m}}$ so với mặt đất.'
    vd_da_1_s = f'Khi chân thang cách chân tường ${x_dep}\\text{{ m}}$ thì đầu thang ở độ cao ${h_dep + 1}\\text{{ m}}$ so với mặt đất.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1_d = f'Thay $x = {x_dep}$ vào công thức ta được $h = \\sqrt{{{L2} - {x_dep}^2}} = \\sqrt{{{h_dep**2}}} = {h_dep}\\text{{ m}}$.'
    loigiai_vd_1_s = f'Sai. Tại $x = {x_dep}$, chiều cao đầu thang là $h = \\sqrt{{{L2} - {x_dep}^2}} = {h_dep}\\text{{ m}}$.'

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = f'\\True Khi chân thang cách chân tường ${x_le}\\text{{ m}}$ thì đầu thang ở độ cao nhỏ hơn ${str_moc_ss}\\text{{ m}}$.'
    vdc_da_1_s = f'Khi chân thang cách chân tường ${x_le}\\text{{ m}}$ thì đầu thang ở độ cao lớn hơn ${str_moc_ss}\\text{{ m}}$.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1_d = f'Tại $x = {x_le}$, ta có $h = \\sqrt{{{L2} - {x_le}^2}} = \\sqrt{{{h_le_sq}}} \\approx {str_h_le}\\text{{ m}} < {str_moc_ss}\\text{{ m}}$.'
    loigiai_vdc_1_s = f'Sai. Tại $x = {x_le}$, $h = \\sqrt{{{h_le_sq}}} \\approx {str_h_le}\\text{{ m}} < {str_moc_ss}\\text{{ m}}$.'

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
