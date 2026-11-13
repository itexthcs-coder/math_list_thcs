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

def bt_Dang12_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([4, 6, 8, 10])
        dh = random.choice([2, 3, 4, 5])
        cd = ab + 2 * dh
        ad = 2 * dh
        ah_kq = dh * sqrt(3)
        hc = ab + dh
        ac_sq = 3 * (dh ** 2) + hc ** 2
        ac_kq = sqrt(ac_sq)
        tan_acd = simplify(ah_kq / hc)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (C) at (5,0);\n'
            '\\coordinate (H) at (1.2,0);\n'
            '\\coordinate (K) at (3.8,0);\n'
            '\\coordinate (A) at (1.2,2.1);\n'
            '\\coordinate (B) at (3.8,2.1);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
            '\\draw[line width=1pt] (A)--(C);\n'
            '\\draw[line width=1pt, dashed] (A)--(H) (B)--(K);\n'
            '\\draw[line width=1pt] (1.2,0.25)--(1.45,0.25)--(1.45,0);\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (B) circle (1pt) node[above right] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below left] {$D$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\fill (K) circle (1pt) node[below] {$K$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thang cân $ABCD$ ($AB // CD$, $AB < CD$) có đáy nhỏ $AB = %d\\text{ cm}$, đáy lớn $CD = %d\\text{ cm}$ và góc đáy $\\widehat{D} = 60^{\\circ}$ (như hình vẽ). %s \\\\
                         a) Tính độ dài đường cao và cạnh bên của hình thang cân $ABCD$. \\\\
                         b) Tính độ dài đường chéo $AC$ và $\\tan \\widehat{ACD}$. '''
                         % (ab, cd, hinh_ve))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Kẻ hai đường cao $AH$ và $BK$ xuống đáy lớn $CD$ ($H, K \\in CD$). Tứ giác $ABKH$ là hình chữ nhật nên $HK = AB = %d\\text{ cm}$. \\\\
                        Vì $ABCD$ là hình thang cân nên $DH = CK = \\dfrac{CD - AB}{2} = \\dfrac{%d - %d}{2} = %d\\text{ cm}$. \\\\
                        Xét $\\triangle ADH$ vuông tại $H$, ta có: \\\\
                        $AH = DH \\cdot \\tan 60^{\\circ} = %s\\text{ (cm)}$; $AD = \\dfrac{DH}{\\cos 60^{\\circ}} = \\dfrac{%d}{\\frac{1}{2}} = %d\\text{ (cm)}$. \n
                        \\item Ta có $HC = HK + KC = %d + %d = %d\\text{ cm}$. \\\\
                        Xét $\\triangle AHC$ vuông tại $H$, theo định lí Pythagore ta có: \\\\
                        $AC = \\sqrt{AH^2 + HC^2} = \\sqrt{(%s)^2 + %d^2} = \\sqrt{%d} = %s\\text{ (cm)}$. \\\\
                        Tỉ số lượng giác $\\tan \\widehat{ACD} = \\dfrac{AH}{HC} = \\dfrac{%s}{%d} = %s$. \n
                        \\end{enumEX} \n'''
                   % (ab, cd, ab, dh, latex(ah_kq), dh, ad,
                      ab, dh, hc, latex(ah_kq), hc, ac_sq, latex(ac_kq), latex(ah_kq), hc, latex(tan_acd)))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
