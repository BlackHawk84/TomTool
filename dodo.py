#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import Copan.System.Git
import Copan.System.Path
from PyQt4 import uic


DOIT_CONFIG = {
    'default_tasks': [
        '01_version',
        '02_pyqtforms',
    ]
}


def task_01_version():
    def write_file():

        if "TOMTOOL_VERSION" not in os.environ:
            try:
                version, _, _ = Copan.System.Git.get_git_build_number(".")
            except Exception:
                version = None
        else:
            version = os.environ["TOMTOOL_VERSION"]

        if version:
            with open('data/version', 'wb') as f:
                f.write(version)

    return {
        'verbosity': 2,
        'targets': ['data/version'],
        'actions': [(write_file,)],
    }


def task_02_pyqtforms():
    def get_forms():
        forms = {}
        for source in glob.iglob('data/forms/*.ui'):
            source_filename = Copan.System.Path.split(source)[-1]
            target_filename = source_filename.replace('.ui', '.py')
            target = os.path.join('TomTool', 'Generated', target_filename)
            forms[target] = source
        return forms

    def forms_actions():
        for (target, source) in get_forms().iteritems():
            with open(target, 'w') as f:
                uic.compileUi(source, f, True)
        return True

    forms = get_forms()
    return {
        'verbosity': 2,
        'actions': [(forms_actions,)],
        'file_dep': forms.values(),
        'targets': forms.keys(),
    }
