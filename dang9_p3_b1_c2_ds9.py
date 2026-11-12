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


def bt_dang9_p3_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        a = random.choice([1, 2, 3, 4])
        # (x - a)/(x - a - 1) + (x - a - 6)/(x - a - 7) = (x - a - 2)/(x - a - 3) + (x - a - 4)/(x - a - 5)
        # Tách 1 ở mỗi phân thức => 1/(x - a - 1) + 1/(x - a - 7) = 1/(x - a - 3) + 1/(x - a - 5)
        # Tổng hai mẫu mỗi vế đều là 2x - 2a - 8 => x0 = a + 4
        m1, m2, m3, m4 = a + 1, a + 7, a + 3, a + 5
        x0 = a + 4
        kq_str = str(x0)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Tìm nghiệm duy nhất của phương trình $\\dfrac{%s}{%s} + \\dfrac{%s}{%s} = \\dfrac{%s}{%s} + \\dfrac{%s}{%s}$.'''
                         %(latex(x - a), latex(x - m1), latex(x - a - 6), latex(x - m2),
                           latex(x - a - 2), latex(x - m3), latex(x - a - 4), latex(x - m4)))
    
        # Nội dung lời giải
        loigiai = ('''Điều kiện xác định: $x \\notin \\left\\{%s; %s; %s; %s\\right\\}$. \\\\
                   Trừ mỗi phân thức ở cả hai vế đi $1$, phương trình trở thành: \\\\
                   $\\left(\\dfrac{%s}{%s} - 1\\right) + \\left(\\dfrac{%s}{%s} - 1\\right) = \\left(\\dfrac{%s}{%s} - 1\\right) + \\left(\\dfrac{%s}{%s} - 1\\right)$ \\\\
                   $\\dfrac{1}{%s} + \\dfrac{1}{%s} = \\dfrac{1}{%s} + \\dfrac{1}{%s}$ \\\\
                   $\\dfrac{%s}{(%s)(%s)} = \\dfrac{%s}{(%s)(%s)}$ \\\\
                   $(%s)\\left[\\dfrac{1}{(%s)(%s)} - \\dfrac{1}{(%s)(%s)}\\right] = 0$. \\\\
                   Vì hai mẫu thức $(%s)(%s)$ và $(%s)(%s)$ luôn khác nhau với mọi $x$ thoả mãn ĐKXĐ nên $%s = 0$, suy ra $x = %s$ (thoả mãn). \\\\
                   Vậy nghiệm của phương trình là $x = %s$.'''
                   %(latex(m1), latex(m3), latex(m4), latex(m2),
                     latex(x - a), latex(x - m1), latex(x - a - 6), latex(x - m2),
                     latex(x - a - 2), latex(x - m3), latex(x - a - 4), latex(x - m4),
                     latex(x - m1), latex(x - m2), latex(x - m3), latex(x - m4),
                     latex(2*x - 2*x0), latex(x - m1), latex(x - m2), latex(2*x - 2*x0), latex(x - m3), latex(x - m4),
                     latex(2*x - 2*x0), latex(x - m1), latex(x - m2), latex(x - m3), latex(x - m4),
                     latex(x - m1), latex(x - m2), latex(x - m3), latex(x - m4),
                     latex(2*x - 2*x0), kq_str,
                     kq_str))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
