# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import, unicode_literals

import os
import subprocess

import numpy as np


def setup_function(function):
    try:
        os.remove('tests/output.txt')
    except:
        pass

teardown_function = setup_function


def test_module_invocation():
    p = subprocess.Popen(['python', '-m', 'apexpy', 'geo', 'apex', '2015', '--height', '300',
                          '-i', 'tests/test_convert.txt', '-o', 'tests/output.txt'])
    p.communicate()
    p.wait()
    data = np.loadtxt('tests/output.txt')
    np.testing.assert_allclose(data, [[57.469547, 93.639816], [58.522701, 94.044762], [59.571465, 94.477257]], rtol=1e-4)


def test_convert_YYYY():
    p = subprocess.Popen(['apexpy', 'geo', 'apex', '2015', '--height', '300',
                          '-i', 'tests/test_convert.txt', '-o', 'tests/output.txt'])
    p.communicate()
    p.wait()
    data = np.loadtxt('tests/output.txt')
    np.testing.assert_allclose(data, [[57.469547, 93.639816], [58.522701, 94.044762], [59.571465, 94.477257]], rtol=1e-4)


def test_convert_YYYYMM():
    p = subprocess.Popen(['apexpy', 'geo', 'apex', '201501', '--height', '300',
                          '-i', 'tests/test_convert.txt', '-o', 'tests/output.txt'])
    p.communicate()
    p.wait()
    data = np.loadtxt('tests/output.txt')
    np.testing.assert_allclose(data, [[57.469547, 93.639816], [58.522701, 94.044762], [59.571465, 94.477257]], rtol=1e-4)


def test_convert_YYYYMMDD():
    p = subprocess.Popen(['apexpy', 'geo', 'apex', '20150101', '--height', '300',
                          '-i', 'tests/test_convert.txt', '-o', 'tests/output.txt'])
    p.communicate()
    p.wait()
    data = np.loadtxt('tests/output.txt')
    np.testing.assert_allclose(data, [[57.469547, 93.639816], [58.522701, 94.044762], [59.571465, 94.477257]], rtol=1e-4)


def test_convert_YYYYMMDDHHMMSS():
    p = subprocess.Popen(['apexpy', 'geo', 'apex', '20150101000000', '--height', '300',
                          '-i', 'tests/test_convert.txt', '-o', 'tests/output.txt'])
    p.communicate()
    p.wait()
    data = np.loadtxt('tests/output.txt')
    np.testing.assert_allclose(data, [[57.469547, 93.639816], [58.522701, 94.044762], [59.571465, 94.477257]], rtol=1e-4)


def test_convert_single_line():
    p = subprocess.Popen(['apexpy', 'geo', 'apex', '20150101000000', '--height', '300',
                          '-i', 'tests/test_convert_single_line.txt', '-o', 'tests/output.txt'])
    p.communicate()
    p.wait()
    data = np.loadtxt('tests/output.txt')
    np.testing.assert_allclose(data, [57.469547, 93.639816], rtol=1e-4)


def test_convert_stdin_stdout():
    p = subprocess.Popen('echo 60 15 | apexpy geo apex 2015 --height 300', shell=True, stdout=subprocess.PIPE)
    stdout, _ = p.communicate()
    p.wait()
    assert b'57.469547, 93.639816' in stdout


def test_convert_mlt():
    p = subprocess.Popen(['apexpy', 'geo', 'mlt', '20150101000000', '--height', '300',
                          '-i', 'tests/test_convert_single_line.txt', '-o', 'tests/output.txt'])
    p.communicate()
    p.wait()
    data = np.loadtxt('tests/output.txt')
    np.testing.assert_allclose(data, [57.469547, 1.061383], rtol=1e-4)
