#!/usr/bin/env python3
import cgi

import db.alchemy as alchemy

form = cgi.FieldStorage()
value = form.getfirst("el", "не задано").replace('_', ' ')

# Load subfolder
import os
baseUrl = os.environ['BASE_URL']

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href=\"""" + baseUrl + """/resources/bootstrap.min.css">
            <link rel="icon" href=\"""" + baseUrl + """/images/favicon.ico">
            <title>Миксер</title>
            <style>
                html {
                    height: 100%;
                    overflow-y: scroll;
                }

                body {
                    font-size: 30pt;
                    padding: 0 10vw;
                    color: #eee;
                    background-color: black;
                }

                a {
                    color: #adf7ff;
                }
                
                a:hover {
                    text-decoration: none;
                    color: #00d4eb;
                }

                h3 {
                    padding-top: 20px;
                    font-size: 3rem;
                }

                .bg {
                    position: fixed;
                    top: 0;
                    left: 0;
                    z-index: -1;
                    height: 100vh;
                    width: 100vw;
                    background: url(""" + baseUrl + """/images/bg.jpg), #555;
                    background-repeat: no-repeat;
                    background-size: cover;
                    background-position: right;
                    background-blend-mode: overlay;
                }
                
                .list a:not(:last-child):after {
                    content: ', ';
                }
                
                .btn+div {
                    padding: 0 10px 0 10px;
                }
                
                .btn {
                    margin-bottom: 5px;
                    font-size: 24pt;
                }
                
                .collapser {
                    color: #ddd;
                    position: relative;
                    background-color: #3e3e3eed;
                    border-color: #3e3e3eed;
                }

                .collapser:focus, 
                .btn-primary:not(:disabled):not(.disabled):active,
                .btn-primary:not(:disabled):not(.disabled):active:focus {
                    background-color: #3e3e3eed;
                    border-color: #3e3e3eed;
                    box-shadow: 0 0 0 0.2rem rgb(50 50 50 / 50%);
                }

                .collapser:hover {
                    background-color: #242424ed;
                    border-color: #3e3e3eed;
                }
                
                .collapser:after {
                    content: '-';
                    position: absolute;
                    right: 10px;
                }
                
                .collapser.collapsed:after {
                    content: '+';
                }
                
                .row:not(:last-of-type) {
                    border: solid #ccc;
                    border-width: 0 0 1px 0;
                    margin-right: 0;
                    margin-left: 0;
                }
            </style>
        </head>
        <body>""")

print(f" <h3 class='text-center mt-3 mb-5'>Миксер для {value.title()}</h3>")

try:
    [base, els] = alchemy.process(value)
    mixes = alchemy.findMixes(els, 3)
    pos = 0

    if pos < mixes.__len__() and mixes[pos].__len__() == 1:
        print("""<button class='btn btn-primary btn-block collapser mt-2' type='button' 
        data-toggle='collapse' data-target='#collapseList1'>Комбинация из 1 ингредиента</button>""")
        print("<div id='collapseList1' class='collapse show'>")
        print("<div class='container'>")
        while pos < mixes.__len__() and mixes[pos].__len__() == 1:
            print("<div class='row'>")
            for el in mixes[pos]:
                link = el.replace(' ', '_').replace("'", '&apos;')
                print(f"<div class='col-6'><a href='mixer.py?el={link}'>{el.title()}</a></div>")
            print("</div>")
            pos += 1
        print("</div>")
        print("</div>")

    if pos < mixes.__len__() and mixes[pos].__len__() == 2:
        print("""<button class='btn btn-primary btn-block collapser mt-2' type='button' 
        data-toggle='collapse' data-target='#collapseList2'>Комбинация из 2 ингредиентов</button>""")
        print("<div id='collapseList2' class='collapse show'>")
        print("<div class='container'>")
        while pos < mixes.__len__() and mixes[pos].__len__() == 2:
            print("<div class='row'>")
            for el in mixes[pos]:
                link = el.replace(' ', '_').replace("'", '&apos;')
                print(f"<div class='col-6'><a href='mixer.py?el={link}'>{el.title()}</a></div>")
            print("</div>")
            pos += 1
        print("</div>")
        print("</div>")

    if pos < mixes.__len__() and mixes[pos].__len__() == 3:
        print("""<button class='btn btn-primary btn-block collapsed collapser mt-2' type='button' 
        data-toggle='collapse' data-target='#collapseList3'>Комбинация из 3 ингредиентов</button>""")
        print("<div id='collapseList3' class='collapse'>")
        print("<div class='container'>")
        while pos < mixes.__len__() and mixes[pos].__len__() == 3:
            print("<div class='row'>")
            for el in mixes[pos]:
                link = el.replace(' ', '_').replace("'", '&apos;')
                print(f"<div class='col-4'><a href='mixer.py?el={link}'>{el.title()}</a></div>")
            print("</div>")
            pos += 1
        print("</div>")
        print("</div>")

    print("""<button class='btn btn-primary btn-block collapser mt-2' type='button' 
            data-toggle='collapse' data-target='#collapseEffects'>Перечень связных элементов</button>""")
    print("<div id='collapseEffects' class='collapse show'>")
    print("<div class='container'>")
    for i in range(0, base.__len__()):
        print(f"<div class='row'><div class='font-weight-bold col-12 pl-0'>{base[i]}:</div><span class='list'>")
        for el in els[i]:
            link = el.replace(' ', '_').replace("'", '&apos;')
            print(f"<a href='mixer.py?el={link}'>{el.title()}</a>")
        print("</span></div>")
    print("</div>")
    print("</div>")
except Exception as ex:
    print(f"<p>{ex}</p>")

print("<br/>")
print("<a class='ml-2' href='elements.py'>&lt;- На главную</a>")

print("""
        <script src=\"""" + baseUrl + """/resources/jquery-3.4.1.slim.min.js"></script>
        <script src=\"""" + baseUrl + """/resources/bootstrap.min.js"></script>
        <div class='bg'></div>
        </body>
        </html>""")
