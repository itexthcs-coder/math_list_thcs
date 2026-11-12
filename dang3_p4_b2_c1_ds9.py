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


def bt_dang3_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            x0 = random.choice([-3, -2, 2, 3, 4])
            y0 = random.choice([-3, -2, 2, 3, 4])
            m1 = random.choice([2, 3])
            m2 = random.choice([3, 4, 5])
            n1 = random.choice([2, 3, 4])
            n2 = random.choice([3, 4, 5])
            if m1 != m2 and n1 != n2 and x0 != y0:
                # Phương trình 1: (x + y)/m1 - (x - y)/m2 = c1 => m2*(x+y) - m1*(x-y) = m1*m2*c1
                # Phương trình 2: x/n1 + y/n2 = c2 => n2*x + n1*y = n1*n2*c2
                a1_rg = m2 - m1
                b1_rg = m2 + m1
                if a1_rg * n1 - b1_rg * n2 != 0:
                    c1 = Rational(x0 + y0, m1) - Rational(x0 - y0, m2)
                    c2 = Rational(x0, n1) + Rational(y0, n2)
                    if c1.q == 1 and c2.q == 1:
                        break
    
        bcnn1 = m1 * m2
        bcnn2 = n1 * n2
        vp1_ng = int(c1) * bcnn1
        vp2_ng = int(c2) * bcnn2
    
        pt1_rg = latex(a1_rg * x + b1_rg * y) + '=' + latex(vp1_ng)
        pt2_rg = latex(n2 * x + n1 * y) + '=' + latex(vp2_ng)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giải hệ phương trình sau: \\\\
                         $\\begin{cases} \\frac{x + y}{%s} - \\frac{x - y}{%s} = %s \\\\ \\frac{x}{%s} + \\frac{y}{%s} = %s \\end{cases}$'''
                         % (latex(m1), latex(m2), latex(int(c1)), latex(n1), latex(n2), latex(int(c2))))
    
        # Nội dung lời giải
        loigiai = ('''Quy đồng mẫu số và khử mẫu hai phương trình (nhân hai vế của phương trình thứ nhất với $%s$, nhân hai vế của phương trình thứ hai với $%s$), ta được: \\\\
                   $\\begin{cases} %s(x + y) - %s(x - y) = %s \\\\ %sx + %sy = %s \\end{cases} \\Leftrightarrow \\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Giải hệ phương trình trên bằng phương pháp cộng đại số, ta tìm được $x = %s$ và $y = %s$. \\\\
                   Vậy hệ phương trình đã cho có nghiệm duy nhất là $(%s; %s)$.'''
                   % (latex(bcnn1), latex(bcnn2),
                      latex(m2), latex(m1), latex(vp1_ng),
                      latex(n2), latex(n1), latex(vp2_ng),
                      pt1_rg, pt2_rg,
                      latex(x0), latex(y0), latex(x0), latex(y0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
