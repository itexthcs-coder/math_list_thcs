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

def bt_Dang5_p2_b1_c4_hh9(self):
    # Khai báo biến
    bc_val = random.choice([4, 6, 8, 10, 12])
    ab_kq = Rational(bc_val, 2)
    ac_kq = Rational(bc_val, 2) * sqrt(3)
    s_kq = Rational(1, 2) * ab_kq * ac_kq

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (C) at (4.5,0);\n'
        '\\coordinate (B) at (0,2.6);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
        '\\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);\n'
        '\\fill (A) circle (1pt) node[below left] {$A$};\n'
        '\\fill (B) circle (1pt) node[above left] {$B$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
    )

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có $\\widehat{C} = 30^{\\circ}$ và cạnh huyền $BC = %d\\text{ cm}$ (như hình vẽ). %s''' % (bc_val, hinh_ve))

    nb_da_1_d = '\\True Số đo góc $B$ bằng $60^{\\circ}$'
    nb_da_1_s = 'Số đo góc $B$ bằng $45^{\\circ}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Trong $\\triangle ABC$ vuông tại $A$, $\\widehat{B} = 90^{\\circ} - \\widehat{C} = 90^{\\circ} - 30^{\\circ} = 60^{\\circ}$.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Độ dài cạnh $AB$ bằng $%s\\text{ cm}$' % latex(ab_kq)
    th_da_1_s = 'Độ dài cạnh $AB$ bằng $%s\\text{ cm}$' % latex(ac_kq)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $AB = BC \\cdot \\sin C = %d \\cdot \\sin 30^{\\circ} = %d \\cdot \\dfrac{1}{2} = %s\\text{ cm}$.''' % (bc_val, bc_val, latex(ab_kq)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Độ dài cạnh $AC$ bằng $%s\\text{ cm}$' % latex(ac_kq)
    vd_da_1_s = 'Độ dài cạnh $AC$ bằng $%s\\text{ cm}$' % latex(Rational(bc_val, 2) * sqrt(2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $AC = BC \\cdot \\cos C = %d \\cdot \\cos 30^{\\circ} = %d \\cdot \\dfrac{\\sqrt{3}}{2} = %s\\text{ cm}$.''' % (bc_val, bc_val, latex(ac_kq)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Diện tích tam giác $ABC$ bằng $%s\\text{ cm}^2$' % latex(s_kq)
    vdc_da_1_s = 'Diện tích tam giác $ABC$ bằng $%s\\text{ cm}^2$' % latex(2 * s_kq)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Diện tích $\\triangle ABC$ là $S = \\dfrac{1}{2}AB \\cdot AC = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ cm}^2$.''' % (latex(ab_kq), latex(ac_kq), latex(s_kq)))
    list_vdc_2 = [loigiai_vdc_1]
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n'
    )
    return content
