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


def bt_dang13_p2_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 2)).replace('.', '{,}')
    
    # Random nồng độ và khối lượng dung dịch
    cases = [
        (500, 12, 10, 20, 400, 100),  # 0.1*400 + 0.2*100 = 60 = 12% * 500
        (600, 15, 10, 25, 400, 200),  # 0.1*400 + 0.25*200 = 90 = 15% * 600
        (400, 18, 15, 25, 280, 120),  # 0.15*280 + 0.25*120 = 42+30=72 = 18% * 400
        (500, 16, 12, 22, 300, 200)   # 0.12*300 + 0.22*200 = 36+44=80 = 16% * 500
    ]
    M_dd, c_sau, c1, c2, x0, y0 = random.choice(cases)
    m_muoi = (M_dd * c_sau) // 100
    
    noidungcauhoi = ('''Trong phòng thí nghiệm, một học sinh cần pha chế $%s\\text{ g}$ dung dịch muối ăn nồng độ $%s\\%%$ từ hai loại dung dịch muối có sẵn là dung dịch loại I nồng độ $%s\\%%$ và dung dịch loại II nồng độ $%s\\%%$. Gọi $x\\text{ (g)}$ là khối lượng dung dịch loại I và $y\\text{ (g)}$ là khối lượng dung dịch loại II cần lấy ($0 < x, y < %s$).''' % (M_dd, c_sau, c1, c2, M_dd))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Tổng khối lượng hai dung dịch cần lấy là $x + y = %s$' % M_dd
    nb_da_1_s = 'Tổng khối lượng hai dung dịch cần lấy là $x - y = %s$' % M_dd
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    
    loigiai_nb_1 = ('''Khối lượng dung dịch thu được là $%s\\text{ g}$ nên ta có phương trình $x + y = %s$.''' % (M_dd, M_dd))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Khối lượng muối nguyên chất có trong $%s\\text{ g}$ dung dịch nồng độ $%s\\%%$ là $%s\\text{ g}$' % (M_dd, c_sau, m_muoi)
    th_da_1_s = 'Khối lượng muối nguyên chất có trong $%s\\text{ g}$ dung dịch nồng độ $%s\\%%$ là $%s\\text{ g}$' % (M_dd, c_sau, c_sau)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    
    loigiai_th_1 = ('''Khối lượng muối nguyên chất có trong dung dịch sau khi pha là $%s \\cdot %s\\%% = %s\\text{ (g)}$.''' % (M_dd, c_sau, m_muoi))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Phương trình biểu diễn tổng khối lượng muối nguyên chất là $%sx + %sy = %s$' % (fmt_dec(c1/100), fmt_dec(c2/100), m_muoi)
    vd_da_1_s = 'Phương trình biểu diễn tổng khối lượng muối nguyên chất là $%sx + %sy = %s$' % (c1, c2, m_muoi)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    
    loigiai_vd_1 = ('''Khối lượng muối trong dung dịch loại I là $%sx\\text{ (g)}$ và trong dung dịch loại II là $%sy\\text{ (g)}$ nên ta có $%sx + %sy = %s$.''' % (fmt_dec(c1/100), fmt_dec(c2/100), fmt_dec(c1/100), fmt_dec(c2/100), m_muoi))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Học sinh đó cần lấy $%s\\text{ g}$ dung dịch loại I và $%s\\text{ g}$ dung dịch loại II' % (x0, y0)
    vdc_da_1_s = 'Học sinh đó cần lấy $%s\\text{ g}$ dung dịch loại I và $%s\\text{ g}$ dung dịch loại II' % (y0, x0)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    
    loigiai_vdc_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$ ta được $x = %s$ và $y = %s$ (thỏa mãn).''' % (M_dd, fmt_dec(c1/100), fmt_dec(c2/100), m_muoi, x0, y0))
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
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' '\\choiceTFn \n' '{'+str(shuffled_answers_nb[0])+'}\n' '{'+str(shuffled_answers_th[0])+'}\n' '{'+str(shuffled_answers_vd[0])+'}\n' '{'+str(shuffled_answers_vdc[0])+'}\n' '\\loigiai{ \n' '\\begin{enumEX}[a)]{1} \n' '\\item '+str(shuffled_solutions_nb[0])+'\n' '\\item '+str(shuffled_solutions_th[0])+'\n' '\\item '+str(shuffled_solutions_vd[0])+'\n' '\\item '+str(shuffled_solutions_vdc[0])+'\n' '\\end{enumEX}} \n' '\\end{ex}\n \\end{minipage}\n\n')

    return content
