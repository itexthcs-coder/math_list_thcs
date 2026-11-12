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


def bt_dang15_p2_b6_c2_ds9(self):
    # Khai báo biến: Tổng N câu, đúng +d điểm, sai -s điểm, tặng sẵn T điểm, cần đạt >= M điểm
    N = random.choice([25, 30, 40])
    d_cong = random.choice([2, 3])
    s_tru = 1
    T_tang = random.choice([5, 10])
    min_dung = randint(int(0.6*N), int(0.8*N))
    # Điểm = T_tang + d_cong*x - s_tru*(N - x) = (d_cong + s_tru)*x + (T_tang - s_tru*N)
    heso_x = d_cong + s_tru
    hang_so = T_tang - s_tru*N
    M_chuan = heso_x * min_dung + hang_so - 1 # Để x >= min_dung - 1/(heso_x) => x >= min_dung
    
    noidungcauhoi = ('''Trong một cuộc thi tuyển dụng gồm $%s$ câu hỏi trắc nghiệm, mỗi câu trả lời đúng được cộng $%s$ điểm, mỗi câu trả lời sai bị trừ $%s$ điểm. Ban tổ chức tặng sẵn cho mỗi thí sinh $%s$ điểm. Thí sinh phải trả lời hết $%s$ câu hỏi và đạt từ $%s$ điểm trở lên mới trúng tuyển. Gọi $x$ ($x \\in \\mathbb{N}, x \\le %s$) là số câu trả lời đúng của một thí sinh.'''
                     % (N, d_cong, s_tru, T_tang, N, M_chuan, N))
    
    # Mệnh đề a
    nb_da_1_d = '\\True Số câu trả lời sai của thí sinh đó là $%s - x$ (câu).' % N
    nb_da_1_s = 'Số câu trả lời sai của thí sinh đó là $x - %s$ (câu).' % N
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì thí sinh phải trả lời hết $%s$ câu hỏi và có $x$ câu trả lời đúng nên số câu trả lời sai là $%s - x$ (câu).''' % (N, N))
    
    # Mệnh đề b
    th_da_1_d = '\\True Tổng số điểm thí sinh đạt được là $%s + %sx - (%s - x)$.' % (T_tang, d_cong, N)
    th_da_1_s = 'Tổng số điểm thí sinh đạt được là $%s + %sx + (%s - x)$.' % (T_tang, d_cong, N)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tổng điểm gồm $%s$ điểm tặng sẵn, cộng $%sx$ điểm từ các câu đúng và trừ đi $1 \\cdot (%s - x)$ điểm từ các câu sai: $%s + %sx - (%s - x)$.'''
                    % (T_tang, d_cong, N, T_tang, d_cong, N))
    
    # Mệnh đề c
    bt_rutgon = latex(heso_x*x + hang_so)
    vd_da_1_d = '\\True Bất phương trình để thí sinh trúng tuyển là $%s \\ge %s$.' % (bt_rutgon, M_chuan)
    vd_da_1_s = 'Bất phương trình để thí sinh trúng tuyển là $%s > %s$.' % (bt_rutgon, M_chuan)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Rút gọn biểu thức điểm ta được $%s$. Vì thí sinh cần đạt từ $%s$ điểm trở lên nên ta có $%s \\ge %s$.'''
                    % (bt_rutgon, M_chuan, bt_rutgon, M_chuan))
    
    # Mệnh đề d
    vdc_da_1_d = '\\True Thí sinh cần trả lời đúng ít nhất $%s$ câu hỏi thì mới trúng tuyển.' % min_dung
    vdc_da_1_s = 'Thí sinh cần trả lời đúng ít nhất $%s$ câu hỏi thì mới trúng tuyển.' % (min_dung - 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Giải bất phương trình $%s \\ge %s \\Leftrightarrow %sx \\ge %s \\Leftrightarrow x \\ge %.2f$. Vì $x \\in \\mathbb{N}$ nên thí sinh cần trả lời đúng ít nhất $%s$ câu.'''
                     % (bt_rutgon, M_chuan, heso_x, M_chuan - hang_so, (M_chuan - hang_so)/heso_x, min_dung))
    
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
