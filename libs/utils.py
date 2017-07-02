#!/usr/bin/env python
# coding:utf-8

import re
from database.tables import session


patt = re.compile(r'\d+$')
search = lambda string: re.search(patt, string)


def store2db(table, result):
    try:
        data = table(**result)
        session.add(data)
        session.commit()
    except Exception as e:
        print e
        session.rollback()