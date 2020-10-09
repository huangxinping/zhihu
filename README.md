# 爬取知乎问题所有回答合并到单一 HTML 文件中

# 环境

> Python 3.6+    
> Linux、Unix，不支持 Windows

## 安装依赖
> 1. 安装 ZhihuSpider 库     
    源码下载：git clone https://github.com/huangxinping/ZhihuSpider.git    
    编译及安装：python setup.py install && pip install .
> 2. 安装另外一些第三方库    
    pip install pdfkit fire tqdm
> 3. 开始用吧    
    python app.py --id {question_id} --save_dir {path}    
    -- save_dir: 默认是桌面


## 例子
```
python app.py --id 345516318
```