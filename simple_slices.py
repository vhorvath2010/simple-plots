import yt

# Load the dataset
ds = yt.load("local-data\sloshing_nomag2_hdf5_plt_cnt_0150")

# Create slice plots of gas density in the 3 axes
x_plot = yt.SlicePlot(ds, "x", ("gas", "density"), width=(800.0, "kpc")).save()
y_plot = yt.SlicePlot(ds, "y", ("gas", "density"), width=(800.0, "kpc")).save()
z_plot = yt.SlicePlot(ds, "z", ("gas", "density"), width=(800.0, "kpc")).save()