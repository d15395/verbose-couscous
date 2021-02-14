#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.config import read_configuration

#Please update this section
project_name = '<Fill the package name>'
project_description = '<Fill the package description>'
project_url = '<Fill the project URL>'

author_name = '<Fill your name>'
author_email = '<Fill your email>'

package_name = '<Package name>'
# src path. Do not include src/ in the path. That is already handled.
package_src_path = '<Package src path>'

setup(name=project_name,
      version='1.0',
      description=project_description,
      author=author_name,
      author_email=author_email,
      url=project_url,
      packages=find_packages(),
      package_dir={package_name: f"src/{package_src_path}"},
      test_suite='tests'
     )