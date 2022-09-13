from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='MultiTrain',
    version='1.0.1',
    packages=['MultiTrain', 'MultiTrain.tests', 'MultiTrain.methods', 'MultiTrain.regression',
              'MultiTrain.classification'],
    url='',
    license='MIT License',
    author='Shittu Samson',
    author_email='tunexo885@gmail.com',
    description='Train all models at once',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                ],
    python_requires='>=3.6',
    install_requires=['matplotlib~=3.5.3',
                      'numpy~=1.23.3',
                      'pandas~=1.4.4',
                      'plotly~=5.10.0',
                      'scikit-learn~=1.1.2',
                      'xgboost~=1.6.2',
                      'catboost~=1.0.6',
                      'imbalanced-learn~=0.9.1',
                      'seaborn~=0.12.0',
                      'lightgbm~=3.3.2',
                      'scikit-optimize~=0.9.0']
)
