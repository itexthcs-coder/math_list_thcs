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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_Dang2_p1_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        goc_ky_hieu = random.choice(['\\alpha', '\\beta', '\\varphi'])
        truong_hop = random.choice([1, 2, 3])
        if truong_hop == 1:
            da = '$0 < \\sin %s < 1$' % goc_ky_hieu
            s = [
                '$\\sin %s > 1$' % goc_ky_hieu,
                '$\\cos %s < 0$' % goc_ky_hieu,
                '$\\cos %s > 1$' % goc_ky_hieu
            ]
            gt = 'Vì trong tam giác vuông, cạnh huyền luôn lớn hơn mỗi cạnh góc vuông nên tỉ số giữa cạnh đối và cạnh huyền luôn lớn hơn $0$ và nhỏ hơn $1$, tức là $0 < \\sin %s < 1$.' % goc_ky_hieu
        elif truong_hop == 2:
            da = '$0 < \\cos %s < 1$' % goc_ky_hieu
            s = [
                '$\\cos %s > 1$' % goc_ky_hieu,
                '$\\sin %s \\le 0$' % goc_ky_hieu,
                '$\\sin %s \\ge 1$' % goc_ky_hieu
            ]
            gt = 'Vì trong tam giác vuông, cạnh huyền luôn lớn hơn mỗi cạnh góc vuông nên tỉ số giữa cạnh kề và cạnh huyền luôn lớn hơn $0$ và nhỏ hơn $1$, tức là $0 < \\cos %s < 1$.' % goc_ky_hieu
        else:
            da = '$\\cot %s = \\dfrac{1}{\\tan %s}$' % (goc_ky_hieu, goc_ky_hieu)
            s = [
                '$\\tan %s + \\cot %s = 1$' % (goc_ky_hieu, goc_ky_hieu),
                '$\\sin %s = \\dfrac{1}{\\cos %s}$' % (goc_ky_hieu, goc_ky_hieu),
                '$\\tan %s = \\dfrac{\\cos %s}{\\sin %s}$' % (goc_ky_hieu, goc_ky_hieu, goc_ky_hieu)
            ]
            gt = 'Theo định nghĩa tỉ số lượng giác của góc nhọn, $\\tan %s = \\dfrac{\\text{cạnh đối}}{\\text{cạnh kề}}$ và $\\cot %s = \\dfrac{\\text{cạnh kề}}{\\text{cạnh đối}}$ nên $\\cot %s = \\dfrac{1}{\\tan %s}$.' % (goc_ky_hieu, goc_ky_hieu, goc_ky_hieu, goc_ky_hieu)
            
        das1 = s[0]
        das2 = s[1]
        das3 = s[2]
        
        # Câu hỏi
        noidungcauhoi = ('''Cho góc nhọn $%s$. Khẳng định nào sau đây là đúng?'''
                         % (goc_ky_hieu))
        
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        # Nội dung lời giải
        loigiai = ('''%s'''
                   % (gt))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
