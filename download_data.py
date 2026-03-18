import copernicusmarine

copernicusmarine.subset(
  dataset_id="cmems_obs-mob_glo_phy-cur_my_0.25deg_P1D-m",
  variables=["ue", "ugos", "uo", "utide", "ve", "vgos", "vo", "vtide"],
  minimum_longitude=-179.875,
  maximum_longitude=179.875,
  minimum_latitude=-89.875,
  maximum_latitude=89.875,
  start_datetime="2020-12-31T00:00:00",
  end_datetime="2023-12-31T00:00:00",
  minimum_depth=0,
  maximum_depth=0,
)

""" 
In your dataset, uo and vo refer to the zonal and meridional components of ocean currents:

🔹 uo (Zonal velocity) → The east-west movement of water.

Positive = Water moving eastward.

Negative = Water moving westward.

🔹 vo (Meridional velocity) → The north-south movement of water.

Positive = Water moving northward.

Negative = Water moving southward.

"""