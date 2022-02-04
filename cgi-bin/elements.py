#!/usr/bin/env python3
import cgi

import db.alchemy as alchemy

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <title>Элементы</title>
            <style>
                html {
                    height: 100%;
                    overflow-y: scroll;
                }

                body {
                    font-size: 30pt;
                    padding: 0 10vw;
                    color: #eee;
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
                    background: url(/skyrim-mixer/images/bg.jpg), #555;
                    background-repeat: no-repeat;
                    background-size: cover;
                    background-position: right;
                    background-blend-mode: overlay;
                }

                .form-control {
                    font-size: 30pt;
                    background: #3333;
                    color: #ddd;
                    border-color: #777;
                }

                .form-control:focus {
                    background: #4444;
                    border-color: #aaa;
                    box-shadow: 0 0 0 0.2rem rgb(100 100 100 / 25%)
                }
                
                #elements a:not(.last):after {
                    content: ', ';
                }
            </style>
        </head>
        <body>
        <h3 class="text-center mt-3 mb-5">Библиотека алхимии Skyrim</h3>
        <form class="text-center mb-5" action="javascript:void(0);">
            <div class='container'>
                <div class='row'>
                    <div class='col-12'>
                        <input id='search' class='form-control' type="text" onfocus="this.value=''" name="value" placeholder='Поиск по названию'>
                    </div>
                </div>
            </div>
        </form>
        """)

print("<div id='elements'>")
for el in alchemy.dict:
    link = el.replace(' ', '_').replace("'", '&apos;')
    print(f"<a href='mixer.py?el={link}'>{el.title()}</a>")
print("</div>")

print("""
        <script type="text/javascript" src="http://ajax.microsoft.com/ajax/jquery/jquery-1.4.2.min.js"></script> 
        <script>
            $('#elements a').last().addClass('last');
        
            $('#search').keyup(function() {
                let val = $(this).val();
                $('#elements a').each(function() {
                    if (!$(this).html().includes(val)) {
                        $(this).addClass('d-none');
                    }
                    else {
                        $(this).removeClass('d-none');
                    }
                });
                
                $('#elements a.last').removeClass('last');
                $('#elements a:not(.d-none)').last().addClass('last');
            });   
            
            $('#search').focus(function() {
                $(this).trigger('keyup');
            });
        </script>


        <div class='bg'></div>
        </body>
        </html>""")
