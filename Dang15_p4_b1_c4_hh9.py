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

def bt_Dang15_p4_b1_c4_hh9(self):
    def deg_to_dm_str(deg_float):
        total_minutes = int(Decimal(str(deg_float * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        return '%d^{\\circ}%d\'' % (total_minutes // 60, total_minutes % 60)

    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([4, 6, 8, 10])
        ac = randint(5, 12)
        ah = ab // 2
        bh_kq = ah * sqrt(3)
        hc = ah + ac
        bc_sq = 3 * (ah ** 2) + hc ** 2
        bc_kq = sqrt(bc_sq)
        s_kq = Rational(1, 2) * bh_kq * ac
        
        deg_c = math.degrees(math.asin(float(bh_kq) / float(bc_kq)))
        goc_c_str = deg_to_dm_str(deg_c)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (H) at (0,0);\n'
            '\\coordinate (A) at (1.5,0);\n'
            '\\coordinate (C) at (4.5,0);\n'
            '\\coordinate (B) at (0,2.6);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
            '\\draw[line width=1pt, dashed] (B)--(H)--(A);\n'
            '\\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);\n'
            '\\fill (A) circle (1pt) node[below] {$A$};\n'
            '\\fill (B) circle (1pt) node[above left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (H) circle (1pt) node[below left] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = %d\\text{ cm}$, $AC = %d\\text{ cm}$ và góc tù $\\widehat{BAC} = 120^{\\circ}$ (như hình vẽ). %s \\\\
                         a) Kẻ đường cao $BH$ ($H$ thuộc tia đối của tia $AC$). Tính độ dài $AH$, $BH$ và cạnh $BC$. \\\\
                         b) Tính diện tích tam giác $ABC$ và số đo góc $C$ (làm tròn đến phút). '''
                         % (ab, ac, hinh_ve))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Vì $\\widehat{BAH}$ kề bù với $\\widehat{BAC} = 120^{\\circ}$ nên $\\widehat{BAH} = 180^{\\circ} - 120^{\\circ} = 60^{\\circ}$. \\\\
                        Xét $\\triangle ABH$ vuông tại $H$, ta có: \\\\
                        $AH = AB \\cdot \\cos 60^{\\circ} = %d \\cdot \\dfrac{1}{2} = %d\\text{ (cm)}$; $BH = AB \\cdot \\sin 60^{\\circ} = %d \\cdot \\dfrac{\\sqrt{3}}{2} = %s\\text{ (cm)}$. \\\\
                        Ta có $HC = HA + AC = %d + %d = %d\\text{ cm}$. \\\\
                        Xét $\\triangle BHC$ vuông tại $H$, theo định lí Pythagore ta có: \\\\
                        $BC = \\sqrt{BH^2 + HC^2} = \\sqrt{(%s)^2 + %d^2} = \\sqrt{%d} = %s\\text{ (cm)}$. \n
                        \\item Diện tích tam giác $ABC$ là: \\\\
                        $S = \\dfrac{1}{2}BH \\cdot AC = \\dfrac{1}{2} \\cdot %s \\cdot %d = %s\\text{ (cm}^2)$. \\\\
                        Trong $\\triangle BHC$ vuông tại $H$, ta có $\\sin C = \\dfrac{BH}{BC} = \\dfrac{%s}{%s}$. \\\\
                        Sử dụng máy tính cầm tay, làm tròn đến phút ta được $\\widehat{C} \\approx %s$. \n
                        \\end{enumEX} \n'''
                   % (ab, ah, ab, latex(bh_kq), ah, ac, hc, latex(bh_kq), hc, bc_sq, latex(bc_kq),
                      latex(bh_kq), ac, latex(s_kq), latex(bh_kq), latex(bc_kq), goc_c_str))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
