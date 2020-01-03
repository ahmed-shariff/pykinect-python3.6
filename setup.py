import setuptools

# to build and install:
# python setup.py
# pip install dist/mlpipeline-*-py3-none-any.whl

setuptools.setup(
    name="pykinect",
    version="0.1.aplpha.1",
    author='Ahmed Shariff',
    author_email='shariff.mfa@outlook.com',
    packages=setuptools.find_packages(),
    description='pykinect port from microsoft',
    # long_description=open('README.rst').read(),
    # long_description_content_type='text/markdown',
    url='https://github.com/ahmed-shariff/pykinect-python3.6',
    # install_requires=['easydict>=1.8', 'mlflow>=1.0.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ]
)
