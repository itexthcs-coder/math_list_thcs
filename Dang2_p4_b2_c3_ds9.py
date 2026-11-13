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


def bt_Dang2_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k1 = random.choice([3, 5, 7, 11])
        m1 = randint(2, 5)
        k2 = random.choice([2, 3, 5, 15])
        m2 = randint(6, 12)
        tu1, mau1 = k1 * (m1**2), k1
        tu2, mau2 = k2 * (m2**2), k2
        kq_a = m1 + m2

        c1, c2, c3 = random.sample([12, 13, 14, 15, 16, 18, 25, 28], 3)
        stp1, stp2, stp3 = c1**2 / 100, c2**2 / 100, c3**2 / 100
        s_stp1 = str(stp1).replace('.', ',')
        s_stp2 = str(stp2).replace('.', ',')
        s_stp3 = str(stp3).replace('.', ',')
        val_b = Rational(c1 + c2 - c3, 10)

        k = random.choice([2, 3, 5])
        a1, a2, a3 = randint(2, 5), randint(3, 6), randint(1, 4)
        mau_c = random.choice([3, 5, 7])
        tu_c = -3 * a1 + 5 * a2 - 4 * a3
        kq_c = Rational(tu_c, mau_c)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Không dùng máy tính cầm tay, tính giá trị của các biểu thức sau:\\
                         a) $M = \sqrt{%s} : \sqrt{%s} + \sqrt{%s} : \sqrt{%s}$.\\
                         b) $N = \sqrt{%s} + \sqrt{%s} - \sqrt{%s}$.\\
                         c) $P = \dfrac{-%s\sqrt{%s} + %s\sqrt{%s} - %s\sqrt{%s}}{%s\sqrt{%s}}$.'''
                         % (latex(tu1), latex(mau1), latex(tu2), latex(mau2),
                            s_stp1, s_stp2, s_stp3,
                            latex(a1), latex(9*k), latex(a2), latex(25*k), latex(a3), latex(16*k), latex(mau_c), latex(k)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Ta có:
                      $$M = \sqrt{%s : %s} + \sqrt{%s : %s} = \sqrt{%s} + \sqrt{%s} = %s + %s = %s.$$
                      \item Đưa các số thập phân về phân số thập phân, ta được:
                      $$N = \sqrt{\dfrac{%s}{100}} + \sqrt{\dfrac{%s}{100}} - \sqrt{\dfrac{%s}{100}} = \dfrac{%s}{10} + \dfrac{%s}{10} - \dfrac{%s}{10} = %s.$$
                      \item Ta có:
                      $$P = \dfrac{-%s \cdot 3\sqrt{%s} + %s \cdot 5\sqrt{%s} - %s \cdot 4\sqrt{%s}}{%s\sqrt{%s}} = \dfrac{(%s)\sqrt{%s}}{%s\sqrt{%s}} = %s.$$
                      \\end{enumEX}'''
                   % (latex(tu1), latex(mau1), latex(tu2), latex(mau2), latex(m1**2), latex(m2**2), latex(m1), latex(m2), latex(kq_a),
                      latex(c1**2), latex(c2**2), latex(c3**2), latex(c1), latex(c2), latex(c3), latex(val_b),
                      latex(a1), latex(k), latex(a2), latex(k), latex(a3), latex(k), latex(mau_c), latex(k),
                      latex(tu_c), latex(k), latex(mau_c), latex(k), latex(kq_c)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
