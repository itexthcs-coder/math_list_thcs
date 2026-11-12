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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang2_p4_b2_c1_ds9(self):
    # Khai báo biến
    def fmt_tp(val):
        return str(val).replace('.', ',')
    
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            x0 = random.choice([-3, -2, -1, 1, 2, 3, 4])
            y0 = random.choice([-3, -2, -1, 1, 2, 3, 4])
            a1 = random.choice([3, 4, 5, 6])
            b1 = random.choice([4, 5, 6, 7])
            a2 = random.choice([2, 4, 5, 8])
            b2 = random.choice([3, 5, 7, 9])
            if a1 * b2 + a2 * b1 != 0 and a1 != a2 and b1 != b2 and x0 != y0:
                break
    
        c1 = a1 * x0 + b1 * y0
        c2 = a2 * x0 - b2 * y0
    
        pt1_tp = '%sx + %sy = %s' % (fmt_tp(a1 / 10), fmt_tp(b1 / 10), fmt_tp(c1 / 10))
        pt2_tp = '%sx - %sy = %s' % (fmt_tp(a2 / 10), fmt_tp(b2 / 10), fmt_tp(c2 / 10))
        pt1_ng = latex(a1 * x + b1 * y) + '=' + latex(c1)
        pt2_ng = latex(a2 * x - b2 * y) + '=' + latex(c2)
    
        pt1_nhan = latex(a1 * b2 * x + b1 * b2 * y) + '=' + latex(c1 * b2)
        pt2_nhan = latex(a2 * b1 * x - b2 * b1 * y) + '=' + latex(c2 * b1)
        hs_x = a1 * b2 + a2 * b1
        vp_x = c1 * b2 + c2 * b1
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giải hệ phương trình sau bằng phương pháp cộng đại số: \\\\
                         $\\begin{cases} %s \\\\ %s \\end{cases}$'''
                         % (pt1_tp, pt2_tp))
    
        # Nội dung lời giải
        loigiai = ('''Nhân hai vế của mỗi phương trình với $10$ để khử hệ số thập phân, ta được: \\\\
                   $\\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Nhân hai vế của phương trình thứ nhất với $%s$ và nhân hai vế của phương trình thứ hai với $%s$, ta được hệ mới: \\\\
                   $\\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Cộng từng vế hai phương trình của hệ mới, ta được $%sx = %s$, suy ra $x = %s$. \\\\
                   Thế $x = %s$ vào phương trình $%s$, ta được $%s \\cdot (%s) + %sy = %s$, suy ra $y = %s$. \\\\
                   Vậy hệ phương trình đã cho có nghiệm duy nhất là $(%s; %s)$.'''
                   % (pt1_ng, pt2_ng,
                      latex(b2), latex(b1),
                      pt1_nhan, pt2_nhan,
                      latex(hs_x), latex(vp_x), latex(x0),
                      latex(x0), pt1_ng, latex(a1), latex(x0), latex(b1), latex(c1), latex(y0),
                      latex(x0), latex(y0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
