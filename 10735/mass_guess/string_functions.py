import os
import numpy as np
from astropy.table import Table, vstack



band_names = ["#id", "nircam_f115w_flux", "nircam_f115w_fluxerr", 'nircam_f150w_flux', "nircam_f150w_fluxerr",
              'nircam_f200w_flux', "nircam_f200w_fluxerr",'nircam_f277w_flux', "nircam_f277w_fluxerr",
              'nircam_f356w_flux', "nircam_f356w_fluxerr",'nircam_f410m_flux', "nircam_f410m_fluxerr",
              'nircam_f444w_flux', "nircam_f444w_fluxerr"]



# Normalize column name for internal use

internal_band_names = band_names[:]
if internal_band_names[0] == "#id":
    internal_band_names[0] = "id"

def read_or_init_table(path, colnames):
    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        return Table(names=colnames)
    try:
        tb = Table.read(path, format="ascii.commented_header")
    except Exception:
        tb = Table(names=colnames)
    if len(tb) == 0:
        tb = Table(names=colnames)
    if "#id" in tb.colnames and "id" not in tb.colnames:
        tb.rename_column("#id", "id")
    for col in colnames:
        if col not in tb.colnames:
            tb[col] = np.nan
    if set(tb.colnames) != set(colnames):
        tb = tb[colnames]
    return tb

def coerce_id(value):
    if value is None:
        return -1
    text = str(value).strip()
    if text == "" or text.lower() == "nan":
        return -1
    return int(float(text))


def store_flux_err_tocat(output_name, idx_name,cat_content):

    existing_tb = read_or_init_table(output_name, internal_band_names)

    name_lrd_int = coerce_id(idx_name)
    ids = np.array([coerce_id(v) for v in existing_tb["id"]], dtype=int)

    if len(cat_content) != len(internal_band_names) - 1:
        raise ValueError(f"content length {len(cat_content)} != {len(internal_band_names) - 1}")

    row_values = [name_lrd_int] + cat_content

    match = np.where(ids == name_lrd_int)[0]
    if match.size > 0:
        row_idx = match[0]
        for col, val in zip(internal_band_names, row_values):
            existing_tb[col][row_idx] = val
        final_tb = existing_tb
        print("content is duplicated, replace the old one.")
    else:
        new_row = Table(rows=[row_values], names=internal_band_names)
        final_tb = vstack([existing_tb, new_row], metadata_conflicts="silent")
        print(f"new stack a row {name_lrd_int}")

    final_tb["id"] = np.array([coerce_id(v) for v in final_tb["id"]], dtype=int)
    final_tb.write(output_name, format="ascii.commented_header", overwrite=True)