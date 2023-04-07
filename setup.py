from os import path, makedirs
from setuptools import setup, find_packages


# Load readme
with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()


# Write default template in Home directory
with open('hapdoc/templates/vitepress/index.html', 'r', encoding='utf-8') as file:
    default_template = file.read()
directory = path.join(path.expanduser('~'), 'HapticX', 'hapdoc', 'templates', 'default')
if not path.exists(directory):
    makedirs(directory)
with open(path.join(directory, 'index.html'), 'w', encoding='utf-8') as file:
    file.write(default_template)


setup(
    name='rpg_core',
    description='old-school text RPG core',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ethosa',
    author_email='social.ethosa@gmail.com',
    maintainer='HapticX',
    maintainer_email='hapticx.company@gmail.com',
    url='https://github.com/HapticX/rpg-core-py',
    version='0.0.1',
    packages=find_packages(),
    py_modules=['rpg_core'],
    install_requires=[],
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Framework :: FastAPI',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation'
    ]
)