import xarray as xr

# open your file (replace with your file path)
ds = xr.open_dataset("cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m_1773814566818.nc")

print(ds["uo"].values)
print(ds["vo"].values)  # see all variables