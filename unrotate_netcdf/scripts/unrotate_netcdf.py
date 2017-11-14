import click


@click.command()
@click.argument('infile', type=click.Path(file_okay=True))
@click.option('--outfile', '-o', help='Output file (default: overwrite infile)')
def main(infile, outfile=None):
    """Convert rotated-pole netCDF to regular lat/lon CF-1.7"""
    from unrotate_netcdf import unrotate_netcdf
    if outfile is None:
        outfile = infile
    unrotate_netcdf(infile, outfile)
