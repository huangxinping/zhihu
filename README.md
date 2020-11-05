# 爬取知乎问题所有回答，并合并为单个 HTML 或 PDF 文件

## 环境

> Python 3.6+    
> Linux、Unix，不支持 Windows    
> wkhtmltopdf - 如果需要导出为 PDF 则需要安装 (https://wkhtmltopdf.org/downloads.html)

## 安装

### A 方案 - 不支持命令行 

> pip install -r requirements.txt

### B 方案 - 不支持命令行 

> 1. 安装 ZhihuSpider 库    
    - git clone https://github.com/huangxinping/ZhihuSpider.git    
    - cd ZhihuSpider    
    - python setup.py install && pip install .    
> 2. 安装另外一些第三方库    
    pip install fire tqdm pdfkit `如果需要导出为 PDF，则需要安装 pdfkit`

### C 方案 - 支持命令行    

> cd zhihuer    
> python setup.py install && pip install .    

## 玩一玩
    1. 通过正常脚本
        python app.py --id {question_id} --path {path} --format {format}   
        -- path: 默认是桌面（测试环境：Mac OS）    
        -- format: html或pdf，默认为 html
        -- threshold：阈值，低于该阈值的点赞数回答则过滤，默认为 10
    2. 通过命令行，支持多个ID通过爬取、合并
        经过 C 方案安装，会自动安装 cli，所以可以通过命令行操作
        zhihuer --id 
                --destination 
                --format 
                --threshold 

## 例子

```
1. 脚本化
cd zhihuer && python app.py --id 345516318 --path ~/Desktop --format pdf --threshold 100

2. 命令行 （必须通过 C 方案安装）
zhihuer --id 345516318,339771266 --destination ~/Desktop --format pdf --threshold 100
```