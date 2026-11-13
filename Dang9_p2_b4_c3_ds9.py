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


def bt_Dang9_p2_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k1 = random.randint(2, 5)
        s1 = k1**3 + random.randint(1, 5)

        k2 = random.randint(3, 5)
        s2 = -(k2**3) + random.randint(1, 4)

        k3 = random.choice([2, 3])
        m3 = random.choice([2, 3, 5])
        tich3 = (k3**3) * m3

        k4 = random.randint(4, 6)
        s4 = k4**3 + random.randint(1, 4)

        noidungcauhoi = "Xét các phép so sánh số thực dưới đây:"

        nb_da_1_d = f"\\True ${k1} < \\sqrt[3]{{{s1}}}$."
        nb_da_1_s = f"${k1} > \\sqrt[3]{{{s1}}}$."
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = f"Ta có ${k1} = \\sqrt[3]{{{k1**3}}}$. Vì ${k1**3} < {s1}$ nên ${k1} < \\sqrt[3]{{{s1}}}$."

        th_da_1_d = f"\\True $-{k2} < \\sqrt[3]{{{s2}}}$."
        th_da_1_s = f"$-{k2} > \\sqrt[3]{{{s2}}}$."
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = f"Ta có $-{k2} = \\sqrt[3]{{-{k2**3}}}$. Vì $-{k2**3} < {s2}$ nên $-{k2} < \\sqrt[3]{{{s2}}}$."

        vd_da_1_d = f"\\True ${k3}\\sqrt[3]{{{m3}}} = \\sqrt[3]{{{tich3}}}$."
        vd_da_1_s = f"${k3}\\sqrt[3]{{{m3}}} = \\sqrt[3]{{{k3*m3}}}$."
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = f"Ta có $\\left({k3}\\sqrt[3]{{{m3}}}\\right)^3 = {k3}^3 \\cdot {m3} = {tich3}$, nên ${k3}\\sqrt[3]{{{m3}}} = \\sqrt[3]{{{tich3}}}$."

        vdc_da_1_d = f"\\True ${k4} < \\sqrt[3]{{{s4}}}$."
        vdc_da_1_s = f"${k4} > \\sqrt[3]{{{s4}}}$."
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = f"Ta có ${k4} = \\sqrt[3]{{{k4**3}}} < \\sqrt[3]{{{s4}}}$."

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

        combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
        combined_th = list(zip([th_da_1], [loigiai_th_1]))
        combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
        combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n'
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
