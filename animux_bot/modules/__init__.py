# Copyright (C) 2019 Nahuel Gomez Castro <nahual_gomca@outlook.com.ar>
#
# This file is part of Animux bot.
#
# Animux bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Animux bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from animux_bot import LOGGER


def __list_all_modules() -> list:
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + '/*.py')
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith('.py') and not f.endswith('__init__.py')]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
LOGGER.info('Modules to load: %s' % str(ALL_MODULES))
__all__ = ALL_MODULES + ['ALL_MODULES']
