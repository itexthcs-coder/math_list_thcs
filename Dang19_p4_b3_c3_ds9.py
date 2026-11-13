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


def bt_Dang19_p4_b3_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m1 = random.choice([1, 2, 3])
        m2 = random.choice([2, 3, 4])
        m3 = random.choice([3, 4, 5])
        a = random.choice([1, 2])
        b = random.choice([2, 3])
        c = random.choice([3, 4])
        hang_so = (a**2 + b**2 + c**2) - (m1 + m2 + m3)
        x_ng = m1 + a**2
        y_ng = m2 + b**2
        z_ng = m3 + c**2

        # Nội dung câu hỏi
        noidungcauhoi = ("""Giải phương trình:
                         $$x + y + z + %d = %d\\sqrt{x - %d} + %d\\sqrt{y - %d} + %d\\sqrt{z - %d}.$$"""
                         % (hang_so, 2*a, m1, 2*b, m2, 2*c, m3))

        # Nội dung lời giải
        loigiai = ("""Điều kiện xác định: $x \\ge %d$, $y \\ge %d$, $z \\ge %d$.\\\\
                    Chuyển vế và nhóm các hạng tử thành tổng các bình phương, phương trình đã cho trở thành:
                    \\begin{align*}
                    [(x - %d) - %d\\sqrt{x - %d} + %d] + [(y - %d) - %d\\sqrt{y - %d} + %d] + [(z - %d) - %d\\sqrt{z - %d} + %d] &= 0 \\\\
                    (\\sqrt{x - %d} - %d)^2 + (\\sqrt{y - %d} - %d)^2 + (\\sqrt{z - %d} - %d)^2 &= 0.
                    \\end{align*}
                    Vì bình phương của một biểu thức luôn không âm nên phương trình tương đương với:
                    $$\\begin{cases} \\sqrt{x - %d} - %d = 0 \\\\ \\sqrt{y - %d} - %d = 0 \\\\ \\sqrt{z - %d} - %d = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x - %d = %d \\\\ y - %d = %d \\\\ z - %d = %d \\end{cases} \\Leftrightarrow \\begin{cases} x = %d \\\\ y = %d \\\\ z = %d \\end{cases} \\text{ (thỏa mãn điều kiện).}$$
                    Vậy nghiệm của phương trình là $(x; y; z) = (%d; %d; %d)$."""
                   % (m1, m2, m3,
                      m1, 2*a, m1, a**2, m2, 2*b, m2, b**2, m3, 2*c, m3, c**2,
                      m1, a, m2, b, m3, c,
                      m1, a, m2, b, m3, c,
                      m1, a**2, m2, b**2, m3, c**2,
                      x_ng, y_ng, z_ng,
                      x_ng, y_ng, z_ng))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
