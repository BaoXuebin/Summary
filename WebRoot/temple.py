#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-08 10:20:27
# @Author  : BaoXuebin (baoxbin@hotmail.com)
# @Link    : ${link}
# @Version : $Id$
import re
import os

# 生成目录，传入参数为Dic
def domTemplate(params):
    content = '''<!-- 这是 {title} 页面 -->
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <title>{title}</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="/esf-api/css/bootstrap.min.css" rel="stylesheet">
        <link href="/esf-api/css/desert.css" rel="stylesheet">
        <script src="/esf-api/js/jquery-1.12.1.js"></script>
        <style type="text/css">
            .esf-container{
                width: 950px;
                margin: 30px auto;
            }
        </style>
        <script type="text/javascript">
            $(function(){
                $.get("/esf-api/md/{pardom}/{name}.md").success(function(data) {
                    var mdcontent = markdown.toHTML(data, 'Maruku');
                    $("#esf-content").html(mdcontent);
                    $("pre").addClass("prettyprint");
                    prettyPrint();
                }); 
            })
        </script>
    </head>
    <body>
        <div class="esf-container">
            <ol class="breadcrumb">
                <li><a href="esf.html">ESF</a></li>
                <li class="active">{title}</li>
            </ol>
            <div class="esf-content" id="esf-content">
                <!-- 插入内容 -->
            </div>
            <hr>
            <nav>
                <ul class="pager">
                    <li><a href="{preurl}">{prename}</a></li>
                    <li><a href="{nexturl}">{nextname}</a></li>
                </ul>
            </nav>
        </div>
        <script src="/esf-api/js/bootstrap.min.js"></script>
        <script src="/esf-api/js/markdown.js"></script>
        <script src="/esf-api/js/prettify.js"></script>
    </body>
    </html>'''

    pat_keys = params.keys()

    for pat in pat_keys:
            content = re.sub(pat, params.get(pat), content)

    return content

# 生成文件，传入参数为Dic
def htmlTemplate(params):

    content = '''<!-- 这是 {title} 页面 -->
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <title>{title}</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="/esf-api/css/bootstrap.min.css" rel="stylesheet">
        <link href="/esf-api/css/desert.css" rel="stylesheet">
        <script src="/esf-api/js/jquery-1.12.1.js"></script>
        <style type="text/css">
            .esf-container{
                width: 950px;
                margin: 30px auto;
            }
        </style>
        <script type="text/javascript">
            $(function(){
                $.get("/esf-api/md/{pardom}/{name}.md").success(function(data) {
                    var mdcontent = markdown.toHTML(data, 'Maruku');
                    $("#esf-content").html(mdcontent);
                    $("pre").addClass("prettyprint");
                    prettyPrint();
                }); 
            })
        </script>
    </head>
    <body>
        <div class="esf-container">
            <ol class="breadcrumb">
                <li><a href="esf.html">ESF</a></li>
                <li><a href="../{pardom}.html">开发模版</a></li>
                <li class="active">{title}</li>
            </ol>
            <div class="esf-content" id="esf-content">
                <!-- 插入内容 -->
            </div>
            <hr>
            <nav>
                <ul class="pager">
                    <li><a href="{preurl}">{prename}</a></li>
                    <li><a href="{nexturl}">{nextname}</a></li>
                </ul>
            </nav>
        </div>
        <script src="/esf-api/js/bootstrap.min.js"></script>
        <script src="/esf-api/js/markdown.js"></script>
        <script src="/esf-api/js/prettify.js"></script>
    </body>
    </html>'''

    pat_keys = params.keys()

    for pat in pat_keys:
            content = re.sub(pat, params.get(pat), content)

    return content

# 创建文件夹
def createDir(path):
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)

# 结构化文件目录
def documentStruct(root):
    createDir(root)
    createDir(root + "\\html")
    createDir(root + "\\md")

# 在对应文件加下，生成对应的 md 文件
def writeMd2File(path, parent, name, content):
    if parent:
        createDir(path + "\\" + parent)
    url = path + "\\" + parent + "\\" + name 
    file = open(url, 'w', 1, 'utf-8')
    file.write("# " + content)
    file.close()

# 在对应文件加下，生成对应的 html 文件
def writeHtml2File(path, parent, name, content):
    if parent:
        createDir(path + "\\" + parent)
    url = path + "\\" + parent + "\\" + name 
    file = open(url, 'w', 1, 'utf-8')
    file.write(content)
    file.close()

# 生成字典
def createDic():

    _list = []

    data = [
        {
            "title": "总体介绍",
            "name": "introduce",
        },
        {
            "title": "开发指南",
            "name": "tutorial",
        },
        {
            "title": "开发规范",
            "name": "standard",
        },
        {
            "title": "开发模版",
            "name": "template",
        },
    ]

    i = 0
    for d in data:
        dic = {}
        dic['{pardom}'] = ""
        dic['{title}'] = d.get("title")
        dic['{name}'] = d.get("name")
        if not i: # i等于0
            dic['{preurl}'] = "#"
            dic['{prename}'] = "没有了"
        else:
            dic['{preurl}'] = data[i-1].get("name") + ".html"
            dic['{prename}'] = data[i-1].get("title")

        if i >= len(data) - 1: # i 是最后一个
            dic["{nexturl}"] = "#"
            dic["{nextname}"] = "没有了"
        else:
            dic["{nexturl}"] = data[i+1].get("name") + ".html"
            dic["{nextname}"] = data[i+1].get("title")

        _list.append(dic)
        i = i + 1

    return _list

# 生成目录文件
def generateDom():
    rootpath = r"C:\Users\wanda\Desktop\temp";
    _list = createDic()
    for l in _list:
        htmlpath = rootpath + "\\html"
        mdpath = rootpath + "\\md"
        parentdir = l.get('{pardom}')
        filename = l.get('{name}')
        title = l.get('{title}')

        writeHtml2File(htmlpath, parentdir, filename+".html", domTemplate(l))
        writeMd2File(mdpath, parentdir, filename+".md", title)


if __name__ == '__main__':
    '''父目录, title, name, preurl, prename, nexturl, nextname'''
    # params = {
    #     '{pardom}': "",
    #     '{title}': "开发模版", 
    #     '{name}': "template",
    #     '{preurl}': "developer_standard.html", 
    #     '{prename}': "开发规范", 
    #     '{nexturl}': "#", 
    #     '{nextname}': "没有了", 
    # }

    # # rootpath = "E:\Project\esf-api\public"
    # rootpath = r"C:\Users\wanda\Desktop\temp";

    # # 结构化模版目录
    # documentStruct(rootpath)

    # htmlpath = rootpath + "\\html"
    # mdpath = rootpath + "\\md"
    # parentdir = params.get('{pardom}')
    # filename = params.get('{name}')
    # title = params.get('{title}')

    # # writeHtml2File(htmlpath, parentdir, filename+".html", htmlTemplate(params))
    # writeHtml2File(htmlpath, parentdir, filename+".html", domTemplate(params))
    # writeMd2File(mdpath, parentdir, filename+".md", title)

    generateDom()

    print ("Finish!")