from setuptools import setup, find_packages

setup(
        name='dotties',
        version='1.0',
        packages=find_packages(),
        license='Unlicense',
        url='https://github.com/tinytacoteam/dotties-core.py',
        description='Dotties is a Mac tool for managing your dotfiles via GitHub.',
        install_requires=[
            'click >= 6.6',
        ],
        entry_points='''
            [console_scripts]
            dotties=dotties.main:cli
        ''',
        )
