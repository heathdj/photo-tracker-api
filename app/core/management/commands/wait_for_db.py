#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: photo-tracker-api/app/core/management/commands/wait_for_db.py
# Project: photo-tracker-api/app/core/management/commands
# Created Date: Sunday, March 19th 2023, 9:53:21 pm
# Author: David Heath
# -----
# Last Modified:
# Modified By:
# -----
#
# MIT License
#
# Copyright (c) 2023 BaldTraveler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copiesof the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###

'''
Django Command to wait for the db to be available
'''

import time


from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    ''' Djange command to wait for the database'''

    def handle(self, *args, **options):
        '''Entrypoint for command'''
        self.stdout.write('waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available...'))
