'''
Handles the configuration file parser.
'''
import configparser
import os
        
def initialize_cfg(path: str) -> configparser.ConfigParser:
    '''
    Returns a config file parser corresponding to a given configuration file
    path.
    '''
    c = configparser.ConfigParser()
    c.read(path)
    return c