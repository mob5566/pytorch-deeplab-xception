import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='deeplab',
    author='jfzhang95',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # url='https://github.com/mapbox/robosat',
    packages=setuptools.find_packages(),
)
