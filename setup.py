from setuptools import setup, find_packages

setup(
    name='unrotate_netcdf',
    version='0.1',
    description='Convert rotated-pole netCDF file to regular lat/lon',
    author='Jonas Solvsteen',
    author_email='josl@dhigroup.com',
    packages=find_packages(),
    entry_points="""
    [console_scripts]
    unrotate_netcdf=unrotate_netcdf.scripts.unrotate_netcdf:main
    """,
    install_requires=[
        'xarray'],
    )
