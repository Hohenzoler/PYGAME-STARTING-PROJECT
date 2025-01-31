from configparser import ConfigParser
import os

# Copyright (C) 2025  Hohenzoler
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

def set_config():  # Function that will create the config file or update it if it's out of date
    config = ConfigParser()
    config_file = 'config.ini'  # Path to config file
    version = '0.0.1'  # Current version

    if not os.path.exists(config_file):  # Checks if configuration file exists

        config['CONFIG'] = generate_default_config_data(version)  # Generates default configs
        write_config_to_file(config, config_file)  # Writes the config to config_file

    else:  # If file exists
        config.read(config_file)  # Reads the config
        config_data = config['CONFIG']

        if version != config_data[
            'version']:  # Checks if the application version and the config versions aren't the same
            configurations = generate_default_config_data(version)  # Generate default config
            title = configurations['title']
            debug = configurations['enable_debug']
            configurations.update(config_data)  # Updates the default config with current configs so that previous settings stay the same
            configurations['version'] = version  # Updates the version since when updating the configs the version also got upated to the previous version
            configurations['title'] = title
            configurations['enable_debug'] = debug
            config['CONFIG'] = configurations  # Sets the updated configs as the config
            write_config_to_file(config, config_file)  # Writes the updated config to file


def generate_default_config_data(version):
    return {
        'version': version,
        'width': 1000,
        'height': 1000,
        'fps': 60,
        'title': 'PYGAME-STARTING-PROJECT',
        'full-screen': 0,
        'enable_debug': 1
    }


def write_config_to_file(config, config_file):
    with open(config_file, 'w') as f:
        config.write(f)
        f.close()


def read_config():
    config = ConfigParser()
    config_file = 'config.ini'  # Path to config file

    config.read(config_file)  # Reads config from config_file

    cfg = {}  # Creates an empty dict

    for key, value in config['CONFIG'].items():
        cfg[key] = value  # Adds configuration to the dict
    return cfg  # Returns the dict
