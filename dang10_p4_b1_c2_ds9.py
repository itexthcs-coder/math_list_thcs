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


def bt_dang10_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        while True:
            a = random.choice([1, 2, 3])
            b = random.choice([2, 3, 4])
            c = random.choice([2, 3, 4])
            if a != b and b != c and a != c:
                # ((x - a)(x - b))/(x - b) = ((a + c)*x - a*c)/(x + c)
                # Rút gọn vế trái: x - a = ((a + c)*x - a*c)/(x + c)
                # Khử mẫu: (x - a)(x + c) = (a + c)x - a*c <=> x^2 + (c - a)x - a*c = (a + c)x - a*c
                # <=> x^2 - 2ax = 0 <=> x(x - 2a) = 0 => x = 0 hoặc x = 2a
                if 2*a != b and 2*a != -c:
                    break
    
        tu_trai = expand((x - a)*(x - b))
        mau_trai = x - b
        tu_phai = (a + c)*x - a*c
        mau_phai = x + c
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giải phương trình: $\\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.'''
                         %(latex(tu_trai), latex(mau_trai), latex(tu_phai), latex(mau_phai)))
    
        # Nội dung lời giải
        loigiai = ('''Điều kiện xác định: $x \\neq %s$ và $x \\neq %s$. \\\\
                   Phân tích tử thức ở vế trái thành nhân tử, ta có: \\\\
                   $\\dfrac{(%s)(%s)}{%s} = \\dfrac{%s}{%s}$. \\\\
                   Với điều kiện $x \\neq %s$, rút gọn phân thức ở vế trái, phương trình trở thành: \\\\
                   $%s = \\dfrac{%s}{%s}$. \\\\
                   Quy đồng mẫu hai vế với mẫu thức chung $%s$ rồi khử mẫu, ta được: \\\\
                   $(%s)(%s) = %s$ \\\\
                   $%s = %s$ \\\\
                   $x^2 - %sx = 0$ \\\\
                   $x(x - %s) = 0$. \\\\
                   Suy ra $x = 0$ hoặc $x = %s$ (cả hai giá trị đều thoả mãn ĐKXĐ). \\\\
                   Vậy tập nghiệm của phương trình đã cho là $S = \\left\\{0; %s\\right\\}$.'''
                   %(latex(b), latex(-c),
                     latex(x - a), latex(x - b), latex(mau_trai), latex(tu_phai), latex(mau_phai),
                     latex(b),
                     latex(x - a), latex(tu_phai), latex(mau_phai),
                     latex(mau_phai),
                     latex(x - a), latex(mau_phai), latex(tu_phai),
                     latex(expand((x - a)*mau_phai)), latex(tu_phai),
                     latex(2*a),
                     latex(2*a),
                     latex(2*a),
                     latex(2*a)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
