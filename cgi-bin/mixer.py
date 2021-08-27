#!/usr/bin/env python3
import cgi

import alchemy

form = cgi.FieldStorage()
value = form.getfirst("el", "не задано").replace('_', ' ')



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <title>Миксер</title>
            <style>
                body {
                    font-size: 30pt;
                    padding: 0 10px;
                }
                h3 {
                    margin-top: 20px;
                    font-size: 3rem;
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
                
                button.collapser {
                    position: relative;
                }
                
                button.collapser:after {
                    content: '-';
                    position: absolute;
                    right: 10px;
                }
                
                button.collapser.collapsed:after {
                    content: '+';
                }
                
                .row {
                    border: solid #ccc;
                    border-width: 0 0 1px 0;
                    margin-right: 0;
                    margin-left: 0;
                }
                
                
            </style>
        </head>
        <body>""")

print(f" <h3 class='text-center mb-3'>Миксер для {value.title()}</h3>")

try:
    [base, els] = alchemy.process(value)
    mixes = alchemy.findMixes(els, 3)
    pos = 0

    if pos < mixes.__len__() and mixes[pos].__len__() == 1:
        print("""<button class='btn btn-primary btn-block collapser mt-2' type='button' 
        data-toggle='collapse' data-target='#collapseList1'>Комбинация из 1 ингредиента</button>""")
        print("<div id='collapseList1' class='collapse show'>")
        while pos < mixes.__len__() and mixes[pos].__len__() == 1:
            print("<div class='row'>")
            for el in mixes[pos]:
                link = el.replace(' ', '_').replace("'", '&apos;')
                print(f"<div class='col-6'><a href='mixer.py?el={link}'>{el.title()}</a></div>")
            print("</div>")
            pos += 1
        print("</div>")

    if pos < mixes.__len__() and mixes[pos].__len__() == 2:
        print("""<button class='btn btn-primary btn-block collapser mt-2' type='button' 
        data-toggle='collapse' data-target='#collapseList2'>Комбинация из 2 ингредиентов</button>""")
        print("<div id='collapseList2' class='collapse show'>")
        while pos < mixes.__len__() and mixes[pos].__len__() == 2:
            print("<div class='row'>")
            for el in mixes[pos]:
                link = el.replace(' ', '_').replace("'", '&apos;')
                print(f"<div class='col-6'><a href='mixer.py?el={link}'>{el.title()}</a></div>")
            print("</div>")
            pos += 1
        print("</div>")

    if pos < mixes.__len__() and mixes[pos].__len__() == 3:
        print("""<button class='btn btn-primary btn-block collapsed collapser mt-2' type='button' 
        data-toggle='collapse' data-target='#collapseList3'>Комбинация из 3 ингредиентов</button>""")
        print("<div id='collapseList3' class='collapse'>")
        while pos < mixes.__len__() and mixes[pos].__len__() == 3:
            print("<div class='row'>")
            for el in mixes[pos]:
                link = el.replace(' ', '_').replace("'", '&apos;')
                print(f"<div class='col-4'><a href='mixer.py?el={link}'>{el.title()}</a></div>")
            print("</div>")
            pos += 1
        print("</div>")

    print("""<button class='btn btn-primary btn-block collapser mt-2' type='button' 
            data-toggle='collapse' data-target='#collapseEffects'>Перечень связных элементов</button>""")
    print("<div id='collapseEffects' class='collapse show'>")
    for i in range(0, base.__len__()):
        print(f"<div class='row'><div class='font-weight-bold col-12 pl-0'>{base[i]}:</div><span class='list'>")
        for el in els[i]:
            link = el.replace(' ', '_').replace("'", '&apos;')
            print(f"<a href='mixer.py?el={link}'>{el.title()}</a>")
        print("</span></div>")
    print("</div>")
except Exception as ex:
    print(f"<p>{ex}</p>")

print("<br/>")
print("<a class='ml-2' href='elements.py'>&lt;- На главную</a>")

print("""
        <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

        <script type="text/javascript" src="http://ajax.microsoft.com/ajax/jquery/jquery-1.4.2.min.js"></script>
        </body>
        </html>""")
