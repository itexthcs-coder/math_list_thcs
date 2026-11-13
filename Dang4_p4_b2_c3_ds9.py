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


def bt_Dang4_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k1 = random.choice([3, 5, 7, 11])
        m1 = randint(2, 5)
        tu1 = k1 * (m1**2)
        p1 = randint(2, 6)

        k2 = random.choice([2, 3, 5])
        m2 = randint(2, 5)
        tu2 = k2 * (m2**2)
        p2 = randint(2, 6)

        k3 = random.choice([2, 3, 5, 7])
        c3 = randint(1, 4)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Rút gọn các biểu thức sau:\\
                         a) $D = \sqrt{%sa^3} : \sqrt{%sa} + %sa$ với $a > 0$.\\
                         b) $E = \sqrt{%sab^2} : \sqrt{%sa} - %sb$ với $a > 0$ và $b < 0$.\\
                         c) $F = a \cdot \sqrt{\dfrac{%s}{a^2}} + (a^2 - %s) \cdot \sqrt{\dfrac{%s}{(a - %s)^2}}$ với $a > %s$.'''
                         % (latex(tu1), latex(k1), latex(p1),
                            latex(tu2), latex(k2), latex(p2),
                            latex(k3), latex(c3**2), latex(k3), latex(c3), latex(c3)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Với $a > 0$, ta có:
                      $$D = \sqrt{%sa^3 : (%sa)} + %sa = \sqrt{%sa^2} + %sa = |%sa| + %sa = %sa + %sa = %sa.$$
                      \item Với $a > 0$ và $b < 0$, ta có $|b| = -b$, suy ra:
                      $$E = \sqrt{%sab^2 : (%sa)} - %sb = \sqrt{%sb^2} - %sb = %s|b| - %sb = -%sb - %sb = %sb.$$
                      \item Với $a > %s$, ta có $a > 0$ và $a - %s > 0$. Do đó:
                      $$F = a \cdot \dfrac{\sqrt{%s}}{|a|} + (a - %s)(a + %s) \cdot \dfrac{\sqrt{%s}}{|a - %s|} = \sqrt{%s} + (a + %s)\sqrt{%s} = (a + %s)\sqrt{%s}.$$
                      \\end{enumEX}'''
                   % (latex(tu1), latex(k1), latex(p1), latex(m1**2), latex(p1), latex(m1), latex(p1), latex(m1), latex(p1), latex(m1 + p1),
                      latex(tu2), latex(k2), latex(p2), latex(m2**2), latex(p2), latex(m2), latex(p2), latex(m2), latex(p2), latex(-m2 - p2),
                      latex(c3), latex(c3), latex(k3), latex(c3), latex(c3), latex(k3), latex(c3), latex(k3), latex(c3), latex(k3), latex(c3 + 1), latex(k3)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
