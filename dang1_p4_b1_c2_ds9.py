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


def bt_dang1_p4_b1_c2_ds9(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        x = symbols('x')
        while True:
            a1 = random.choice([2, 3])
            r1 = random.choice([1, 2, 3])
            r2 = random.choice([1, 2, 3])
            # (x - r1)(a1*x - 1) = a1*x^2 - (a1*r1 + 1)*x + r1 = 0
            # (a2*x - 1)(x + r2) = a2*x^2 + (a2*r2 - 1)*x - r2 = 0
            a2 = random.choice([2, 3])
            if r1 != r2 and a1 != a2:
                break
    
        pt1 = expand((x - r1)*(a1*x - 1))
        pt2 = expand((x + r2)*(a2*x - 1))
        x1_a = r1
        x2_a = Rational(1, a1)
        x1_b = -r2
        x2_b = Rational(1, a2)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giải các phương trình sau bằng cách đưa về phương trình tích: \\\\
                         a) $%s = 0$ \\\\
                         b) $%s = 0$'''
                         %(latex(pt1), latex(pt2)))
    
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Biến đổi phương trình về phương trình tích bằng cách tách hạng tử bậc nhất: \\\\
                        $%s = 0$ \\\\
                        $%sx^2 - %sx - x + %s = 0$ \\\\
                        $%sx(x - %s) - (x - %s) = 0$ \\\\
                        $(x - %s)(%sx - 1) = 0$. \\\\
                        Ta giải hai phương trình: \\\\
                        $\\bullet$ $x - %s = 0$, suy ra $x = %s$. \\\\
                        $\\bullet$ $%sx - 1 = 0$, suy ra $x = %s$. \\\\
                        Vậy tập nghiệm của phương trình là $S = \\left\\{%s; %s\\right\\}$. \n
                        \\item Biến đổi phương trình về phương trình tích như sau: \\\\
                        $%s = 0$ \\\\
                        $%sx^2 + %sx - x - %s = 0$ \\\\
                        $%sx(x + %s) - (x + %s) = 0$ \\\\
                        $(x + %s)(%sx - 1) = 0$. \\\\
                        Ta giải hai phương trình: \\\\
                        $\\bullet$ $x + %s = 0$, suy ra $x = %s$. \\\\
                        $\\bullet$ $%sx - 1 = 0$, suy ra $x = %s$. \\\\
                        Vậy tập nghiệm của phương trình là $S = \\left\\{%s; %s\\right\\}$. \n
                        \\end{enumEX} \n'''
                   %(latex(pt1),
                     latex(a1), latex(a1*r1), latex(r1),
                     latex(a1), latex(r1), latex(r1),
                     latex(r1), latex(a1),
                     latex(r1), latex(x1_a),
                     latex(a1), latex(x2_a),
                     latex(x1_a), latex(x2_a),
                     latex(pt2),
                     latex(a2), latex(a2*r2), latex(r2),
                     latex(a2), latex(r2), latex(r2),
                     latex(r2), latex(a2),
                     latex(r2), latex(x1_b),
                     latex(a2), latex(x2_b),
                     latex(x1_b), latex(x2_b)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
