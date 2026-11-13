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

def bt_Dang10_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r = random.choice([4, 6, 8, 10])
        oh = r // 2
        mh_kq = oh * sqrt(3)
        mn_kq = r * sqrt(3)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (M) at (2.16,1.25);\n'
            '\\coordinate (N) at (2.16,-1.25);\n'
            '\\coordinate (H) at (2.16,0);\n'
            '\\draw[line width=1pt] (O) circle (2.5);\n'
            '\\draw[line width=1pt] (O)--(M) (O)--(N) (M)--(N) (O)--(H);\n'
            '\\draw[line width=1pt] (2.16,0.25)--(2.41,0.25)--(2.41,0);\n'
            '\\fill (O) circle (1pt) node[left] {$O$};\n'
            '\\fill (M) circle (1pt) node[above right] {$M$};\n'
            '\\fill (N) circle (1pt) node[below right] {$N$};\n'
            '\\fill (H) circle (1pt) node[below right] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho đường tròn $(O; %d\\text{ cm})$ và dây cung $MN = %s\\text{ cm}$. Kẻ $OH$ vuông góc với $MN$ tại $H$ (như hình vẽ). %s \\\\
                         a) Tính độ dài đoạn thẳng $OH$. \\\\
                         b) Tính số đo góc $\\widehat{MOH}$ và số đo góc ở tâm $\\widehat{MON}$. '''
                         % (r, latex(mn_kq), hinh_ve))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Vì $\\triangle OMN$ cân tại $O$ có đường cao $OH$ nên $H$ là trung điểm của $MN$, suy ra: \\\\
                        $MH = \\dfrac{MN}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$. \\\\
                        Xét $\\triangle OMH$ vuông tại $H$, theo định lí Pythagore ta có: \\\\
                        $OH = \\sqrt{OM^2 - MH^2} = \\sqrt{%d^2 - (%s)^2} = %d\\text{ (cm)}$. \n
                        \\item Trong $\\triangle OMH$ vuông tại $H$, ta có $\\cos \\widehat{MOH} = \\dfrac{OH}{OM} = \\dfrac{%d}{%d} = \\dfrac{1}{2}$. \\\\
                        Theo bảng tỉ số lượng giác của các góc đặc biệt, suy ra $\\widehat{MOH} = 60^{\\circ}$. \\\\
                        Vì $OH$ đồng thời là tia phân giác của $\\widehat{MON}$ nên $\\widehat{MON} = 2\\widehat{MOH} = 2 \\cdot 60^{\\circ} = 120^{\\circ}$. \n
                        \\end{enumEX} \n'''
                   % (latex(mn_kq), latex(mh_kq), r, latex(mh_kq), oh, oh, r))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
