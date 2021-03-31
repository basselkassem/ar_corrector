from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
setup(
    name='ar_corrector',  # Required
     packages=['ar_corrector'],
    version='v1.0.6-alpha',  # Required
    description='Arabic Spelling Correction',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    download_url = 'https://github.com/basselkassem/ar_corrector/archive/refs/tags/v1.0.0-alpha.tar.gz', 
    author='Bassel Kassem',  # Optional
    author_email='bassel.kassem.job@gmail.com',  # Optional
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='NLP, Spellingcheck',  # Optional
    python_requires='>=3.6, <4',
    install_requires=['requests'],  # Optional
    package_data={  # Optional
        '': ['resources/*.pickle'],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/basselkassem/ar_corrector/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'https://github.com/basselkassem',
        'Source': 'https://github.com/basselkassem/ar_corrector',
    },
)