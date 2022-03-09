from setuptools import setup

with open('README.md') as f:
    readme = f.read()

version = "1.0.0"

setup(
  name="Py2JVM",
  version=version,
  description="Python to Java compiler/transpiler with the aim to work across multiple versions!",
  long_description=readme,
  long_description_content_type="text/markdown",
  keywords=['python', 'java', 'transpiler', 'compiler', 'py2jvm'],
  author="Forest&",
  include_package_data=True,
  classifiers=[
  'Programming Language :: Python',
  'Programming Language :: Python :: 3.10',
  'Programming Language :: Python :: Implementation :: CPython'
  ]
)
