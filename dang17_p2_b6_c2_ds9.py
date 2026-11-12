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


def bt_dang17_p2_b6_c2_ds9(self):
    # Khai báo biến:
    # Gói A: Thuê bao tbA, miễn phí mpA phút, vượt mức giaA/phút => tbA + giaA*(x - mpA)
    # Gói B: Thuê bao tbB, không miễn phí, giaB/phút => tbB + giaB*x
    bo_goi = [
        (50, 60, 0.8, 80, 0.5, 260, 250),
        (40, 50, 0.6, 70, 0.4, 300, 280),
        (60, 60, 0.7, 90, 0.4, 240, 220)
    ]
    tbA, mpA, giaA, tbB, giaB, moc_x, x_test = random.choice(bo_goi)
    
    noidungcauhoi = ('''Một công ty viễn thông cung cấp hai gói cước gọi nội mạng hằng tháng:
    \\begin{itemize}
    \\item \\textbf{Gói A:} Cước thuê bao $%s$ nghìn đồng/tháng, miễn phí $%s$ phút đầu tiên, từ phút thứ $%s$ trở đi tính giá $%s$ nghìn đồng/phút.
    \\item \\textbf{Gói B:} Cước thuê bao $%s$ nghìn đồng/tháng, không có phút miễn phí, tính giá $%s$ nghìn đồng/phút cho toàn bộ thời gian gọi.
    \\end{itemize}
    Gọi $x$ (phút, $x > %s$) là thời gian gọi trong một tháng của khách hàng.'''
                     % (tbA, mpA, mpA + 1, str(giaA).replace('.', ','), tbB, str(giaB).replace('.', ','), mpA))
    
    # Mệnh đề a
    nb_da_1_d = '\\True Số tiền khách hàng phải trả trong một tháng nếu dùng Gói A là $%s + %s(x - %s)$ (nghìn đồng).' % (tbA, str(giaA).replace('.', ','), mpA)
    nb_da_1_s = 'Số tiền khách hàng phải trả trong một tháng nếu dùng Gói A là $%s + %sx$ (nghìn đồng).' % (tbA, str(giaA).replace('.', ','))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì miễn phí $%s$ phút đầu nên số phút tính cước thêm là $x - %s$, do đó tổng cước Gói A là $%s + %s(x - %s)$ (nghìn đồng).'''
                    % (mpA, mpA, tbA, str(giaA).replace('.', ','), mpA))
    
    # Mệnh đề b
    th_da_1_d = '\\True Số tiền khách hàng phải trả trong một tháng nếu dùng Gói B là $%s + %sx$ (nghìn đồng).' % (tbB, str(giaB).replace('.', ','))
    th_da_1_s = 'Số tiền khách hàng phải trả trong một tháng nếu dùng Gói B là $%s + %s(x - %s)$ (nghìn đồng).' % (tbB, str(giaB).replace('.', ','), mpA)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Gói B không có phút miễn phí nên cước phải trả là $%s + %sx$ (nghìn đồng).'''
                    % (tbB, str(giaB).replace('.', ',')))
    
    # Mệnh đề c
    vd_da_1_d = '\\True Chi phí dùng Gói B rẻ hơn Gói A khi $%s + %sx < %s + %s(x - %s)$.' % (tbB, str(giaB).replace('.', ','), tbA, str(giaA).replace('.', ','), mpA)
    vd_da_1_s = 'Chi phí dùng Gói B rẻ hơn Gói A khi $%s + %sx > %s + %s(x - %s)$.' % (tbB, str(giaB).replace('.', ','), tbA, str(giaA).replace('.', ','), mpA)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Để Gói B tiết kiệm hơn Gói A thì số tiền trả cho Gói B phải nhỏ hơn Gói A: $%s + %sx < %s + %s(x - %s)$.'''
                    % (tbB, str(giaB).replace('.', ','), tbA, str(giaA).replace('.', ','), mpA))
    
    # Mệnh đề d
    vdc_da_1_d = '\\True Nếu một khách hàng gọi $%s$ phút trong tháng thì nên chọn Gói A để tiết kiệm chi phí hơn.' % x_test
    vdc_da_1_s = 'Nếu một khách hàng gọi $%s$ phút trong tháng thì nên chọn Gói B để tiết kiệm chi phí hơn.' % x_test
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Giải bất phương trình $%s + %sx < %s + %s(x - %s)$ ta được $x > %s$. Vì $x = %s < %s$ nên Gói A có chi phí rẻ hơn Gói B.'''
                     % (tbB, str(giaB).replace('.', ','), tbA, str(giaA).replace('.', ','), mpA, moc_x, x_test, moc_x))
    
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
