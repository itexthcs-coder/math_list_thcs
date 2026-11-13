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

def bt_Dang14_p3_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = randint(3, 6)
        ad = random.choice([3, 6])
        k = ad // 3
        cd_val = ab + k * math.sqrt(3)
        number = Decimal(str(cd_val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
        
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (C) at (4.5,0);\n'
            '\\coordinate (H) at (2.2,0);\n'
            '\\coordinate (A) at (0,2.6);\n'
            '\\coordinate (B) at (2.2,2.6);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
            '\\draw[line width=1pt, dashed] (B)--(H);\n'
            '\\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);\n'
            '\\draw[line width=1pt] (2.2,0.3)--(2.5,0.3)--(2.5,0);\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (B) circle (1pt) node[above right] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below left] {$D$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thang vuông $ABCD$ ($\\widehat{A} = \\widehat{D} = 90^{\\circ}$) có đáy nhỏ $AB = %d\\text{ cm}$, cạnh bên $AD = %d\\text{ cm}$ và góc $\\widehat{C} = 60^{\\circ}$ (như hình vẽ). Tính độ dài đáy lớn $CD$ theo đơn vị xăng-ti-mét (làm tròn kết quả đến hàng phần trăm). %s'''
                         % (ab, ad, hinh_ve))
        
        # Nội dung lời giải
        loigiai = ('''Kẻ đường cao $BH$ vuông góc với $CD$ tại $H$. Tứ giác $ABHD$ có ba góc vuông nên là hình chữ nhật, suy ra $BH = AD = %d\\text{ cm}$ và $DH = AB = %d\\text{ cm}$. \\\\
        Xét $\\triangle BHC$ vuông tại $H$, ta có: $HC = BH \\cdot \\cot 60^{\\circ} = %d \\cdot \\dfrac{\\sqrt{3}}{3} = %d\\sqrt{3}\\text{ (cm)}$. \\\\
        Độ dài đáy lớn $CD$ là: $CD = DH + HC = %d + %d\\sqrt{3} \\approx %s\\text{ (cm)}$.'''
                   % (ad, ab, ad, k, ab, k, str(kq_str)))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
