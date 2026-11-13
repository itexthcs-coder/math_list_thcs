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


def bt_Dang14_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = randint(1, 3)
        a2 = randint(4, 7)

        b1 = randint(1, 4)
        b2 = randint(2, 6)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tìm điều kiện của $x$ để các biểu thức sau xác định:\\
                         a) $A = \sqrt{(x - %s)(x - %s)}$.\\
                         b) $B = \sqrt{\dfrac{x + %s}{x - %s}}$.\\
                         c) So sánh điều kiện xác định của $B = \sqrt{\dfrac{x + %s}{x - %s}}$ và $C = \dfrac{\sqrt{x + %s}}{\sqrt{x - %s}}$.'''
                         % (latex(a1), latex(a2),
                            latex(b1), latex(b2),
                            latex(b1), latex(b2), latex(b1), latex(b2)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Biểu thức $A$ xác định khi $(x - %s)(x - %s) \ge 0$.
                      \begin{itemize}
                      \item Trường hợp 1: $x - %s \ge 0$ và $x - %s \ge 0 \Leftrightarrow x \ge %s$.
                      \item Trường hợp 2: $x - %s \le 0$ và $x - %s \le 0 \Leftrightarrow x \le %s$.
                      \end{itemize}
                      Vậy $x \ge %s$ hoặc $x \le %s$.
                      \item Biểu thức $B$ xác định khi $\dfrac{x + %s}{x - %s} \ge 0$ và $x - %s \ne 0$.
                      \begin{itemize}
                      \item Trường hợp 1: $x + %s \ge 0$ và $x - %s > 0 \Leftrightarrow x > %s$.
                      \item Trường hợp 2: $x + %s \le 0$ và $x - %s < 0 \Leftrightarrow x \le -%s$.
                      \end{itemize}
                      Vậy $x > %s$ hoặc $x \le -%s$.
                      \item Biểu thức $C = \dfrac{\sqrt{x + %s}}{\sqrt{x - %s}}$ xác định khi $x + %s \ge 0$ và $x - %s > 0 \Leftrightarrow x > %s$. Như vậy, điều kiện xác định của $C$ chặt hơn của $B$ (không nhận giá trị $x \le -%s$).
                      \\end{enumEX}'''
                   % (latex(a1), latex(a2), latex(a1), latex(a2), latex(a2), latex(a1), latex(a2), latex(a1), latex(a2), latex(a1),
                      latex(b1), latex(b2), latex(b2), latex(b1), latex(b2), latex(b2), latex(b1), latex(b2), latex(b1), latex(b2), latex(b1),
                      latex(b1), latex(b2), latex(b1), latex(b2), latex(b2), latex(b1)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
