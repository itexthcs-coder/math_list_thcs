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

def bt_Dang20_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
        doi, ke, huyen = random.choice(bo)
        sin_a = Rational(doi, huyen)
        cos_a = Rational(ke, huyen)
        tan_a = Rational(doi, ke)
        cot_a = Rational(ke, doi)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (4,0);\n'
            '\\coordinate (C) at (0,3);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
            '\\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho góc nhọn $\\alpha$. Chứng minh các hệ thức lượng giác cơ bản sau dựa vào định nghĩa tỉ số lượng giác trong tam giác vuông (xét $\\triangle ABC$ vuông tại $A$ có $\\widehat{B} = \\alpha$ như hình vẽ): %s \\\\
                         a) $\\tan \\alpha = \\dfrac{\\sin \\alpha}{\\cos \\alpha}$ và $\\cot \\alpha = \\dfrac{\\cos \\alpha}{\\sin \\alpha}$. \\\\
                         b) $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$. \\\\
                         c) Vận dụng kết quả trên, biết $\\sin \\alpha = %s$ (với $\\alpha$ nhọn), hãy tính $\\cos \\alpha$, $\\tan \\alpha$ và $\\cot \\alpha$. '''
                         % (hinh_ve, latex(sin_a)))
        
        # Nội dung lời giải
        loigiai = ('''Xét $\\triangle ABC$ vuông tại $A$ có $\\widehat{B} = \\alpha$. Đặt $BC = a$, $AC = b$, $AB = c$. Theo định nghĩa, ta có: \\\\
                   $\\sin \\alpha = \\dfrac{b}{a}$; $\\cos \\alpha = \\dfrac{c}{a}$; $\\tan \\alpha = \\dfrac{b}{c}$; $\\cot \\alpha = \\dfrac{c}{b}$. \\\\
                   \\begin{enumEX}[a)]{1} \n
                        \\item Ta có: $\\dfrac{\\sin \\alpha}{\\cos \\alpha} = \\dfrac{\\frac{b}{a}}{\\frac{c}{a}} = \\dfrac{b}{c} = \\tan \\alpha$; $\\dfrac{\\cos \\alpha}{\\sin \\alpha} = \\dfrac{\\frac{c}{a}}{\\frac{b}{a}} = \\dfrac{c}{b} = \\cot \\alpha$. \n
                        \\item Áp dụng định lí Pythagore trong $\\triangle ABC$ vuông tại $A$, ta có $b^2 + c^2 = a^2$. Do đó: \\\\
                        $\\sin^2 \\alpha + \\cos^2 \\alpha = \\left(\\dfrac{b}{a}\\right)^2 + \\left(\\dfrac{c}{a}\\right)^2 = \\dfrac{b^2 + c^2}{a^2} = \\dfrac{a^2}{a^2} = 1$. \n
                        \\item Vì $\\alpha$ là góc nhọn nên $\\cos \\alpha > 0$. Từ $\\sin^2 \\alpha + \\cos^2 \\alpha = 1$, suy ra: \\\\
                        $\\cos \\alpha = \\sqrt{1 - \\sin^2 \\alpha} = \\sqrt{1 - \\left(%s\\right)^2} = \\sqrt{\\dfrac{%d}{%d}} = %s$. \\\\
                        Từ câu a, ta có: $\\tan \\alpha = \\dfrac{\\sin \\alpha}{\\cos \\alpha} = %s$ và $\\cot \\alpha = \\dfrac{\\cos \\alpha}{\\sin \\alpha} = %s$. \n
                        \\end{enumEX} \n'''
                   % (latex(sin_a), ke**2, huyen**2, latex(cos_a), latex(tan_a), latex(cot_a)))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
