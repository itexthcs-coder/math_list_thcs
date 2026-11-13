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

def bt_Dang17_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([6, 8, 10, 12])
        be = 2 * ab
        ce = random.choice([3, 6, 9])
        while ce >= be:
            ce = random.choice([3, 6, 9])
        bc = be - ce
        k_ce = ce // 3
        cd_kq = k_ce * sqrt(3)
        ed_kq = 2 * k_ce * sqrt(3)
        ae_kq = ab * sqrt(3)
        ad_kq = ae_kq - ed_kq

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (3,0);\n'
            '\\coordinate (E) at (0,5.2);\n'
            '\\coordinate (C) at (1.5,2.6);\n'
            '\\coordinate (D) at (0,1.73);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
            '\\draw[line width=1pt, dashed] (D)--(E) (C)--(E);\n'
            '\\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (D) circle (1pt) node[left] {$D$};\n'
            '\\fill (E) circle (1pt) node[above] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tứ giác $ABCD$ có $\\widehat{A} = \\widehat{C} = 90^{\\circ}$, $\\widehat{B} = 60^{\\circ}$, $AB = %d\\text{ cm}$ và $BC = %d\\text{ cm}$. Kéo dài $AD$ và $BC$ cắt nhau tại $E$ (như hình vẽ). %s \\\\
                         a) Tính độ dài các đoạn thẳng $BE$, $CE$ và góc $\\widehat{E}$. \\\\
                         b) Tính độ dài hai cạnh còn lại $CD$ và $AD$ của tứ giác $ABCD$. '''
                         % (ab, bc, hinh_ve))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Xét $\\triangle ABE$ vuông tại $A$ có $\\widehat{B} = 60^{\\circ}$, ta có: \\\\
                        $\\cos B = \\dfrac{AB}{BE} \\Rightarrow BE = \\dfrac{AB}{\\cos 60^{\\circ}} = \\dfrac{%d}{\\frac{1}{2}} = %d\\text{ (cm)}$. \\\\
                        Vì điểm $C$ nằm giữa $B$ và $E$ nên $CE = BE - BC = %d - %d = %d\\text{ (cm)}$. \\\\
                        Trong $\\triangle ABE$ vuông tại $A$, hai góc nhọn $B$ và $E$ phụ nhau nên $\\widehat{E} = 90^{\\circ} - 60^{\\circ} = 30^{\\circ}$. \n
                        \\item Xét $\\triangle ECD$ vuông tại $C$ có $\\widehat{E} = 30^{\\circ}$ và $CE = %d\\text{ cm}$, ta có: \\\\
                        $CD = CE \\cdot \\tan 30^{\\circ} = %d \\cdot \\dfrac{\\sqrt{3}}{3} = %s\\text{ (cm)}$; $ED = \\dfrac{CE}{\\cos 30^{\\circ}} = \\dfrac{%d}{\\frac{\\sqrt{3}}{2}} = %s\\text{ (cm)}$. \\\\
                        Trong $\\triangle ABE$ vuông tại $A$, $AE = AB \\cdot \\tan 60^{\\circ} = %s\\text{ cm}$. \\\\
                        Vì điểm $D$ nằm giữa $A$ và $E$ nên: $AD = AE - ED = %s - %s = %s\\text{ (cm)}$. \n
                        \\end{enumEX} \n'''
                   % (ab, be, be, bc, ce,
                      ce, ce, latex(cd_kq), ce, latex(ed_kq), latex(ae_kq), latex(ae_kq), latex(ed_kq), latex(ad_kq)))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
