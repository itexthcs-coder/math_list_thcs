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

def bt_Dang14_p1_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        g1 = randint(12, 43)
        g2 = 90 - g1
        k = randint(2, 7)
        loai = random.choice([1, 2, 3])
        if loai == 1:
            bieu_thuc = '\\dfrac{%d\\tan %d^{\\circ}}{\\cot %d^{\\circ}}' % (k, g1, g2)
            kq = k
            giai_thich = 'Vì $%d^{\\circ} + %d^{\\circ} = 90^{\\circ}$ nên $\\tan %d^{\\circ} = \\cot %d^{\\circ}$. \\\\ Do đó $\\dfrac{%d\\tan %d^{\\circ}}{\\cot %d^{\\circ}} = \\dfrac{%d\\cot %d^{\\circ}}{\\cot %d^{\\circ}} = %d$.' % (g1, g2, g1, g2, k, g1, g2, k, g2, g2, k)
        elif loai == 2:
            bieu_thuc = '%d\\sin %d^{\\circ} - %d\\cos %d^{\\circ}' % (k, g1, k, g2)
            kq = 0
            giai_thich = 'Vì $%d^{\\circ} + %d^{\\circ} = 90^{\\circ}$ nên $\\sin %d^{\\circ} = \\cos %d^{\\circ}$. \\\\ Do đó $%d\\sin %d^{\\circ} - %d\\cos %d^{\\circ} = %d\\cos %d^{\\circ} - %d\\cos %d^{\\circ} = 0$.' % (g1, g2, g1, g2, k, g1, k, g2, k, g2, k, g2)
        else:
            bieu_thuc = '\\dfrac{\\sin %d^{\\circ}}{\\cos %d^{\\circ}} + \\dfrac{\\tan %d^{\\circ}}{\\cot %d^{\\circ}}' % (g1, g2, g2, g1)
            kq = 2
            giai_thich = 'Vì $%d^{\\circ} + %d^{\\circ} = 90^{\\circ}$ nên $\\sin %d^{\\circ} = \\cos %d^{\\circ}$ và $\\tan %d^{\\circ} = \\cot %d^{\\circ}$. \\\\ Do đó $\\dfrac{\\sin %d^{\\circ}}{\\cos %d^{\\circ}} + \\dfrac{\\tan %d^{\\circ}}{\\cot %d^{\\circ}} = 1 + 1 = 2$.' % (g1, g2, g1, g2, g2, g1, g1, g2, g2, g1)
            
        ds_sai = [x_val for x_val in [-1, 0, 1, 2, k, -k, k + 1] if x_val != kq]
        
        da = '$%d$' % kq
        das1 = '$%d$' % ds_sai[0]
        das2 = '$%d$' % ds_sai[1]
        das3 = '$%d$' % ds_sai[2]
        
        # Câu hỏi
        noidungcauhoi = ('''Giá trị của biểu thức $A = %s$ bằng'''
                         % (bieu_thuc))
        
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
                   % (giai_thich))
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
