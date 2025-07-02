from setuptools import setup, find_packages

setup(
    name='wikidata-mak-integration',
    version='1.0.0',
    author='Kim Becker, Pablo Trutnau',
    author_email='',
    description='Enrichment and integration of MAK Collection publication metadata into Wikidata.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ptrutnau/Dis18-Gruppe6',
    license='BSD-3-Clause',
    packages=find_packages(where='Scripts'),
    package_dir={'': 'Scripts'},
    include_package_data=True,
    install_requires=[
        'requests',
        'pandas',
        'pywikibot',
        'tqdm'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    python_requires='>=3.8',
)
