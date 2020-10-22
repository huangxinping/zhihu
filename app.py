#!/usr/bin/env python
import os
from lxml import etree, html
import time
import pdfkit
import fire
import shutil
from tqdm import tqdm

start_section = """
<!DOCTYPE html>
<html lang="zh">
    <head>
        <meta charset="UTF-8">
        <title>
            1234567890
        </title>
        <link rel="stylesheet" type="text/css" href="print.css" media="print">
        <style type="text/css">
            *,::after,::before{box-sizing: border-box;}body{font-size: 1.2rem;line-height: 1.5em;background-color: #f6f6f6;font-family: "PT Serif", "Times New Roman", Times, serif, "Helvetica Neue", Helvetica, Arial, sans-serif;color: rgb(31, 9, 9);}.article{max-width: 50em;margin: 0px auto;padding: 6em;background: #fff;overflow: hidden;border-radius: 2px;-webkit-box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);-webkit-box-sizing: border-box;box-sizing: border-box;}p{margin-bottom: 1.5em;line-height: inherit;}p img[eeimg]{display: inline-block;margin: 0 3px;max-width: 100%;vertical-align: middle;}p + ul,p + ol{margin-top: 0.5em;}blockquote{margin: 0 2em;background: #eee;border-radius: 5px;padding: 15px;color: rgb(101, 101, 101);font-style: italic;}blockquote p{background: #eee;border-radius: 5px;}blockquote p::before{content: "\201C";}blockquote p::after{content: "\201D";}blockquote ul,blockquote ol{margin-left: 0px;}blockquote::before,blockquote::after,q::before,q::after{content: none;}blockquote > :first-child,li > :first-child{margin-top: 0px;}blockquote > :last-child{margin-bottom: 0px;}blockquote,q{quotes: none;}a{cursor: pointer;text-decoration: none;color: #3ac19f;}a:hover,a:active{text-decoration: none;color: #ff6188;outline: 0px;}a.url{word-break: break-all;}table tr th{border-bottom: 0px;}table{border-collapse: collapse;border-spacing: 0px;margin-bottom: 1.5em;font-size: 1em;width: 100%;overflow: auto;break-inside: auto;text-align: left;}header,footer{font-family: "PT Serif", "Times New Roman", Times, serif;color: rgb(31, 9, 9);}thead{background-color: rgb(218, 218, 218);display: table-header-group;}thead th,tfoot th{padding: 0.25em 0.25em 0.25em 0.4em;text-transform: uppercase;}tr{break-inside: avoid;break-after: auto;}tr:nth-child(2n){background: rgb(232, 231, 231);}th{text-align: left;}td{vertical-align: top;padding: 0.25em 0.25em 0.25em 0.4em;}tt{font-size: 0.8em;line-height: 1.7em;}ol,ul{text-indent: 0;position: relative;list-style: none;margin: 0px 0px 1.5em 1.5em;}ol li{list-style-type: decimal;list-style-position: outside;}ul li{list-style-type: disc;list-style-position: outside;}li div{padding-top: 0px;}li{margin: 0px;margin-left: 2em;position: relative;}li > figure:last-child{margin-bottom: 0.5rem;}li > :first-child{margin-top: 0px;}li > ul,li > ol{margin-top: inherit;margin-bottom: 0px;}li ol > li{list-style-type: lower-alpha;}li li ol > li{list-style-type: lower-roman;}kbd{margin: 0px 0.1em;padding: 0.1em 0.6em;font-size: 0.8em;color: rgb(36, 39, 41);background: rgb(255, 255, 255);border: 1px solid rgb(173, 179, 185);border-radius: 3px;box-shadow: rgba(12, 13, 14, 0.2) 0px 1px 0px,rgb(255, 255, 255) 0px 0px 0px 2px inset;white-space: nowrap;vertical-align: middle;}samp,tt{font-family: var(--monospace);}hr{border-bottom: 1px solid #d6d6d6;margin-inline-start: 15%;margin-inline-end: 15%;margin-block-start: 5rem;margin-block-end: 5rem;}u{text-decoration: none;border-bottom: 1px dashed #f40;}figure{margin: 2em auto;max-width: 100%;padding: 0px;font-size: 1rem;text-align: center;}figure img{display: block;max-width: 60%;margin: auto;}figure figcaption{padding: 0 1em;font-size: 0.9rem;color: #999;}figure > table{margin: 0px !important;}div.hr:focus{cursor: none;}a img,img a{cursor: pointer;}
        </style>
        <style type="text/css">
            .background-image{text-align: center;max-width: inherit;}.background-image img{max-width: 100%;}.video{max-width: inherit;margin: 80px auto;}.video-cover{max-width: inherit;background-color: #141216;}.video img{height: 400px;display: block;margin: 0 auto;}.video-tip{border-radius: 0 0 8px 8px;max-width: inherit;height: 34px;text-align: center;}.header{margin-bottom: 80px;}.title{font-size: 36px;margin-bottom: 80px;text-align: center;line-height: 42px;}.AuthorInfo,.Avatar{border-radius: 5px;}.Popover{width: 50px;height: 50px;}.AuthorInfo{width: 240px;margin: auto;}.AuthorInfo-content{position: relative;left: 60px;top: -50px;line-height: 1em;padding: 6px 0;}.AuthorInfo-name{font-size: 16px;}.AuthorInfo-detail{font-size: 16px;margin-top: 8px;}.Popover,.AuthorInfo,.AuthorInfo-content,.AuthorInfo{height: 50px;}.LinkCard{margin: 1em auto;width: 390px !important;border-radius: 12px;}.LinkCard-content{position: relative;display: -webkit-box;display: -ms-flexbox;display: flex;-webkit-box-align: center;-ms-flex-align: center;align-items: center;-webkit-box-pack: justify;-ms-flex-pack: justify;justify-content: space-between;padding: 12px;border-radius: inherit;background-color: hsla(0, 0%, 96.5%, 0.88);}.LinkCard-text{overflow: hidden;}.LinkCard-title{display: -webkit-box;-webkit-line-clamp: 2;-webkit-box-orient: vertical;overflow: hidden;text-overflow: ellipsis;max-height: 40px;font-size: 16px;font-weight: 500;line-height: 1.25;color: #1a1a1a;}.LinkCard-meta{display: -webkit-box;display: -ms-flexbox;display: flex;margin-top: 4px;font-size: 14px;line-height: 20px;color: #999;white-space: nowrap;}.LinkCard-imageCell{margin-left: 8px;border-radius: 6px;}.LinkCard-image{display: block;margin: 0 !important;width: 60px;height: 60px;-o-object-fit: cover;object-fit: cover;border-radius: inherit;}.LinkCard-image--default{display: -webkit-box;display: -ms-flexbox;display: flex;-webkit-box-align: center;-ms-flex-align: center;align-items: center;-webkit-box-pack: center;-ms-flex-pack: center;justify-content: center;background-color: #ebebeb;color: #d3d3d3;}svg:not(:root){overflow: hidden;}.TipCard,.LinkCard{position: relative;display: block;width: inherit;-webkit-box-sizing: border-box;box-sizing: border-box;max-width: 100%;overflow: hidden;text-indent: 0 !important;}.TipCard,.LinkCard,.TipCard:hover,.LinkCard:hover{text-decoration: none;border: none !important;color: inherit !important;}.TipCard-backdrop,.LinkCard-backdrop{position: absolute;top: 0;left: 0;right: 0;bottom: 0;background-repeat: no-repeat;-webkit-filter: blur(20px);filter: blur(20px);background-size: cover;background-position: 50%;}.divide{height: 30px;max-width: 45em;margin: 0 auto;}.reference{text-indent: 0;font-size: 14px;}.reference tr:nth-child(2n){background: white;}
        </style>
    </head>
    <body>
"""
end_section = """
    </body>
</html>
"""


