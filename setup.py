from setuptools import setup, find_packages

setup(
    name='nous.pofilter',
    version='0.2',
    description='Customized runner for pofilter.',
    author='Ignas Mikalajunas',
    author_email='ignas@nous.lt',
    url='http://github.com/Ignas/nous.pofilter/',
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: GNU General Public License (GPL)",
                 "Programming Language :: Python"],
    install_requires=[
        "translate-toolkit",
        ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    namespace_packages=['nous'],
    zip_safe=False,
    license="GPL",
    entry_points="""
    [console_scripts]
    pofilter = nous.pofilter:main
    """,
)
