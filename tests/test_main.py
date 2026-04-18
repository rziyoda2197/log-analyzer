import pytest
import re
from log_analyzer import LogAnalyzer

def test_log_analyzer_init():
    log_analyzer = LogAnalyzer('test.log')
    assert log_analyzer.log_file == 'test.log'

def test_log_analyzer_read_log_file():
    log_analyzer = LogAnalyzer('test.log')
    log_data = log_analyzer.read_log_file()
    assert isinstance(log_data, list)

def test_log_analyzer_parse_log_data():
    log_analyzer = LogAnalyzer('test.log')
    log_data = log_analyzer.read_log_file()
    parsed_data = log_analyzer.parse_log_data(log_data)
    assert isinstance(parsed_data, dict)

def test_log_analyzer_analyze_errors():
    log_analyzer = LogAnalyzer('test.log')
    log_data = log_analyzer.read_log_file()
    parsed_data = log_analyzer.parse_log_data(log_data)
    errors = log_analyzer.analyze_errors(parsed_data)
    assert isinstance(errors, list)

def test_log_analyzer_get_error_count():
    log_analyzer = LogAnalyzer('test.log')
    log_data = log_analyzer.read_log_file()
    parsed_data = log_analyzer.parse_log_data(log_data)
    errors = log_analyzer.analyze_errors(parsed_data)
    error_count = log_analyzer.get_error_count(errors)
    assert isinstance(error_count, int)

def test_log_analyzer_get_error_types():
    log_analyzer = LogAnalyzer('test.log')
    log_data = log_analyzer.read_log_file()
    parsed_data = log_analyzer.parse_log_data(log_data)
    errors = log_analyzer.analyze_errors(parsed_data)
    error_types = log_analyzer.get_error_types(errors)
    assert isinstance(error_types, dict)
