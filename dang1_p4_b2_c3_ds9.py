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


def bt_dang1_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k1 = random.choice([2, 3, 5])
        m1 = randint(2, 4)
        n1 = randint(2, 4)
        while m1 == n1:
            n1 = randint(2, 4)
        a1, a2 = k1 * (m1**2), k1 * (n1**2)
        val_a1 = k1 * m1 * n1

        k2 = random.choice([2, 3, 5])
        m2 = randint(3, 6)
        b1, b2 = k2 * (m2**2), k2
        val_a2 = k2 * (m2 - 1)
        kq_a = val_a1 - val_a2

        k3 = random.choice([2, 3])
        u1, u2 = randint(2, 4), randint(1, 3)
        c1, c2 = k3 * (u1**2), k3 * (u2**2)
        val_b1 = k3 * (u1 + u2)

        k4 = random.choice([2, 3])
        v1, v2 = randint(4, 6), randint(1, 3)
        d1, d2 = k4 * (v1**2), k4 * (v2**2)
        val_b2 = k4 * (v1 - v2)
        kq_b = val_b1 - val_b2

        p1, p2, p3 = random.sample([2, 3, 5, 7], 3)
        val_c1 = p1 * p2 * p3
        k5 = random.choice([2, 3, 5])
        w1, w2 = randint(2, 4), randint(2, 5)
        e1, e2 = k5 * (w1**2), k5 * (w2**2)
        val_c2 = k5 * w1 * w2
        kq_c = val_c1 - val_c2

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tính giá trị của các biểu thức sau:\\
                         a) $A = \sqrt{%s} \cdot \sqrt{%s} - \sqrt{%s}(\sqrt{%s} - \sqrt{%s})$.\\
                         b) $B = \sqrt{%s}(\sqrt{%s} + \sqrt{%s}) - \sqrt{%s}(\sqrt{%s} - \sqrt{%s})$.\\
                         c) $C = \sqrt{%s^2 \cdot %s^2 \cdot %s^2} - \sqrt{%s} \cdot \sqrt{%s}$.'''
                         % (latex(a1), latex(a2), latex(k2), latex(b1), latex(b2),
                            latex(k3), latex(c1), latex(c2), latex(k4), latex(d1), latex(d2),
                            latex(p1), latex(p2), latex(p3), latex(e1), latex(e2)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Ta có:
                      $$A = \sqrt{%s \cdot %s} - (\sqrt{%s \cdot %s} - \sqrt{%s \cdot %s}) = \sqrt{%s} - (\sqrt{%s} - \sqrt{%s}) = %s - (%s - %s) = %s.$$
                      \item Ta có:
                      $$B = (\sqrt{%s \cdot %s} + \sqrt{%s \cdot %s}) - (\sqrt{%s \cdot %s} - \sqrt{%s \cdot %s}) = (%s + %s) - (%s - %s) = %s - %s = %s.$$
                      \item Ta có:
                      $$C = \sqrt{%s^2} \cdot \sqrt{%s^2} \cdot \sqrt{%s^2} - \sqrt{%s \cdot %s} = %s \cdot %s \cdot %s - \sqrt{%s} = %s - %s = %s.$$
                      \\end{enumEX}'''
                   % (latex(a1), latex(a2), latex(k2), latex(b1), latex(k2), latex(b2),
                      latex(a1 * a2), latex(k2 * b1), latex(k2 * b2),
                      latex(val_a1), latex(k2 * m2), latex(k2), latex(kq_a),
                      latex(k3), latex(c1), latex(k3), latex(c2), latex(k4), latex(d1), latex(k4), latex(d2),
                      latex(k3 * u1), latex(k3 * u2), latex(k4 * v1), latex(k4 * v2),
                      latex(val_b1), latex(val_b2), latex(kq_b),
                      latex(p1), latex(p2), latex(p3), latex(e1), latex(e2),
                      latex(p1), latex(p2), latex(p3), latex(e1 * e2),
                      latex(val_c1), latex(val_c2), latex(kq_c)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
