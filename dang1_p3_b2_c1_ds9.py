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


def bt_dang1_p3_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            y0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
            a1 = random.choice([2, 3, 4])
            b1 = random.choice([2, 3, 5])
            a2 = random.choice([2, 3, 4])
            b2 = random.choice([2, 3, 5])
            if math.gcd(b1, b2) == 1 and b1 != b2 and x0 != y0:
                break
    
        c1 = a1 * x0 + b1 * y0
        c2 = a2 * x0 - b2 * y0
        p = random.choice([3, 4, 5])
        q = random.choice([2, 3, 4])
        kq = p * x0 - q * y0
        kq_str = str(kq).replace('.', ',')
    
        pt1_str = latex(a1 * x + b1 * y) + '=' + latex(c1)
        pt2_str = latex(a2 * x - b2 * y) + '=' + latex(c2)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Biết hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$ có nghiệm duy nhất là $(x_0; y_0)$. Tính giá trị của biểu thức $A = %sx_0 - %sy_0$.'''
                         % (pt1_str, pt2_str, latex(p), latex(q)))
    
        # Nội dung lời giải
        pt1_nhan = latex(a1 * b2 * x + b1 * b2 * y) + '=' + latex(c1 * b2)
        pt2_nhan = latex(a2 * b1 * x - b2 * b1 * y) + '=' + latex(c2 * b1)
        hs_x = a1 * b2 + a2 * b1
        vp_x = c1 * b2 + c2 * b1
    
        loigiai = ('''Nhân hai vế của phương trình thứ nhất với $%s$ và nhân hai vế của phương trình thứ hai với $%s$, ta được hệ mới: \\\\
                   $\\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Cộng từng vế hai phương trình của hệ mới, ta được $%sx = %s$, suy ra $x = %s$. \\\\
                   Thế $x = %s$ vào phương trình thứ nhất của hệ đã cho, ta có $%s \\cdot (%s) + %sy = %s$, suy ra $y = %s$. \\\\
                   Vậy nghiệm duy nhất của hệ phương trình là $(x_0; y_0) = (%s; %s)$. \\\\
                   Khi đó $A = %s \\cdot (%s) - %s \\cdot (%s) = %s$.'''
                   % (latex(b2), latex(b1),
                      pt1_nhan, pt2_nhan,
                      latex(hs_x), latex(vp_x), latex(x0),
                      latex(x0), latex(a1), latex(x0), latex(b1), latex(c1), latex(y0),
                      latex(x0), latex(y0),
                      latex(p), latex(x0), latex(q), latex(y0), latex(kq)))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
