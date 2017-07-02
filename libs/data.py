#!/usr/bin/env python
# coding:utf-8

import random
import base64
import requests
import js2py
from Crypto.Cipher import AES


param_1 = '{"csrf_token":""}'   # JSON.stringify(j0x)
# param_1 = '{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}'   # JSON.stringify(j0x)
param_2 = "010001"  # baJ5O(["流泪", "强"])
param_3 = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"  # baJ5O(OY2x.md)
param_4 = "0CoJUm6Qyw8W8jud"    # baJ5O(["爱心", "女孩", "惊恐", "大笑"])


def AES_encrypt(text, key, iv="0102030405060708"):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def random_num(num):
    """随机数i"""
    b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    c = ""
    for i in range(num):
        c += b[int(random.random()*len(b))]
    return c


def post_data(d, e, f, g):
    h = {}
    # i = random_num(16)
    i = 'msjSJZolY4hy1cOk'
    tmp = AES_encrypt(d, g)
    encText = AES_encrypt(tmp, i)
    # encSecKey = c(i, e, f)
    encSecKey = '0907b231190c23b9b9bf4d6acd20efbd7d19e085f2f246bb2a5b4c30899d25fcc729cb9cb276105733880c7282756c8ea89212e33803dd7c6560f6a56df0143418d178059fe01ef1cf1f1fce8d3a6049004bf40ff8731befce19443b470a85594c27c458171108e1a1411cfd8de123f58d3d57173167b497c6627c3e8080a450'
    return {
        'params': encText,
        'encSecKey': encSecKey
    }


data = post_data(param_1, param_2, param_3, param_4)



