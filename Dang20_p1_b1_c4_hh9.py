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

def bt_Dang20_p1_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh_ben = random.choice([5, 10, 13, 17, 25])
        if canh_ben in [5, 10]:
            nua_day = 3 if canh_ben == 5 else 6
            duong_cao = 4 if canh_ben == 5 else 8
        elif canh_ben == 13:
            nua_day = 5
            duong_cao = 12
        elif canh_ben == 17:
            nua_day = 8
            duong_cao = 15
        else:
            nua_day = 7
            duong_cao = 24
        canh_day = 2 * nua_day
        
        ham = random.choice(['sin', 'cos', 'tan'])
        if ham == 'sin':
            kq = Rational(duong_cao, canh_ben)
            sai_1 = Rational(nua_day, canh_ben)
            sai_2 = Rational(duong_cao, canh_day)
            sai_3 = Rational(canh_day, canh_ben)
            ct = '\\sin B = \\dfrac{AH}{AB} = \\dfrac{%d}{%d} = %s' % (duong_cao, canh_ben, latex(kq))
        elif ham == 'cos':
            kq = Rational(nua_day, canh_ben)
            sai_1 = Rational(duong_cao, canh_ben)
            sai_2 = Rational(canh_day, canh_ben)
            sai_3 = Rational(nua_day, duong_cao)
            ct = '\\cos B = \\dfrac{BH}{AB} = \\dfrac{%d}{%d} = %s' % (nua_day, canh_ben, latex(kq))
        else:
            kq = Rational(duong_cao, nua_day)
            sai_1 = Rational(duong_cao, canh_day)
            sai_2 = Rational(nua_day, duong_cao)
            sai_3 = Rational(duong_cao, canh_ben)
            ct = '\\tan B = \\dfrac{AH}{BH} = \\dfrac{%d}{%d} = %s' % (duong_cao, nua_day, latex(kq))
            
        da = '$%s$' % latex(kq)
        das1 = '$%s$' % latex(sai_1)
        das2 = '$%s$' % latex(sai_2)
        das3 = '$%s$' % latex(sai_3)
        
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4,0);\n'
            '\\coordinate (H) at (2,0);\n'
            '\\coordinate (A) at (2,3.2);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
            '\\draw[line width=1pt] (A)--(H);\n'
            '\\draw[line width=1pt] (2,0.25)--(2.25,0.25)--(2.25,0);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        
        # Câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ cân tại $A$ có cạnh bên $AB = AC = %d\\text{ cm}$ và cạnh đáy $BC = %d\\text{ cm}$ (như hình vẽ). Giá trị của $\\%s B$ bằng %s'''
                         % (canh_ben, canh_day, ham, hinh_ve))
        
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        # Nội dung lời giải
        loigiai = ('''Kẻ đường cao $AH$ của tam giác cân $ABC$ ($H \\in BC$). \\\\
        Vì $\\triangle ABC$ cân tại $A$ nên đường cao $AH$ đồng thời là đường trung tuyến, suy ra $BH = \\dfrac{BC}{2} = \\dfrac{%d}{2} = %d\\text{ (cm)}$. \\\\
        Xét $\\triangle ABH$ vuông tại $H$, theo định lí Pythagore ta có: \\\\
        $AH = \\sqrt{AB^2 - BH^2} = \\sqrt{%d^2 - %d^2} = %d\\text{ (cm)}$. \\\\
        Vậy $%s$.'''
                   % (canh_day, nua_day, canh_ben, nua_day, duong_cao, ct))
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
