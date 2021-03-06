# 爬取知乎问题所有回答，并合并为单个 HTML 或 PDF 文件

## 环境

> Python 3.6+    
> Linux、Unix，不支持 Windows    
> wkhtmltopdf - 如果需要导出为 PDF 则需要安装 (https://wkhtmltopdf.org/downloads.html)

## 安装

> 1. git clone https://github.com/huangxinping/zhihu.git    
> 2. cd zhihu && python setup.py sdist && cd dist && tar xzf zhihuer-0.0.1.tar.gz && cd zhihuer-0.0.1 && python setup.py install      
> 3. reopen terminal

## 使用

> zhihuer -i, --id: 支持多个ID，多个ID通过','分割         
>         -d, --destination: 默认是桌面（测试环境：Mac OS）         
>         -f, --format: html或pdf，默认为 html     
>         -t, --threshold：阈值，低于该阈值的点赞数回答则过滤，默认为 10 

## 例子

##### 假设需要爬取：https://www.zhihu.com/question/345516318 和 https://www.zhihu.com/question/339771266

```
zhihuer --id 345516318,339771266 --destination ~/Desktop --format pdf --threshold 100
```

##### 爬取(https://www.zhihu.com/question/345516318)结果部分截图展示

![研究生们刚开始看英文文献是怎么看的？](docs/1.png)
