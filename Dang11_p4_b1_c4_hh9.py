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

def bt_Dang11_p4_b1_c4_hh9(self):
    def deg_to_dm_str(deg_float):
        total_minutes = int(Decimal(str(deg_float * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        return '%d^{\\circ}%d\'' % (total_minutes // 60, total_minutes % 60)

    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bh = randint(2, 6)
        ab = 2 * bh
        ah_kq = bh * sqrt(3)
        bc = 4 * bh
        ac_kq = ab * sqrt(3)
        am_kq = bh * sqrt(3)
        tan_abm = Rational(1, 2) * sqrt(3)
        deg_abm = math.degrees(math.atan(math.sqrt(3) / 2.0))
        goc_abm_str = deg_to_dm_str(deg_abm)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (H) at (1.5,0);\n'
            '\\coordinate (C) at (5,0);\n'
            '\\coordinate (A) at (1.5,2.4);\n'
            '\\coordinate (M) at (3.25,1.2);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
            '\\draw[line width=1pt] (A)--(H) (B)--(M);\n'
            '\\draw[line width=1pt] (1.5,0.25)--(1.75,0.25)--(1.75,0);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\fill (M) circle (1pt) node[above right] {$M$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có đường cao $AH$ ($H \\in BC$). Biết $\\widehat{B} = 60^{\\circ}$ và $BH = %d\\text{ cm}$ (như hình vẽ). %s \\\\
                         a) Tính độ dài cạnh $AB$, đường cao $AH$ và cạnh huyền $BC$. \\\\
                         b) Gọi $M$ là trung điểm của $AC$. Tính $\\tan \\widehat{ABM}$ và số đo góc $\\widehat{ABM}$ (làm tròn đến phút). '''
                         % (bh, hinh_ve))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Xét $\\triangle AHB$ vuông tại $H$, ta có: \\\\
                        $\\cos B = \\dfrac{BH}{AB} \\Rightarrow AB = \\dfrac{BH}{\\cos 60^{\\circ}} = \\dfrac{%d}{\\frac{1}{2}} = %d\\text{ (cm)}$. \\\\
                        $AH = AB \\cdot \\sin 60^{\\circ} = %d \\cdot \\dfrac{\\sqrt{3}}{2} = %s\\text{ (cm)}$. \\\\
                        Xét $\\triangle ABC$ vuông tại $A$, ta có: \\\\
                        $\\cos B = \\dfrac{AB}{BC} \\Rightarrow BC = \\dfrac{AB}{\\cos 60^{\\circ}} = \\dfrac{%d}{\\frac{1}{2}} = %d\\text{ (cm)}$. \n
                        \\item Trong $\\triangle ABC$ vuông tại $A$, $AC = AB \\cdot \\tan 60^{\\circ} = %s\\text{ cm}$. \\\\
                        Vì $M$ là trung điểm của $AC$ nên $AM = \\dfrac{AC}{2} = %s\\text{ cm}$. \\\\
                        Xét $\\triangle ABM$ vuông tại $A$, ta có: $\\tan \\widehat{ABM} = \\dfrac{AM}{AB} = \\dfrac{%s}{%d} = %s$. \\\\
                        Sử dụng máy tính cầm tay, làm tròn đến phút ta được $\\widehat{ABM} \\approx %s$. \n
                        \\end{enumEX} \n'''
                   % (bh, ab, ab, latex(ah_kq), ab, bc,
                      latex(ac_kq), latex(am_kq), latex(am_kq), ab, latex(tan_abm), goc_abm_str))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
