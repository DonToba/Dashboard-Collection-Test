import geopandas as gpd


def merge_data(building_file, kobo_df):

    buildings = gpd.read_file(building_file)

    buildings["Build_ID"] = buildings["Build_ID"].astype(str)
    kobo_df["Build_ID"] = kobo_df["Build_ID"].astype(str)

    merged = buildings.merge(
        kobo_df,
        on="Build_ID",
        how="left"
    )

    return merged
