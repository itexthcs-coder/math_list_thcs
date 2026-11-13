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


def bt_Dang16_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        P0 = random.choice([60, 100, 180, 240])
        R0 = 15 if P0 == 60 else (4 if P0 == 100 else (5 if P0 == 180 else 15))
        U0 = int(math.sqrt(P0 * R0))

        ti_so = random.choice([2, 3, 4])
        k_R = random.choice([2, 3])
        k_P = (ti_so**2) * k_R

        U_thietbi = 220
        R_thietbi = random.choice([44, 55, 88])
        P_thietbi = (U_thietbi**2) // R_thietbi

        # Nội dung câu hỏi
        noidungcauhoi = ('''Công suất $P$ ($\text{W}$), hiệu điện thế $U$ ($\text{V}$), điện trở $R$ ($\Omega$) trong đoạn mạch một chiều liên hệ với nhau theo công thức $U = \sqrt{PR}$.\\
                         a) Tính hiệu điện thế $U$ của một bóng đèn có công suất $P = %s\text{ W}$ và điện trở $R = %s\ \Omega$.\\
                         b) Nếu công suất tăng gấp $%s$ lần, điện trở giảm $%s$ lần thì tỉ số giữa hiệu điện thế lúc đó và hiệu điện thế ban đầu bằng bao nhiêu?\\
                         c) Một thiết bị điện hoạt động ở hiệu điện thế $U = %s\text{ V}$ với điện trở $R = %s\ \Omega$. Hãy tính công suất tiêu thụ $P$ của thiết bị đó.'''
                         % (latex(P0), latex(R0), latex(k_P), latex(k_R), latex(U_thietbi), latex(R_thietbi)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Thay $P = %s$ và $R = %s$ vào công thức, ta được:
                      $$U = \sqrt{%s \cdot %s} = \sqrt{%s} = %s\text{ (V)}.$$
                      \item Gọi $P, R, U$ lần lượt là công suất, điện trở và hiệu điện thế ban đầu ($U = \sqrt{PR}$). Khi công suất tăng gấp $%s$ lần và điện trở giảm $%s$ lần thì $P' = %sP$ và $R' = \dfrac{R}{%s}$. Hiệu điện thế lúc đó là:
                      $$U' = \sqrt{P'R'} = \sqrt{%sP \cdot \dfrac{R}{%s}} = \sqrt{%sPR} = \sqrt{%s} \cdot \sqrt{PR} = %sU.$$
                      Vậy tỉ số giữa hiệu điện thế lúc đó và hiệu điện thế ban đầu là $\dfrac{U'}{U} = %s$.
                      \item Từ $U = \sqrt{PR} \Rightarrow U^2 = PR \Rightarrow P = \dfrac{U^2}{R} = \dfrac{%s^2}{%s} = %s\text{ (W)}$.
                      \\end{enumEX}'''
                   % (latex(P0), latex(R0), latex(P0), latex(R0), latex(P0 * R0), latex(U0),
                      latex(k_P), latex(k_R), latex(k_P), latex(k_R), latex(k_P), latex(k_R), latex(ti_so**2), latex(ti_so**2), latex(ti_so), latex(ti_so),
                      latex(U_thietbi), latex(R_thietbi), latex(P_thietbi)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
