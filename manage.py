'''This is the management console for the reporting module.
This tool helps users 
1. create new reports
2. run reports
3. deploy reports to production'''

from pathlib import Path
import sys
import os
import subprocess
import shutil


def newreport(name):
    '''This function creates a new report folder structure that includes:
    1. a jupyter notebook for the main analysis
    2. a visuals directory
    3. a Jupyter Book directory '''

    name_low = name.lower()

    # general directories
    BASE_DIR = Path(__file__).resolve().parent
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    ANALYSIS_TEMPLATE_PATH = os.path.join(TEMPLATE_DIR, 'analysis_template.ipynb')
    # report specific directories
    REPORT_DIR = os.path.join(BASE_DIR, name_low)
    analysis = name_low + '_analysis.ipynb'
    ANALYSIS_DIR = os.path.join(REPORT_DIR, analysis)
    book = name_low + '_book'
    BOOK_DIR = os.path.join(REPORT_DIR, book)
    
    if not os.path.exists(REPORT_DIR):
        # create main report directory
        os.mkdir(REPORT_DIR)
        # copy notebook template for analysis
        shutil.copy(ANALYSIS_TEMPLATE_PATH, ANALYSIS_DIR)
        # Initialize Book with Jupyter Books
        bashCommand = "jupyter-book create {}/".format(BOOK_DIR)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    else:
        print('There is already a report with this name')


def run_report(name, scope='report_only'):
    if scope == 'all':
        # run analysis notebook
        print('Running {}'.format())

    # build book

    # open index.html

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])