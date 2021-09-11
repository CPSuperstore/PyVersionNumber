import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name='PyVersionNumber',
    packages=['PyVersionNumber'],
    version='1.1.1',
    license='MIT',
    description='A small library for handling and comparing Semantic Version Numbers',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='CPSuperstore',
    author_email='cpsuperstoreinc@gmail.com',
    url='https://github.com/CPSuperstore/PyVersionNumber',
    project_urls={
        "Bug Tracker": "https://github.com/CPSuperstore/PyVersionNumber/issues",
    },
    download_url='https://github.com/CPSuperstore/PyVersionNumber/archive/refs/tags/v1.1.1.tar.gz',
    keywords=['SEMANTIC', 'VERSION', 'NUMBER', 'VERSIONING', 'MAJOR', 'MINOR', 'PATCH'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'Topic :: Documentation',
        'Topic :: Software Development :: Version Control',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English'
    ],
)
