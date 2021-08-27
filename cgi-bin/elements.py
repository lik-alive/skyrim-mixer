#!/usr/bin/env python3
import cgi

import alchemy

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <title>Элементы</title>
            <style>
                #elements a:not(.last):after {
                    content: ', ';
                }
                body {
                    font-size: 30pt;
                    padding: 0 10px;
                }
                h3 {
                    margin-top: 20px;
                    font-size: 3rem;
                }
                input.form-control {
                    font-size: 30pt;
                }
            </style>
        </head>
        <body>
        <h3 class="text-center mb-3">Библиотека алхимии Skyrim</h3>
        <form class="text-center mb-2" action="javascript:void(0);">
            <div class='row'>
                <div class='col-12'>
                    <input id='search' class='form-control' type="text" onfocus="this.value=''" name="value" placeholder='Поиск по названию'>
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



        </body>
        </html>""")
