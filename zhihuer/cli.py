import sys
import argparse
import os
import re
import zhihuer
from zhihuer.app import main as converter


def main():
    parser = argparse.ArgumentParser(description='Zhihuer Worker', add_help=False)

    parser.add_argument('-i', '--id', action='store', help='问题ID，多个用","分割')
    parser.add_argument('-d', '--destination', action='store', default=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop'), help='文件保存位置')
    parser.add_argument('-f', '--format', action='store', default='html', help='文件输出类型(html/pdf)')
    parser.add_argument('-t', '--threshold', action='store', default=10, type=int, help='点赞数阈值，低于该阈值的会过滤')

    parser.add_argument('-v', '--version', action='store_true', help='版本信息')
    parser.add_argument('-h', '--help', action='store_true', help='帮助')

    args = parser.parse_args()

    if args.help:
        parser.print_help()
        sys.exit(0)
    if args.version:
        print(zhihuer.__version__)
        sys.exit(0)

    if args.id is None:
        print('请输入ID！')
        sys.exit(0)

    if len(os.popen('which zhihu').read()) < 1:
        os.system(f'pip install git+https://hub.fastgit.org/huangxinping/ZhihuSpider.git')

    ids = list()

    if args.id is not None:
        ids.extend(re.split(r'[\s,]+', args.id))
    for id in ids:
        converter(id, args.destination, args.format, args.threshold)
    sys.exit(0)


if __name__ == '__main__':
    sys.argv = ['zhihuer',
                '-u', '345516318,339771266',
                '-f', 'pdf',
                '-d', f"{os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')}",
                '-t', 10]
    main()
