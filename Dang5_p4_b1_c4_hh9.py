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

def bt_Dang5_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]
        doi, ke, huyen = random.choice(bo)
        tan_a = Rational(doi, ke)
        cot_a = Rational(ke, doi)
        sin_a = Rational(doi, huyen)
        cos_a = Rational(ke, huyen)
        
        c1 = randint(2, 4)
        c2 = randint(2, 4)
        c3 = randint(3, 5)
        tu = c1 * doi + c2 * ke
        mau = c3 * doi - ke
        while mau == 0:
            c3 += 1
            mau = c3 * doi - ke
        gt_a = Rational(tu, mau)

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
        noidungcauhoi = ('''Cho góc nhọn $\\alpha$ biết $\\tan \\alpha = %s$ (xét mô hình tam giác vuông $ABC$ có $\\widehat{B} = \\alpha$ như hình vẽ). %s \\\\
                         a) Tính $\\cot \\alpha$. \\\\
                         b) Không dùng máy tính cầm tay, hãy tính $\\sin \\alpha$ và $\\cos \\alpha$. \\\\
                         c) Tính giá trị của biểu thức $A = \\dfrac{%d\\sin \\alpha + %d\\cos \\alpha}{%d\\sin \\alpha - \\cos \\alpha}$. '''
                         % (latex(tan_a), hinh_ve, c1, c2, c3))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Ta có $\\cot \\alpha = \\dfrac{1}{\\tan \\alpha} = %s$. \n
                        \\item Xét $\\triangle ABC$ vuông tại $A$ có $\\widehat{B} = \\alpha$. Vì $\\tan \\alpha = \\dfrac{AC}{AB} = %s$ nên ta có thể chọn $AC = %d$, $AB = %d$. \\\\
                        Theo định lí Pythagore, ta có: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{%d^2 + %d^2} = %d$. \\\\
                        Do đó: $\\sin \\alpha = \\dfrac{AC}{BC} = %s$ và $\\cos \\alpha = \\dfrac{AB}{BC} = %s$. \n
                        \\item Thay $\\sin \\alpha = %s$ và $\\cos \\alpha = %s$ vào biểu thức $A$, ta được: \\\\
                        $A = \\dfrac{%d \\cdot %s + %d \\cdot %s}{%d \\cdot %s - %s} = \\dfrac{\\frac{%d}{%d}}{\\frac{%d}{%d}} = %s$. \n
                        \\end{enumEX} \n'''
                   % (latex(cot_a), latex(tan_a), doi, ke, ke, doi, huyen, latex(sin_a), latex(cos_a),
                      latex(sin_a), latex(cos_a), c1, latex(sin_a), c2, latex(cos_a), c3, latex(sin_a), latex(cos_a),
                      tu, huyen, mau, huyen, latex(gt_a)))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
