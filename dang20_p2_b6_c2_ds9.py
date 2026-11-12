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


def bt_dang20_p2_b6_c2_ds9(self):
    # Khai báo biến: Tổng N_tong áo trong T_tong ngày. T1 ngày đầu may N1 áo/ngày.
    T_tong = random.choice([15, 18, 20])
    T1 = random.choice([5, 6])
    T2 = T_tong - T1
    N1 = random.choice([60, 70, 80])
    da_may = T1 * N1
    x_min = randint(85, 110)
    N_tong = da_may + T2 * x_min
    
    noidungcauhoi = ('''Một xưởng may nhận đơn hàng sản xuất $%s$ chiếc áo trong vòng $%s$ ngày. Trong $%s$ ngày đầu tiên, xưởng may được trung bình $%s$ chiếc áo mỗi ngày. Gọi $x$ (chiếc áo/ngày, $x \\in \\mathbb{N}^*$) là năng suất trung bình trong những ngày còn lại để xưởng hoàn thành đơn hàng đúng hoặc trước thời hạn.'''
                     % (N_tong, T_tong, T1, N1))
    
    # Mệnh đề a
    nb_da_1_d = '\\True Tổng số áo xưởng may được trong $%s$ ngày đầu là $%s$ chiếc.' % (T1, da_may)
    nb_da_1_s = 'Tổng số áo xưởng may được trong $%s$ ngày đầu là $%s$ chiếc.' % (T1, da_may + N1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Trong $%s$ ngày đầu, xưởng may được $%s \\cdot %s = %s$ (chiếc áo).''' % (T1, T1, N1, da_may))
    
    # Mệnh đề b
    th_da_1_d = '\\True Số ngày còn lại theo kế hoạch của đơn hàng là $%s$ ngày.' % T2
    th_da_1_s = 'Số ngày còn lại theo kế hoạch của đơn hàng là $%s$ ngày.' % (T2 + 1)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Số ngày còn lại theo kế hoạch là $%s - %s = %s$ (ngày).''' % (T_tong, T1, T2))
    
    # Mệnh đề c
    vd_da_1_d = '\\True Bất phương trình biểu thị điều kiện hoàn thành đơn hàng đúng hoặc trước hạn là $%s + %sx \\ge %s$.' % (da_may, T2, N_tong)
    vd_da_1_s = 'Bất phương trình biểu thị điều kiện hoàn thành đơn hàng đúng hoặc trước hạn là $%s + %sx \\le %s$.' % (da_may, T2, N_tong)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Tổng số áo may được trong cả đợt là $%s + %sx$. Để hoàn thành đúng hoặc trước hạn thì tổng số áo phải từ $%s$ chiếc trở lên: $%s + %sx \\ge %s$.'''
                    % (da_may, T2, N_tong, da_may, T2, N_tong))
    
    # Mệnh đề d
    vdc_da_1_d = '\\True Trong $%s$ ngày còn lại, mỗi ngày xưởng phải may ít nhất $%s$ chiếc áo.' % (T2, x_min)
    vdc_da_1_s = 'Trong $%s$ ngày còn lại, mỗi ngày xưởng phải may ít nhất $%s$ chiếc áo.' % (T2, x_min + 5)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $%s + %sx \\ge %s \\Leftrightarrow %sx \\ge %s \\Leftrightarrow x \\ge %s$. Vậy mỗi ngày xưởng phải may ít nhất $%s$ chiếc áo.'''
                     % (da_may, T2, N_tong, T2, N_tong - da_may, x_min, x_min))
    
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
