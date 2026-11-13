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

def bt_Dang16_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2, 3])
        ac = 12 * k
        ab = 16 * k
        bc = 20 * k
        da_kq = Rational(16 * k, 3)
        dc_kq = Rational(20 * k, 3)
        bd_kq = Rational(16 * k, 3) * sqrt(10)
        sin_bdc_val = 3.0 / math.sqrt(10)
        sin_bdc_str = str(Decimal(str(sin_bdc_val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (4,0);\n'
            '\\coordinate (C) at (0,3);\n'
            '\\coordinate (D) at (0,1.33);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
            '\\draw[line width=1pt] (B)--(D);\n'
            '\\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[left] {$D$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có cạnh $AC = %d\\text{ cm}$ và $\\tan B = \\dfrac{3}{4}$. Kẻ đường phân giác trong $BD$ ($D \\in AC$) như hình vẽ. %s \\\\
                         a) Tính độ dài các cạnh $AB$ và $BC$. \\\\
                         b) Tính độ dài các đoạn thẳng $DA$, $DC$ và tính $\\tan \\widehat{ABD}$, $\\sin \\widehat{BDC}$ (làm tròn $\\sin \\widehat{BDC}$ đến chữ số thập phân thứ ba). '''
                         % (ac, hinh_ve))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Xét $\\triangle ABC$ vuông tại $A$, ta có: \\\\
                        $\\tan B = \\dfrac{AC}{AB} = \\dfrac{3}{4} \\Rightarrow AB = \\dfrac{4 \\cdot AC}{3} = \\dfrac{4 \\cdot %d}{3} = %d\\text{ (cm)}$. \\\\
                        Theo định lí Pythagore, ta có: $BC = \\sqrt{AB^2 + AC^2} = \\sqrt{%d^2 + %d^2} = %d\\text{ (cm)}$. \n
                        \\item Vì $BD$ là đường phân giác của $\\triangle ABC$ nên theo tính chất đường phân giác, ta có: \\\\
                        $\\dfrac{DA}{DC} = \\dfrac{AB}{BC} = \\dfrac{%d}{%d} = \\dfrac{4}{5} \\Rightarrow \\dfrac{DA}{4} = \\dfrac{DC}{5} = \\dfrac{DA + DC}{4 + 5} = \\dfrac{%d}{9} = %s$. \\\\
                        Suy ra $DA = %s\\text{ cm}$ và $DC = %s\\text{ cm}$. \\\\
                        Xét $\\triangle ABD$ vuông tại $A$: $\\tan \\widehat{ABD} = \\dfrac{AD}{AB} = \\dfrac{%s}{%d} = \\dfrac{1}{3}$. \\\\
                        Theo định lí Pythagore trong $\\triangle ABD$, $BD = \\sqrt{AB^2 + AD^2} = \\sqrt{%d^2 + \\left(%s\\right)^2} = %s\\text{ cm}$. \\\\
                        Vì $\\widehat{BDC}$ và $\\widehat{BDA}$ kề bù nên $\\sin \\widehat{BDC} = \\sin \\widehat{BDA} = \\dfrac{AB}{BD} = \\dfrac{%d}{%s} = \\dfrac{3}{\\sqrt{10}} \\approx %s$. \n
                        \\end{enumEX} \n'''
                   % (ac, ab, ab, ac, bc,
                      ab, bc, ac, latex(Rational(ac, 9)), latex(da_kq), latex(dc_kq),
                      latex(da_kq), ab, ab, latex(da_kq), latex(bd_kq), ab, latex(bd_kq), sin_bdc_str))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
