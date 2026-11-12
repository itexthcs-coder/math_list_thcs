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


def bt_dang20_p4_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 2)).replace('.', '{,}')
    
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        valid_cases = [
            (4, 4, 6, 2.5, 44, 14),
            (5, 4, 5, 2.5, 45, 15),
            (3, 4, 7, 2.5, 43, 13),
            (4, 5, 6, 2.5, 34, 10)
        ]
        t_truoc, k_truoc, t_sau, k_sau, x0, y0 = random.choice(valid_cases)
        vp1 = t_truoc - k_truoc * t_truoc
        vp2 = int(k_sau * t_sau - t_sau)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cách đây $%s\\text{ năm}$, tuổi của mẹ gấp $%s$ lần tuổi của con. Sau $%s\\text{ năm}$ nữa (tính từ hiện nay), tuổi của mẹ chỉ còn gấp $%s$ lần tuổi của con. Tính tuổi của mẹ và tuổi của con hiện nay.'''
                         % (t_truoc, k_truoc, t_sau, fmt_dec(k_sau)))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{itemize}
                        \\item Gọi tuổi của mẹ hiện nay là $x$ (tuổi) và tuổi của con hiện nay là $y$ (tuổi). Điều kiện: $x > y > %s$.\\\\
                        Cách đây $%s\\text{ năm}$, tuổi của mẹ là $x - %s$ và tuổi của con là $y - %s$. Vì lúc đó tuổi mẹ gấp $%s$ lần tuổi con nên ta có phương trình:
                        $$x - %s = %s(y - %s) \\Leftrightarrow x - %sy = %s. \\quad (1)$$
                        Sau $%s\\text{ năm}$ nữa, tuổi của mẹ là $x + %s$ và tuổi của con là $y + %s$. Vì lúc đó tuổi mẹ gấp $%s$ lần tuổi con nên ta có phương trình:
                        $$x + %s = %s(y + %s) \\Leftrightarrow x - %sy = %s. \\quad (2)$$
                        Từ $(1)$ và $(2)$, ta có hệ phương trình:
                        $$\\begin{cases} x - %sy = %s \\\\ x - %sy = %s. \\end{cases}$$
                        \\item Trừ từng vế $(2)$ cho $(1)$, ta được:
                        $$%sy = %s \\Leftrightarrow y = %s.$$
                        Thay $y = %s$ vào $(1)$, ta được $x = %s + %s \\cdot %s = %s$.
                        \\item Các giá trị $x = %s$ và $y = %s$ thỏa mãn điều kiện của ẩn.\\\\
                        Vậy hiện nay mẹ $%s\\text{ tuổi}$ và con $%s\\text{ tuổi}$.
                    \\end{itemize}'''
                   % (t_truoc,
                      t_truoc, t_truoc, t_truoc, k_truoc,
                      t_truoc, k_truoc, t_truoc, k_truoc, vp1,
                      t_sau, t_sau, t_sau, fmt_dec(k_sau),
                      t_sau, fmt_dec(k_sau), t_sau, fmt_dec(k_sau), vp2,
                      k_truoc, vp1, fmt_dec(k_sau), vp2,
                      fmt_dec(k_truoc - k_sau), vp2 - vp1, y0,
                      y0, vp1, k_truoc, y0, x0,
                      x0, y0, x0, y0))
    
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')
    

    return content
