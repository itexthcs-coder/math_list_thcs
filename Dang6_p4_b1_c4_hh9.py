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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_Dang6_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        g1 = randint(14, 38)
        g2 = 90 - g1
        g3 = randint(18, 42)
        while g3 == g1:
            g3 = randint(18, 42)
        g4 = 90 - g3
        k1 = randint(2, 7)
        k2 = randint(2, 6)
        
        g5 = randint(15, 35)
        g6 = 90 - g5
        g7 = randint(12, 40)
        g8 = 90 - g7

        # Nội dung câu hỏi
        noidungcauhoi = ('''Không sử dụng máy tính cầm tay, hãy tính giá trị của các biểu thức sau: \\\\
                         a) $M = \\dfrac{%d\\tan %d^{\\circ}}{\\cot %d^{\\circ}} + %d\\sin %d^{\\circ} - %d\\cos %d^{\\circ}$. \\\\
                         b) $N = \\sin^2 %d^{\\circ} + \\sin^2 %d^{\\circ} + \\tan %d^{\\circ} \\cdot \\tan %d^{\\circ}$. '''
                         % (k1, g1, g2, k2, g3, k2, g4, g5, g6, g7, g8))
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Vì $%d^{\\circ} + %d^{\\circ} = 90^{\\circ}$ và $%d^{\\circ} + %d^{\\circ} = 90^{\\circ}$ nên $\\tan %d^{\\circ} = \\cot %d^{\\circ}$ và $\\sin %d^{\\circ} = \\cos %d^{\\circ}$. \\\\
                        Ta có: $M = \\dfrac{%d\\cot %d^{\\circ}}{\\cot %d^{\\circ}} + %d\\cos %d^{\\circ} - %d\\cos %d^{\\circ} = %d + 0 = %d$. \n
                        \\item Vì $%d^{\\circ} + %d^{\\circ} = 90^{\\circ}$ và $%d^{\\circ} + %d^{\\circ} = 90^{\\circ}$ nên $\\sin %d^{\\circ} = \\cos %d^{\\circ}$ và $\\tan %d^{\\circ} = \\cot %d^{\\circ}$. \\\\
                        Xét tam giác vuông có góc nhọn $\\alpha = %d^{\\circ}$ với cạnh đối $a$, cạnh kề $b$, cạnh huyền $c$, ta có: \\\\
                        $\\sin^2 %d^{\\circ} + \\cos^2 %d^{\\circ} = \\left(\\dfrac{a}{c}\\right)^2 + \\left(\\dfrac{b}{c}\\right)^2 = \\dfrac{a^2 + b^2}{c^2} = \\dfrac{c^2}{c^2} = 1$. \\\\
                        Mặt khác $\\tan %d^{\\circ} \\cdot \\cot %d^{\\circ} = 1$. Do đó $N = 1 + 1 = 2$. \n
                        \\end{enumEX} \n'''
                   % (g1, g2, g3, g4, g1, g2, g3, g4, k1, g2, g2, k2, g4, k2, g4, k1, k1,
                      g5, g6, g7, g8, g6, g5, g8, g7, g5, g5, g5, g7, g7))
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
