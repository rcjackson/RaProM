# ImproveProcessRawMRR - RaProM.py

RaProM is a MRR processing methodology, with enhanced spectra processing and Doppler dealiasing, that produces as output data a number of fields which include equivalent reflectivity (Ze), Doppler fall speed and derived parameters such as spectral width, skewness, and kurtosis, plus a simplified precipitation hydrometeor type classification (drizzle, rain, mixed, snow, and hail), and additional variables depending on the precipitation hydrometeor type. MRR stands for Micro Rain Radar, a Doppler vertically pointing radar manufactured by Metek GmbH. A description of the RaProM processing and examples is available at: <br/>
Garcia-Benadi A, Bech J, Gonzalez S, Udina M, Codina B, Georgis J-F. Precipitation Type Classification of Micro Rain Radar Data Using an Improved Doppler Spectral Processing Methodology. Remote Sens. 2020, 12, 4113. https://doi.org/10.3390/rs12244113<br/><br/>
**Note1: the scripts are designed to work with MRR-2.**<br/><br/>
**Note2: a different version similar to RaProM, called RaProM-Pro (https://github.com/AlbertGBena/RaProM-Pro), is available for MRR-Pro files. More information on RaProM-Pro is available at: <br/>
Garcia-Benadí A, Bech J, Gonzalez S, Udina M, Codina B. A New Methodology to Characterise the Radar Bright Band Using Doppler Spectral Moments from Vertically Pointing Radar Observations. Remote Sens. 2021, 13, 4323. https://doi.org/10.3390/rs13214323**<br/><br/>

An additional Python script CorrecRawFile is also included. If you know that your raw file has writing  errors (temporal inconsistencies), please execute this file before RaProM. You can execute this file from the command window or idle.

More information at: Garcia-Benadí et al (2020)
https://doi.org/10.3390/rs12244113

## Versions and dependences

The main script is called RaProM_3-11.py and requires Python 3.11 or later. The following libraries are necessary:

	numpy , version 1.21.6

	miepython, version 2.2.1 (matplotlib is necessary for this library works)

	netCDF4, version 1.7.2 or later(cftime is necessary for this library works)


The script works with the MRR raw archives.

The libraries can be installed with pip, using these sentences:

	pip install numpy
	pip install miepython
	pip install netCDF4
	pip install matplotlib
	pip install cftime

If you have already installed one of the libraries but need to change the version, you can use this syntaxis:

	pip install numpy~=1.21.6

## How to cite

If you use this script for your publication, please cite as:

Garcia-Benadi A, Bech J, Gonzalez S, Udina M, Codina B, Georgis J-F. Precipitation Type Classification of Micro Rain Radar Data Using an Improved Doppler Spectral Processing Methodology. Remote Sens. 2020, 12, 4113.DOI: 10.3390/rs12244113  

## Outputs
The script produces the following outputs from MRR raw data:<br />
**W:** Fall speed with aliasing correction (m s<sup>-1</sup>)<br />
**spectral width:** Spectral width of the dealiased velocity distribution (m s<sup>-1</sup>)<br />
**skewness:** Skewness of the dealiased velocity distribution<br />
**kurtosis:** Kurtosis of the dealiased velocity distribution<br />
**PIA:** Path Integrated Attenuation calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**PIA_all:** Path Integrated Attenuation calculated assuming all hydrometeors are in liquid phase regardless of hydrometeor type classification<br />
**Type:** Predominant hydrometeor type numerical value where possible values are: -20 (hail), -15 (mixed), -10 (snow), 0 (mixed), 5 (drizzle), 10 (rain) and 20 (unknown precipitation)<br />
**LWC:** Liquid Water Content (g m<sup>-3</sup>) calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**RR:** Rain Rate (mm h<sup>-1</sup>) calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**SR:** Snow Rate (mm h<sup>-1</sup>)<br />
**Z:** Radar reflectivity (dBZ) calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**Za:** Attenuated radar reflectivity (dBZ) calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**Ze:** Equivalent radar reflectivity (dBZ)<br />
**N(D):** Drop Size Distribution (log10(m<sup>-3</sup> mm<sup>-1</sup>)) calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**N(D) in_function_of_time_and_height** Drop Size Distribution (log10(m<sup>-3</sup> mm<sup>-1</sup>)) in function of time and height calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**SNR:** Signal to noise ratio from signal without dealiasing (dB)<br />
**Noise:** Noise from spectra reflectivity  (m<sup>-1</sup>)<br />
**N<sub>w</sub>:** Intercept of the gamma distribution normalized to the Liquid Water Content (log10(m<sup>-3</sup> mm<sup>-1</sup>)) calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**D<sub>m</sub>:** Mean mass-weighted raindrop diameter (mm) calculated using only liquid hydrometeors according to hydrometeor type classification<br />
**BB<sub>bottom</sub>:** Bright Band bottom height  (m) (above ground level)<br />
**BB<sub>top</sub>:** Bright Band top height (m) (above ground level)<br />
**TyPrecipi:** Precipitation regime numerical value where possible values are: 5 (convective), 0 (transition) and -5 (stratiform) calculated using only liquid hydrometeors according to hydrometeor type classification<br />
<br />
Notice that PIA and PIA_all have 1 height bin more, because the first element is at 0 m height a.g.l. imposed by the manufacturer

## How to execute the script
The script is run from a command line. The path to the data is passed as an argument; it can be either a directory of `.raw` files (all of them are processed) or a single `.raw` file.

```
python RaProM_3-11.py PATH [-t SECONDS] [-h<meters>] [-M<value>]
```

Arguments:

| Argument | Meaning |
| --- | --- |
| `PATH` | Directory of `.raw` files **or** a single `.raw` file. Required. |
| `-t SECONDS` | Integration time in seconds. Default: `60`. Also accepts `-t60` (no space) and `--integration-time 60`. |
| `-h<meters>` | Override the MRR antenna height (above sea level) when it was not configured correctly in the raw file. Float or integer, e.g. `-h100.8`. |
| `-M<value>` | Multiplicative bias for the MRR calibration constant. Affects Z, RR, and other derived variables. `M = RR_MRR / RR_REF`, typically close to 1. Float or integer, e.g. `-M0.78`. |
| `--help`, `-?` | Print the usage message and exit. |

Examples:

Process every raw file in a directory with the default 60 s integration time:
```
python RaProM_3-11.py /path/to/mrrdata/
```

Process a single raw file:
```
python RaProM_3-11.py /path/to/mrrdata/0520.raw
```

Override the antenna height and use a 30 s integration time:
```
python RaProM_3-11.py /path/to/mrrdata/ -t 30 -h100.8
```

Apply a calibration bias of 0.78:
```
python RaProM_3-11.py /path/to/mrrdata/ -M0.78
```

For each input file, the result is written to a netCDF file in the same directory with the suffix `-processed.nc` (e.g. `0520.raw` → `0520-processed.nc`).

**NOTE:** Avoid using spaces and special characters in your file path.

If `PATH` is omitted, the script falls back to the older interactive prompts (asks for the directory and the integration time). New code should prefer the CLI form above.

You can also invoke the module form:
```
python -m raprom /path/to/mrrdata/
```

## Using from a notebook or another Python script
The processing is exposed as plain Python functions in the `raprom` module, so it can be driven from a Jupyter notebook or another script:

```python
import raprom

# Process one file. Returns the absolute path of the produced netCDF.
out = raprom.process_file('/path/to/0520.raw',
                          integration_time=60,   # default 60
                          height=None,           # None → use value from raw
                          calibration=1.0,       # M, default 1.0
                          verbose=False)         # silence the spinner

# Process every .raw file in a directory. Returns a list of paths.
outs = raprom.process_directory('/path/to/mrrdata/', verbose=False)

# Open the result with xarray (or netCDF4) for analysis.
import xarray as xr
ds = xr.open_dataset(out)
```

The CLI shim (`python RaProM_3-11.py ...`) and `python -m raprom ...` both call `raprom.main()` internally, so all three entry points share the same argument handling.

## Do you have any problem with your data?
If so, your RAW files may be corrupted. There is a new script for this called CorrecRawFiles-py_3-11.py .
This script analyses every line in the original RAW file and fixes it. If errors are found, a new file with 
the same name but finished as -corrected will be created.
To execute the script follow the same steps described above.

## Contact
If you have any question, please contact with Albert at albert.garcia@meteo.ub.edu  or   albert.garcia-benadi@upc.edu
