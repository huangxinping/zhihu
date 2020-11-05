import os
from setuptools import setup
import zhihuer


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(name='zhihuer',
      version=zhihuer.__version__,
      packages=['zhihuer'],
      author='monor.huang',
      author_email='monor.huang@gmail.com',
      url='https://github.com/huangxinping/zhihuer',
      description='爬取知乎问题回答并合并到单个文件。',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      license='MIT',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3 :: Only'
      ],
      keywords='zhihu question answer html pdf',
      install_requires=[
          'pdfkit',
          'fire',
          'tqdm',
          'lxml'
      ],
      entry_points={
          'console_scripts': [
              'zhihuer = zhihuer.cli:main'
          ]
      },
      )
