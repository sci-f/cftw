# ContainersFTW Competition

This is a containersFTW competition container base! Here is how to get started.

## File Organization
 - Any data that you want to package in the container, put it [data](data). It will be copied to `/data/input` in the container. For larger datasets that need to be downloaded/cloned, you can do this in the `%post` section of the [Singularity](Singularity) file.
 - Any helper scripts for your competitors (eg, reading in data and validating output) should be put in [analysis/helpers](analysis/helpers). You can provide examples for the user in the application [analysis/main.py](analysis/main.py)


 - Provide tests for the user under [analysis/tests]. This can be validation of output, or even code. You should 

## Labels
The [Singularity](Singularity) file has a section for `%labels`. You should replace the `COMPETITION_HOST` label with your name.


```
CONTAINERSFTW_COMPETITION_HOST containersftw
```
