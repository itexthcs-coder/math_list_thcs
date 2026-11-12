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


def bt_dang1_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            a1 = random.choice([2, 3, 4])
            b1 = random.choice([2, 3])
            m1 = random.choice([1, 2])
            n1 = random.choice([1, 2])
            a2 = random.choice([2, 3])
            m2 = random.choice([1, 2])
            x0 = random.choice([-2, -1, 1, 2, 3])
            y0 = random.choice([-2, -1, 1, 2, 3])
            if a1 + 2 * b1 != 0 and x0 != y0:
                break
    
        # Hệ: a1(x + m1) - b1(y - n1) = d1 và a2(x - m2) + y = d2
        c1 = a1 * x0 - b1 * y0
        d1 = c1 + a1 * m1 + b1 * n1
        c2 = a2 * x0 + y0
        d2 = c2 - a2 * m2
    
        pt1_goc = '%s(x + %s) - %s(y - %s) = %s' % (latex(a1), latex(m1), latex(b1), latex(n1), latex(d1))
        pt2_goc = '%s(x - %s) + y = %s' % (latex(a2), latex(m2), latex(d2))
    
        pt1_rg = latex(a1 * x - b1 * y) + '=' + latex(c1)
        pt2_rg = latex(a2 * x + y) + '=' + latex(c2)
        y_the = -a2 * x + c2
        vt_the = a1 * x - b1 * y_the
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giải hệ phương trình sau bằng phương pháp thế: \\\\
                         $\\begin{cases} %s \\\\ %s \\end{cases}$'''
                         % (pt1_goc, pt2_goc))
    
        # Nội dung lời giải
        loigiai = ('''Thu gọn từng phương trình của hệ, ta được: \\\\
                   $\\begin{cases} %sx + %s - %sy + %s = %s \\\\ %sx - %s + y = %s \\end{cases} \\Leftrightarrow \\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Từ phương trình thứ hai của hệ thu gọn, biểu diễn $y$ theo $x$ ta được $y = %s$. \\\\
                   Thế $y = %s$ vào phương trình thứ nhất, ta được: \\\\
                   $%sx - %s(%s) = %s \\Leftrightarrow %s = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$. \\\\
                   Thay $x = %s$ vào biểu thức $y = %s$, ta được $y = -%s \\cdot (%s) + (%s) = %s$. \\\\
                   Vậy hệ phương trình đã cho có nghiệm duy nhất là $(%s; %s)$.'''
                   % (latex(a1), latex(a1 * m1), latex(b1), latex(b1 * n1), latex(d1),
                      latex(a2), latex(a2 * m2), latex(d2),
                      pt1_rg, pt2_rg,
                      latex(y_the), latex(y_the),
                      latex(a1), latex(b1), latex(y_the), latex(c1),
                      latex(vt_the), latex(c1),
                      latex(a1 + a2 * b1), latex(c1 + b1 * c2), latex(x0),
                      latex(x0), latex(y_the), latex(a2), latex(x0), latex(c2), latex(y0),
                      latex(x0), latex(y0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
