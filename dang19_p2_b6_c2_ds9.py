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


def bt_dang19_p2_b6_c2_ds9(self):
    # Khai báo biến: Bậc 1 (50 kWh đầu): g1 đồng/kWh; Bậc 2 (51-100): g2 đồng/kWh
    g1 = random.choice([1700, 1800])
    g2 = g1 + random.choice([100, 200])
    tien_b1 = 50 * g1
    hieu_g = 50 * (g2 - g1) # tien_b1 - 50*g2 = -hieu_g
    x_max = randint(70, 95)
    ngan_sach = tien_b1 + g2 * (x_max - 50)
    
    noidungcauhoi = ('''Giá bán lẻ điện sinh hoạt của một hộ gia đình được tính như sau: $50\\text{ kWh}$ đầu tiên có giá $%s$ đồng/$\\text{kWh}$; từ $\\text{kWh}$ thứ $51$ đến $100$ có giá $%s$ đồng/$\\text{kWh}$. Trong tháng 10, gia đình bác Hùng sử dụng hết $x\\text{ kWh}$ điện ($50 < x \\le 100$) và dự trù số tiền điện không vượt quá $%s$ đồng.'''
                     % (g1, g2, ngan_sach))
    
    # Mệnh đề a
    nb_da_1_d = '\\True Số tiền điện phải trả cho $50\\text{ kWh}$ đầu tiên là $%s$ đồng.' % tien_b1
    nb_da_1_s = 'Số tiền điện phải trả cho $50\\text{ kWh}$ đầu tiên là $%s$ đồng.' % (50 * g2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Số tiền cho $50\\text{ kWh}$ bậc 1 là $50 \\cdot %s = %s$ (đồng).''' % (g1, tien_b1))
    
    # Mệnh đề b
    th_da_1_d = '\\True Tổng số tiền điện gia đình bác Hùng phải trả trong tháng 10 là $%s + %s(x - 50)$ (đồng).' % (tien_b1, g2)
    th_da_1_s = 'Tổng số tiền điện gia đình bác Hùng phải trả trong tháng 10 là $%s + %sx$ (đồng).' % (tien_b1, g2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Số điện ở bậc 2 là $x - 50$ ($\\text{kWh}$) nên tổng tiền điện là $%s + %s(x - 50)$ (đồng).''' % (tien_b1, g2))
    
    # Mệnh đề c
    vd_da_1_d = '\\True Bất phương trình biểu diễn dự trù kinh phí của gia đình bác Hùng là $%sx - %s \\le %s$.' % (g2, hieu_g, ngan_sach)
    vd_da_1_s = 'Bất phương trình biểu diễn dự trù kinh phí của gia đình bác Hùng là $%sx + %s \\le %s$.' % (g2, hieu_g, ngan_sach)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $%s + %s(x - 50) \\le %s \\Leftrightarrow %s + %sx - %s \\le %s \\Leftrightarrow %sx - %s \\le %s$.'''
                    % (tien_b1, g2, ngan_sach, tien_b1, g2, 50*g2, ngan_sach, g2, hieu_g, ngan_sach))
    
    # Mệnh đề d
    vdc_da_1_d = '\\True Gia đình bác Hùng có thể sử dụng tối đa $%s\\text{ kWh}$ điện trong tháng 10 để không vượt mức dự trù.' % x_max
    vdc_da_1_s = 'Gia đình bác Hùng có thể sử dụng tối đa $%s\\text{ kWh}$ điện trong tháng 10 để không vượt mức dự trù.' % (x_max + 5)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Giải bất phương trình $%sx - %s \\le %s \\Leftrightarrow %sx \\le %s \\Leftrightarrow x \\le %s$. Vậy gia đình sử dụng tối đa $%s\\text{ kWh}$.'''
                     % (g2, hieu_g, ngan_sach, g2, ngan_sach + hieu_g, x_max, x_max))
    
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
