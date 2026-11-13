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


def bt_Dang13_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c1, c2 = randint(2, 4), randint(3, 5)
        c3 = randint(1, c1 + c2 - 1)
        tong_c = c1 + c2 - c3
        nghiem_a = randint(2, 5)
        vp_a = tong_c * nghiem_a

        k = random.choice([2, 3])
        m, n = randint(2, 3), randint(2, 4)
        c_b = randint(1, 5)
        val_b = randint(2, 5)
        vp_b = k * m * n * val_b

        c_c = randint(2, 6)
        vp_c = randint(3, 8)
        tamthuc_c = sp.expand((x - c_c)**2)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Giải các phương trình sau:\\
                         a) $\sqrt{%sx} + \sqrt{%sx} - \sqrt{%sx} = %s$ (với $x \ge 0$).\\
                         b) $\sqrt{%s(x - %s)} \cdot \sqrt{%s(x - %s)} = %s$ (với $x \ge %s$).\\
                         c) $\sqrt{%s} = %s$.'''
                         % (latex(c1**2), latex(c2**2), latex(c3**2), latex(vp_a),
                            latex(k*(m**2)), latex(c_b), latex(k*(n**2)), latex(c_b), latex(vp_b), latex(c_b),
                            latex(tamthuc_c), latex(vp_c)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Với $x \ge 0$, phương trình tương đương với:
                      $$%s\sqrt{x} + %s\sqrt{x} - %s\sqrt{x} = %s \Leftrightarrow %s\sqrt{x} = %s \Leftrightarrow \sqrt{x} = %s \Leftrightarrow x = %s \text{ (thỏa mãn)}.$$
                      \item Với $x \ge %s$, áp dụng quy tắc nhân hai căn bậc hai, ta có:
                      $$\sqrt{%s(x - %s)^2} = %s \Leftrightarrow %s|x - %s| = %s \Leftrightarrow x - %s = %s \Leftrightarrow x = %s \text{ (thỏa mãn)}.$$
                      \item Ta có $\sqrt{%s} = %s \Leftrightarrow \sqrt{(x - %s)^2} = %s \Leftrightarrow |x - %s| = %s$.
                      Suy ra $x - %s = %s$ hoặc $x - %s = -%s$, tìm được $x = %s$ hoặc $x = %s$.
                      \\end{enumEX}'''
                   % (latex(c1), latex(c2), latex(c3), latex(vp_a), latex(tong_c), latex(vp_a), latex(nghiem_a), latex(nghiem_a**2),
                      latex(c_b), latex((k*m*n)**2), latex(c_b), latex(vp_b), latex(k*m*n), latex(c_b), latex(vp_b), latex(c_b), latex(val_b), latex(c_b + val_b),
                      latex(tamthuc_c), latex(vp_c), latex(c_c), latex(vp_c), latex(c_c), latex(vp_c),
                      latex(c_c), latex(vp_c), latex(c_c), latex(vp_c), latex(c_c + vp_c), latex(c_c - vp_c)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
