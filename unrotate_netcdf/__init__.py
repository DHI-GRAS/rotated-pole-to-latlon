import xarray as xr

LATLON_ATTRIBUTES = {
    'lat': {
        'standard_name': 'latitude',
        'long_name': 'latitude',
        'units': 'degrees_north'},
    'lon': {
        'standard_name': 'longitude',
        'long_name': 'longitude',
        'units': 'degrees_east'}}

TO_RENAME = {
    'rlat': 'lat',
    'rlon': 'lon'}


def unrotate_ds(ds):
    """Convert Dataset from roated-pole (lon only) to regular lat/lon"""
    rp = ds['rotated_pole']
    assert rp.attrs['grid_mapping_name'] == 'rotated_latitude_longitude'
    assert rp.attrs['grid_north_pole_latitude'] == 90
    lon_offset = rp.attrs['grid_north_pole_longitude']

    dsnew = ds.rename(TO_RENAME).drop('rotated_pole')

    dsnew['lon'] += lon_offset

    for da in dsnew.data_vars.values():
        da.attrs.pop('grid_mapping')

    for varn in ['lat', 'lon']:
        dsnew[varn].attrs = LATLON_ATTRIBUTES[varn]

    dsnew.attrs = {'Conventions': 'CF-1.7'}
    return dsnew


def unrotate_netcdf(infile, outfile):
    """Convert netCDF file from roated-pole (lon only) to regular lat/lon"""
    ds = xr.open_dataset(infile)
    dsnew = unrotate_ds(ds)
    dsnew.to_netcdf(outfile)