def timer(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        func(*args, **kw)
        t2 = time.time()
        print(f'耗时{t2 - t1}秒')

    return wrapper


def to_pdf(path):
    print('开始转换到PDF...')
    try:
        file_name = os.path.basename(path)
        title = file_name.replace('.html', '')
        pdfkit.from_file(path, f'{path.replace(file_name, "")}{title}.pdf')
    except Exception as e:
        ...


def title():
    return os.listdir('./question')[0]


def agree_numbers(elem):
    return int(elem.split('-')[1])


@timer
def main(id, path=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop'), format='html', threshold=10):
    # Step 1: spider answers
    os.system(f'zhihu -u https://www.zhihu.com/question/{id} -w {os.getcwd()}')

    # Step 2: merge
    name = title()
    if os.path.exists(f'{path}/{name}.html'):
        os.remove(f'{path}/{name}.html')
    with open(f'{path}/{name}.html', 'a+') as w:
        w.writelines(start_section.replace('1234567890', name))
    need_have_title = True
    for file in tqdm(sorted(
            [file_name for file_name in os.listdir(f'./question/{name}') if int(file_name.split('-')[1]) > threshold],
            key=agree_numbers, reverse=True)):
        if not file.endswith('html'):
            continue
        with open(f'./question/{name}/{file}') as f:
            content = f.readlines()
            parser = etree.HTMLParser(encoding="utf-8")
            selector = etree.HTML(''.join(content), parser=parser)
            try:
                body = selector.xpath('//div[@class="article"]')
                if len(body):
                    with open(f'{path}/{name}.html', 'a+') as w:
                        text = html.tostring(body[0]).decode("utf-8")
                        if not need_have_title:
                            tmp = text.split('\n')
                            tmp = tmp[:2] + tmp[7:]
                            tmp[10] = f'{tmp[10]}-{file.split("-")[1]}点赞'
                            text = ''.join(tmp)
                        else:
                            tmp = text.split('\n')
                            tmp[15] = f'{tmp[15]}-{file.split("-")[1]}点赞'
                            text = ''.join(tmp)
                        w.writelines(text)
                        need_have_title = False
            except Exception as e:
                ...
    with open(f'{path}/{name}.html', 'a+') as w:
        w.writelines(end_section)

    # Step 3: remove temp files
    shutil.rmtree('./question')

    # Step 4: check if need convert to pdf
    if format == 'pdf':
        to_pdf(f'{path}/{name}.html')
        os.remove(f'{path}/{name}.html')


if __name__ == "__main__":
    fire.Fire(main)
