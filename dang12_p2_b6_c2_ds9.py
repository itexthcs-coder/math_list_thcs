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


def bt_dang12_p2_b6_c2_ds9(self):
    # Khai báo biến: Lãi suất r%/năm, cần lãi ít nhất L triệu đồng
    r_list = [(6.5, 52, 800), (7.5, 60, 800), (6.0, 48, 800), (8.0, 56, 700), (7.2, 54, 750)]
    r, L, min_tien = random.choice(r_list)
    r_dec = round(r / 100, 4)
    tien_thieu = min_tien - 50
    lai_thieu = round(tien_thieu * r_dec, 2)
    
    noidungcauhoi = ('''Một ngân hàng áp dụng lãi suất gửi tiết kiệm kì hạn 12 tháng là $%s\\%%/$năm. Cô Lan dự kiến gửi một khoản tiền vào ngân hàng này và mong muốn số tiền lãi hằng năm ít nhất là $%s$ triệu đồng. Gọi $x$ (triệu đồng, $x > 0$) là số tiền cô Lan cần gửi tiết kiệm.'''
                     % (str(r).replace('.', ','), L))
    
    # Mệnh đề a
    nb_da_1_d = '\\True Số tiền lãi cô Lan nhận được sau một năm là $%sx$ (triệu đồng).' % str(r_dec).replace('.', ',')
    nb_da_1_s = 'Số tiền lãi cô Lan nhận được sau một năm là $%sx$ (triệu đồng).' % str(r).replace('.', ',')
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Lãi suất $%s\\%% = %s$ nên số tiền lãi nhận được sau $1$ năm là $%sx$ (triệu đồng).'''
                    % (str(r).replace('.', ','), str(r_dec).replace('.', ','), str(r_dec).replace('.', ',')))
    
    # Mệnh đề b
    th_da_1_d = '\\True Để đạt được mong muốn về tiền lãi, $x$ phải thỏa mãn bất phương trình $%sx \\ge %s$.' % (str(r_dec).replace('.', ','), L)
    th_da_1_s = 'Để đạt được mong muốn về tiền lãi, $x$ phải thỏa mãn bất phương trình $%sx \\le %s$.' % (str(r_dec).replace('.', ','), L)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Số tiền lãi ít nhất là $%s$ triệu đồng nên $%sx \\ge %s$.''' % (L, str(r_dec).replace('.', ','), L))
    
    # Mệnh đề c
    vd_da_1_d = '\\True Số tiền tối thiểu cô Lan cần gửi tiết kiệm là $%s$ triệu đồng.' % min_tien
    vd_da_1_s = 'Số tiền tối thiểu cô Lan cần gửi tiết kiệm là $%s$ triệu đồng.' % (min_tien + 100)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $%sx \\ge %s \\Leftrightarrow x \\ge %s : %s = %s$. Vậy số tiền tối thiểu cần gửi là $%s$ triệu đồng.'''
                    % (str(r_dec).replace('.', ','), L, L, str(r_dec).replace('.', ','), min_tien, min_tien))
    
    # Mệnh đề d
    vdc_da_1_d = '\\True Nếu cô Lan gửi $%s$ triệu đồng thì sau một năm số tiền lãi nhận được chưa đạt mức mong muốn.' % tien_thieu
    vdc_da_1_s = 'Nếu cô Lan gửi $%s$ triệu đồng thì sau một năm số tiền lãi nhận được vượt mức mong muốn.' % tien_thieu
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Với $x = %s$ triệu đồng, tiền lãi nhận được là $%s \\cdot %s = %s < %s$ (triệu đồng), chưa đạt mức mong muốn.'''
                     % (tien_thieu, tien_thieu, str(r_dec).replace('.', ','), str(lai_thieu).replace('.', ','), L))
    
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
