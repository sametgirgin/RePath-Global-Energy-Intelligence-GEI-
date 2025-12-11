from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st


st.set_page_config(page_title="RePath Global Energy Intelligence (GEI)", layout="wide")

DATA_FILE = Path(__file__).resolve().parent / "energystats.xlsx"
EXAJOULE_MD = Path(__file__).resolve().parent / "exajoule.md"
CARBON_MD = Path(__file__).resolve().parent / "carbon.md"
OIL_MD = Path(__file__).resolve().parent / "oil.md"
GAS_MD = Path(__file__).resolve().parent / "gas.md"
COAL_MD = Path(__file__).resolve().parent / "coal.md"
NUCLEAR_MD = Path(__file__).resolve().parent / "nuclear.md"
MINERAL_MD = Path(__file__).resolve().parent / "mineral.md"
PROJECT_MD = Path(__file__).resolve().parent / "project.md"
LOGO_FILE = Path(__file__).resolve().parent / "logo.png"

# Emissions dataset configuration: sheet name and value label for charts.
EMISSIONS_SERIES = [
    ("Carbon: Carbon Dioxide Emissions from Energy (from 1965)", "CO2 from Energy", "Emissions (MtCO2)"),
    ("Natural Gas Flaring (from 1975)", "Natural Gas Flaring", "Flaring (Bcm)"),
    ("Carbon: Carbon Dioxide Emissions from Flaring (from 1975)", "CO2 from Flaring", "Emissions from flaring (MtCO2)"),
    ("Carbon: Carbon Dioxide Equivalent Emissions from Methane and Process Emissions (from 1990)", "CO2-Process Emissions, Methane ", "Emissions (MtCO2e)"),
    ("Carbon: Carbon Dioxide Equivalent Emissions from Energy, Process Emissions, Methane, and Flaring (from 1990)", "CO2e Emissions ", "Emissions (MtCO2e)"),
    ("Carbon: Carbon Capture, Usage, and Storage (CCUS) (from 2000)", "CCUS Capture Capacity", "Capture capacity (Mt/yr)"),
]

OIL_SERIES = [
    ("Oil: Proved reserves - Barrels (from 1990)", "Oil - Proved reserves history", "Proved reserves (billion bbl)", "entity_year"),
    ("Oil: Production - Barrels (from 1965)", "Oil Production - barrels", "Production (thousand bbl/day)", "entity_year"),
    ("Oil: Production - Tonnes (from 1965)", "Oil Production - tonnes", "Production (million tonnes)", "entity_year"),
    ("Oil: Crude oil and condensate production - Barrels (from 2000)", "Crude+cond production - barrels", "Production (thousand bbl/day)", "entity_year"),
    ("Oil: Natural Gas Liquids production - Barrels (from 2000)", "NGLs production - barrels", "NGL production (thousand bbl/day)", "entity_year"),
    ("Oil: Total liquids consumption - Barrels (from 1965)", "Liquids Consumption - barrels", "Consumption (thousand bbl/day)", "entity_year"),
    ("Oil: Consumption - Barrels (from 1965)", "Oil Consumption - barrels", "Consumption (thousand bbl/day)", "entity_year"),
    ("Oil: Consumption - Tonnes (from 1965)", "Oil Consumption - Tonnes", "Consumption (million tonnes)", "entity_year"),
    ("Oil: Consumption - Exajoules (from 1965)", "Oil Consumption - EJ", "Consumption (EJ)", "entity_year"),
    ("Oil: Refinery throughput (from 1980)", "Oil refinery - throughput", "Throughput (thousand bbl/day)", "entity_year"),
    ("Oil: Refining capacity (from 1965)", "Oil refinery - capacity", "Refining capacity (thousand bbl/day)", "entity_year"),
    ("Oil: Trade movements-Imports", "Oil trade movements-Imports", "Imports (thousand bbl/day)", "entity_year"),
    ("Oil: Trade movements- Exports", "Oil trade movements-Exports", "Exports (thousand bbl/day)", "entity_year"),
]

OIL_PRICE_SERIES = [
    ("Oil: Spot crude prices", "Spot crude prices"),
    ("Oil: Crude prices (from 1861)", "Oil crude prices since 1861"),
    ("Oil: Regional refining margins (from 2000)", "Oil - Regional refining margins"),
]

OIL_FLOW_TABLES = [
    ("Oil: Inter-area movements (for 2024)", "Oil - Inter-area movements", "Crude flows (million tonnes)"),
    ("Product - Inter-area movements (for 2024)", "Product - Inter-area movements ", "Product flows (million tonnes)"),
]

GAS_SERIES = [
    ("Gas: Proved reserves - Bcm (from 1980)", "Gas - Proved reserves history", "Proved reserves (tcm)", "entity_year"),
    ("Gas: Production - Bcm (from 1970)", "Gas Production - Bcm", "Production (bcm)", "entity_year"),
    ("Gas: Production - Bcf (from 1970)", "Gas Production - bcf", "Production (bcf/day)", "entity_year_header1"),
    ("Gas: Production - Exajoules (from 1970)", "Gas Production - EJ", "Production (EJ)", "entity_year"),
    ("Gas: Consumption - Bcm (from 1965)", "Gas Consumption - Bcm", "Consumption (bcm)", "entity_year"),
    ("Gas: Consumption - Bcf (from 1965)", "Gas Consumption - Bcf", "Consumption (bcf/day)", "entity_year"),
    ("Gas: Consumption - Exajoules (from 1965)", "Gas Consumption - EJ", "Consumption (EJ)", "entity_year"),
    ("Gas: Hydrogen Production Capacity (from 2000)", "Gas - H2 Production Capacity", "H2 capacity (kT/yr)", "entity_source_year"),
    ("Gas: LNG imports (from 2000)", "Gas - LNG imports bcm", "LNG imports (bcm)", "entity_year"),
    ("Gas: LNG exports (from 2000)", "Gas - LNG exports bcm", "LNG exports (bcm)", "entity_year"),
]

GAS_PRICE_SERIES = [
    ("LNG prices US dollars per MBTU", "LNG Prices US dollars per MBTU"),
    ("Natural Gas US Dollars per MBTU", "Natural Gas US Dollars MBTU"),
    ("Hydrogen dolar per kg", "Hydrogen dolar per kg"),
    ("Amonia $ per mt", "Amonia $ per mt"),
]

GAS_FLOW_TABLES = [
    ("Gas: Trade movements LNG (for 2024)", "Gas trade 2024 - LNG", "LNG trade (bcm)"),
    ("Gas: Trade movements pipeline (for 2024)", "Gas trade 2024 - pipeline", "Pipeline trade (bcm)"),
]

COAL_SERIES = [
    ("Coal: Production - Tonnes (from 1981)", "Coal Production - mt", "Production (million tonnes)", "entity_year"),
    ("Coal: Production - Exajoules (from 1981)", "Coal Production - EJ", "Production (EJ)", "entity_year"),
    ("Coal: Consumption - Exajoules (from 1965)", "Coal Consumption - EJ", "Consumption (EJ)", "entity_year"),
    ("Coal: Import Trade movements (from 2000)", "Coal - Import Trade movements ", "Imports (EJ)", "entity_year"),
    ("Coal: Export Trade movements (from 2000)", "Coal - Export Trade movements", "Exports (EJ)", "entity_year"),
]

COAL_PRICE_SERIES = [
    ("Coal: Mined energy resource & Uranium prices (from 1987)", "Coal & Uranium - Prices"),
]

COAL_FLOW_TABLES = [
    ("Coal: Inter-area movements (for 2024)", "Coal trade movements 2024", "Coal trade (EJ)"),
]

NUCLEAR_SERIES = [
    ("Nuclear Energy - Generation - TWh (from 1965)", "Nuclear Generation - TWh", "Generation (TWh)", "entity_year"),
    ("Nuclear Energy - Consumption - Exajoules (from 1965)", "Nuclear Consumption - EJ", "Consumption (EJ)", "entity_year"),
]

HYDRO_SERIES = [
    ("Hydroelectricity - Generation - TWh (from 1965)", "Hydro Generation - TWh", "Generation (TWh)", "entity_year"),
    ("Hydroelectricity - Consumption - Exajoules (from 1965)", "Hydro Consumption - EJ", "Consumption (EJ)", "entity_year"),
]

RENEWABLE_SERIES = [
    ("Renewables - Combined renewable electricity and biofuels total energy supply - Exajoules (from 1965)", "Renewables Consumption -EJ", "Consumption (EJ)", "entity_year_int"),
    ("Renewables - Renewable Power Total Energy Input (inc hydro)- Exajoules (from 1965)", "Renewable Power (inc hydro) -EJ", "Energy input (EJ)", "entity_year_int"),
    ("Renewables - Renewable Power Total Energy Input (exc hydro) - Exajoules (from 1965)", "Ren power (excl hydro) - EJ", "Energy input excl hydro (EJ)", "entity_year_int"),
    ("Renewables - Renewable Power  (inc hydro) - TWh (from 1965)", "Renewable Power (inc hydro)-TWh", "Generation (TWh)", "entity_year_int"),
    ("Renewables - Renewable Power (exc hydro) - TWh (from 1965)", "Ren power (excl hydro) - TWh", "Generation excl hydro (TWh)", "entity_year_int"),
    ("Renewables - Solar generation - TWh (from 1965)", "Solar Generation - TWh", "Solar generation (TWh)", "entity_year_int"),
    ("Renewables - Solar consumption - Exajoules (from 1965)", "Solar Consumption - EJ", "Solar consumption (EJ)", "entity_year_int"),
    ("Renewable Energy - Solar (Installed capacity)", "Solar Installed Capacity", "Solar capacity (MW)", "entity_year_int"),
    ("Renewables - Wind generation - TWh (from 1965)", "Wind Generation - TWh", "Wind generation (TWh)", "entity_year_int"),
    ("Renewables - Wind consumption - Exajoules (from 1965)", "Wind Consumption - EJ", "Wind consumption (EJ)", "entity_year_int"),
    ("Renewable Energy - Wind  (Installed capacity)", "Wind Installed Capacity", "Wind capacity (MW)", "entity_year_int"),
    ("Renewables - Geothermal, Biomass and Other generation - TWh  (from 1965)", "Geo Biomass Other - TWh", "Other generation (TWh)", "entity_year_int"),
    ("Renewables - Geothermal, Biomass and Other - Exajoules (from 1965)", "Geo Biomass Other - EJ", "Other consumption (EJ)", "entity_year_int"),
    ("Renewables - Biofuels production - Kboe/d (from 1990)", "Biofuels production - kboed", "Biofuels production (kboe/d)", "entity_year_int"),
    ("Renewables - Biofuels consumption - Kboe/d (from 1990)", "Biofuels Consumption - kboed", "Biofuels consumption (kboe/d)", "entity_year_int"),
]

ELECTRICITY_SERIES = [
    ("Electricity generation - TWh (from 1985)", "Electricity Generation - TWh", "Generation (TWh)", "entity_year_int"),
    ("Electricity generation from oil -TWh (from 1985)", "Oil inputs - Elec generation ", "Generation from oil (TWh)", "entity_year_int"),
    ("Electricity generation from gas - TWh (from 1985)", "Gas inputs - Elec generation", "Generation from gas (TWh)", "entity_year_int"),
    ("Electricity generation from coal - TWh (from 1985)", "Coal inputs - Elec generation ", "Generation from coal (TWh)", "entity_year_int"),
    ("Electricity generation from other - TWh (from 1985)", "Other inputs - Elec generation", "Generation from other (TWh)", "entity_year_int"),
    ("Electricity - Grid-Scale Battery Energy Storage Systems (BESS) (from 2013)", "Grid Scale BESS Capacity", "BESS capacity (GW)", "entity_year_int"),
]

MINERAL_SERIES = [
    ("Key materials - Cobalt Production - Reserves (from 1995)", "Cobalt P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Lithium Production - Reserves (from 1995)", "Lithium P-R", "Thousand tonnes of Lithium content", "entity_year_int"),
    ("Key materials - Graphite Production - Reserves (from 1995)", "Natural Graphite P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Rare Earth Production - Reserves (from 1995)", "Rare Earth metals P-R", "Thousand tonnes1", "entity_year_int"),
    ("Key materials - Copper Production - Reserves (from 2014)", "Copper P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Manganese Production - Reserves (from 2014)", "Manganese P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Nickel Production - Reserves (from 2014)", "Nickel P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Zinc Production - Reserves (from 2014)", "Zinc P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Platinum Group Metals Production - Reserves (from 2014)", "Platinum Group Metals P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Bauxite Production - Reserves (from 2014)", "Bauxite P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Aluminium Production - Capacity (from 2014)", "Aluminium P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Tin Production - Reserves (from 2014)", "Tin P-R", "Thousand tonnes", "entity_year_int"),
    ("Key materials - Vanadium Production - Reserves (from 2014)", "Vanadium P-R", "Thousand tonnes", "entity_year_int"),
]


@st.cache_data(show_spinner=False)
def load_tes_totals():
    """Load Total Energy Supply (EJ) data."""
    df = pd.read_excel(DATA_FILE, sheet_name="Total Energy Supply (TES) -EJ")
    df = df.rename(columns={df.columns[0]: "Country"})
    df = df[df["Country"].notna()]
    year_cols = [c for c in df.columns if isinstance(c, (int, float))]
    df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="Country", value_vars=year_cols, var_name="Year", value_name="TES_EJ")
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["TES_EJ", "Year"])
    return long


@st.cache_data(show_spinner=False)
def load_tes_per_capita():
    """Load TES per capita (GJ/person) data."""
    df = pd.read_excel(DATA_FILE, sheet_name="TES per Capita")
    df = df.rename(columns={df.columns[0]: "Country"})
    df = df[df["Country"].notna()]
    year_cols = [c for c in df.columns if isinstance(c, (int, float))]
    df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="Country", value_vars=year_cols, var_name="Year", value_name="TES_per_capita")
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["TES_per_capita", "Year"])
    return long


@st.cache_data(show_spinner=False)
def load_tes_by_fuel():
    """Load TES by fuel where columns are fuels and rows are countries."""
    df = pd.read_excel(DATA_FILE, sheet_name="TES by fuel")
    df = df.rename(columns={df.columns[0]: "Country"})
    df = df[df["Country"].notna()]
    fuel_cols = [c for c in df.columns if c != "Country"]
    df[fuel_cols] = df[fuel_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="Country", value_vars=fuel_cols, var_name="Fuel", value_name="Value")
    long = long.dropna(subset=["Value"])
    return long


@st.cache_data(show_spinner=False)
def load_exajoule_text() -> str:
    if not EXAJOULE_MD.exists():
        return ""
    return EXAJOULE_MD.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_carbon_text() -> str:
    if not CARBON_MD.exists():
        return ""
    return CARBON_MD.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_oil_text() -> str:
    if not OIL_MD.exists():
        return ""
    return OIL_MD.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_gas_text() -> str:
    if not GAS_MD.exists():
        return ""
    return GAS_MD.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_coal_text() -> str:
    if not COAL_MD.exists():
        return ""
    return COAL_MD.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_nuclear_text() -> str:
    if not NUCLEAR_MD.exists():
        return ""
    return NUCLEAR_MD.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_mineral_text() -> str:
    if not MINERAL_MD.exists():
        return ""
    return MINERAL_MD.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_project_text() -> str:
    if not PROJECT_MD.exists():
        return ""
    return PROJECT_MD.read_text(encoding="utf-8")


@st.cache_data(show_spinner=False)
def load_country_series(sheet_name: str, value_label: str):
    """Load country-time series where first column is country/region and remaining are years."""
    df = pd.read_excel(DATA_FILE, sheet_name=sheet_name)
    df = df.rename(columns={df.columns[0]: "Entity"})
    df = df[df["Entity"].notna()]
    year_cols = [c for c in df.columns if isinstance(c, (int, float))]
    df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="Entity", value_vars=year_cols, var_name="Year", value_name=value_label)
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["Year", value_label])
    return long


@st.cache_data(show_spinner=False)
def load_country_series_year_strings(sheet_name: str, value_label: str):
    """Load series where year information is embedded in column names (e.g., 'at end 2000')."""
    df = pd.read_excel(DATA_FILE, sheet_name=sheet_name)
    df = df.rename(columns={df.columns[0]: "Entity"})
    df = df[df["Entity"].notna()]
    year_map = {}
    for col in df.columns[1:]:
        year = pd.to_numeric(pd.Series([col]).astype(str).str.extract(r"(19\\d{2}|20\\d{2})")[0], errors="coerce").iloc[0]
        if pd.notna(year):
            year_map[col] = int(year)
    if not year_map:
        return pd.DataFrame(columns=["Entity", "Year", value_label])
    df = df[["Entity"] + list(year_map.keys())]
    df = df.rename(columns=year_map)
    numeric_cols = [c for c in df.columns if c != "Entity"]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="Entity", value_vars=numeric_cols, var_name="Year", value_name=value_label)
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["Year", value_label])
    return long


@st.cache_data(show_spinner=False)
def load_country_series_year_strings_skip(sheet_name: str, value_label: str, skip_rows: int):
    """Load year-string series that need top rows skipped before headers/data."""
    raw = pd.read_excel(DATA_FILE, sheet_name=sheet_name, header=None)
    data = raw.iloc[skip_rows:].reset_index(drop=True)
    # Keep first 5 columns (entity + up to four year columns).
    data = data.iloc[:, :5]
    data = data.rename(columns={0: "Entity"})
    data = data[data["Entity"].notna()]
    year_map = {}
    for col in data.columns[1:]:
        year = pd.to_numeric(pd.Series([col]).astype(str).str.extract(r"(19\\d{2}|20\\d{2})")[0], errors="coerce").iloc[0]
        if pd.isna(year):
            # Try from the top row values (row 0) that contain "at end YYYY"
            year = pd.to_numeric(
                pd.Series([data[col].iloc[0]]).astype(str).str.extract(r"(19\\d{2}|20\\d{2})")[0],
                errors="coerce",
            ).iloc[0]
        if pd.notna(year):
            year_map[col] = int(year)
    if not year_map:
        return pd.DataFrame(columns=["Entity", "Year", value_label])
    data = data.rename(columns=year_map)
    numeric_cols = [c for c in data.columns if c != "Entity"]
    data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors="coerce")
    long = data.melt(id_vars="Entity", value_vars=numeric_cols, var_name="Year", value_name=value_label)
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["Year", value_label])
    return long


@st.cache_data(show_spinner=False)
def load_country_series_header1(sheet_name: str, value_label: str):
    """Load series where useful headers start on the second row (header=1)."""
    df = pd.read_excel(DATA_FILE, sheet_name=sheet_name, header=1)
    df = df.rename(columns={df.columns[0]: "Entity"})
    df = df[df["Entity"].notna()]
    year_cols = [c for c in df.columns if isinstance(c, (int, float))]
    df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="Entity", value_vars=year_cols, var_name="Year", value_name=value_label)
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["Year", value_label])
    return long


@st.cache_data(show_spinner=False)
def load_entity_source_series(sheet_name: str, value_label: str):
    """Load series where second column is a category (e.g., Source) that should be retained."""
    df = pd.read_excel(DATA_FILE, sheet_name=sheet_name)
    df = df.rename(columns={df.columns[0]: "Entity", df.columns[1]: "Source"})
    df = df[df["Entity"].notna()]
    year_cols = [c for c in df.columns if isinstance(c, (int, float))]
    df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")
    df["EntityFull"] = df["Entity"].astype(str) + " (" + df["Source"].astype(str) + ")"
    long = df.melt(id_vars=["EntityFull"], value_vars=year_cols, var_name="Year", value_name=value_label)
    long = long.rename(columns={"EntityFull": "Entity"})
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["Year", value_label])
    return long


@st.cache_data(show_spinner=False)
def load_country_series_year_int(sheet_name: str, value_label: str):
    """Load series using only integer year columns (drops growth/share columns)."""
    df = pd.read_excel(DATA_FILE, sheet_name=sheet_name)
    df = df.rename(columns={df.columns[0]: "Entity"})
    df = df[df["Entity"].notna()]
    year_cols = []
    for col in df.columns[1:]:
        if isinstance(col, (int, float)) and pd.notna(col) and float(col).is_integer():
            year_cols.append(int(col))
    if not year_cols:
        return pd.DataFrame(columns=["Entity", "Year", value_label])
    df = df.rename(columns={c: int(c) for c in year_cols})
    df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="Entity", value_vars=year_cols, var_name="Year", value_name=value_label)
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["Year", value_label])
    return long


@st.cache_data(show_spinner=False)
def load_renewables_gen_by_source():
    """Load renewables generation by source (stacked bar by year)."""
    df = pd.read_excel(DATA_FILE, sheet_name="Renewables Generation by Source")
    df = df.rename(columns={df.columns[0]: "Entity"})
    df = df[df["Entity"].notna()]
    value_cols = [c for c in df.columns if c not in ("Entity", "Year")]
    df[value_cols] = df[value_cols].apply(pd.to_numeric, errors="coerce")
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    long = df.melt(id_vars=["Entity", "Year"], value_vars=value_cols, var_name="Source", value_name="Value")
    long = long.dropna(subset=["Value", "Year"])
    return long


@st.cache_data(show_spinner=False)
def load_wind_tech_types():
    df = pd.read_excel(DATA_FILE, sheet_name="Wind Technology Types")
    df = df.rename(columns={df.columns[0]: "Entity"})
    df = df[df["Entity"].notna()]
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    value_cols = ["Onshore", "Offshore"]
    df[value_cols] = df[value_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars=["Entity", "Year"], value_vars=value_cols, var_name="Type", value_name="CapacityMW")
    long = long.dropna(subset=["CapacityMW", "Year"])
    return long


@st.cache_data(show_spinner=False)
def load_solar_tech_types():
    df = pd.read_excel(DATA_FILE, sheet_name="Solar Technology Types")
    df = df.rename(columns={df.columns[0]: "Entity"})
    df = df[df["Entity"].notna()]
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    value_cols = ["Solar PV", "CSP"]
    df[value_cols] = df[value_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars=["Entity", "Year"], value_vars=value_cols, var_name="Type", value_name="CapacityMW")
    long = long.dropna(subset=["CapacityMW", "Year"])
    return long


@st.cache_data(show_spinner=False)
def load_elec_generation_by_fuel():
    """Load electricity generation by fuel for 2023/2024."""
    df = pd.read_excel(DATA_FILE, sheet_name="Elec generation by fuel", header=1)
    df = df.rename(
        columns={
            df.columns[0]: "Entity",
            df.columns[1]: "Year",
            df.columns[2]: "Oil",
            df.columns[3]: "Natural Gas",
            df.columns[4]: "Coal",
            df.columns[5]: "Nuclear",
            df.columns[6]: "Hydro",
            df.columns[7]: "Renewables",
            df.columns[8]: "Other",
        }
    )
    df = df[df["Entity"].notna()]
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    fuel_cols = ["Oil", "Natural Gas", "Coal", "Nuclear", "Hydro", "Renewables", "Other"]
    df[fuel_cols] = df[fuel_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars=["Entity", "Year"], value_vars=fuel_cols, var_name="Fuel", value_name="Value")
    long = long.dropna(subset=["Year", "Value"])
    return long


@st.cache_data(show_spinner=False)
def load_mineral_prices():
    df = pd.read_excel(DATA_FILE, sheet_name="Mineral Commodity Prices")
    df = df.rename(columns={df.columns[0]: "Year"})
    df = df[df["Year"].notna()]
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    value_cols = [c for c in df.columns if c != "Year"]
    for col in value_cols:
        df[col] = df[col].apply(lambda x: pd.to_numeric(x, errors="coerce"))
    long = df.melt(id_vars="Year", value_vars=value_cols, var_name="Commodity", value_name="Price")
    long = long.dropna(subset=["Year", "Price"])
    return long


@st.cache_data(show_spinner=False)
def load_mineral_series(sheet_name: str, value_label: str):
    """Load mineral production/reserves series with integer years; keep R/P ratio if present."""
    df = pd.read_excel(DATA_FILE, sheet_name=sheet_name)
    df = df.rename(columns={df.columns[0]: "Entity"})
    df = df[df["Entity"].notna()]
    rp_series = None
    if "R/P ratio" in df.columns:
        rp_series = df[["Entity", "R/P ratio"]].copy()
        df = df.drop(columns=["R/P ratio"])
    year_cols = []
    for col in df.columns[1:]:
        if isinstance(col, (int, float)) and pd.notna(col) and float(col).is_integer():
            year_cols.append(int(col))
    df = df.rename(columns={c: int(c) for c in year_cols})
    df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="Entity", value_vars=year_cols, var_name="Year", value_name=value_label)
    long["Year"] = pd.to_numeric(long["Year"], errors="coerce").astype("Int64")
    long = long.dropna(subset=["Year", value_label])
    return long, rp_series


@st.cache_data(show_spinner=False)
def load_flow_matrix(sheet_name: str, value_label: str):
    """Load origin-destination flow matrix; first column is source, others are destinations."""
    df = pd.read_excel(DATA_FILE, sheet_name=sheet_name)
    df = df.rename(columns={df.columns[0]: "From"})
    df = df[df["From"].notna()]
    destination_cols = [c for c in df.columns if c not in ("From", "Total")]
    df[destination_cols] = df[destination_cols].apply(pd.to_numeric, errors="coerce")
    long = df.melt(id_vars="From", value_vars=destination_cols, var_name="To", value_name=value_label)
    long = long.dropna(subset=[value_label])
    return long


@st.cache_data(show_spinner=False)
def load_carbon_prices(sheet_name: str):
    """Load carbon prices sheets where rows are years and columns are markets."""
    df = pd.read_excel(DATA_FILE, sheet_name=sheet_name)
    df = df.rename(columns={df.columns[0]: "Year"})
    df = df[df["Year"].notna()]
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
    value_cols = [c for c in df.columns if c != "Year"]
    for col in value_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    long = df.melt(id_vars="Year", value_vars=value_cols, var_name="Market", value_name="Price")
    long = long.dropna(subset=["Year", "Price"])
    return long


def make_line_chart(data: pd.DataFrame, countries: list, value_field: str, title: str, y_title: str):
    filtered = data[data["Country"].isin(countries)]
    if filtered.empty:
        return None
    chart = (
        alt.Chart(filtered)
        .mark_line(point=True)
        .encode(
            x=alt.X("Year:O", title="Year"),
            y=alt.Y(f"{value_field}:Q", title=y_title),
            color=alt.Color("Country:N", title="Country"),
            tooltip=["Country", "Year", alt.Tooltip(value_field, title=y_title)],
        )
        .properties(title=title, height=400)
    )
    return chart


@st.cache_data(show_spinner=False)
def load_coal_reserves():
    """Load coal reserves split by fuel type for stacked bar."""
    raw = pd.read_excel(DATA_FILE, sheet_name="Coal - Reserves", header=None)
    data = raw.iloc[2:].reset_index(drop=True)
    data = data.iloc[:, :3]
    data = data.rename(columns={0: "Country", 1: "Anthracite and bituminous", 2: "Sub-bituminous and lignite"})
    data = data[data["Country"].notna()]
    value_cols = ["Anthracite and bituminous", "Sub-bituminous and lignite"]
    data[value_cols] = data[value_cols].apply(pd.to_numeric, errors="coerce")
    long = data.melt(id_vars="Country", value_vars=value_cols, var_name="Type", value_name="ReservesMt")
    long = long.dropna(subset=["ReservesMt"])
    return long


@st.cache_data(show_spinner=False)
def load_coal_rp_ratio():
    """Compute reserve-to-production ratio using reserves and 2023 production (million tonnes)."""
    reserves = load_coal_reserves().pivot(index="Country", columns="Type", values="ReservesMt").fillna(0)
    reserves["Total Reserves (Mt)"] = reserves.sum(axis=1)
    prod = load_country_series("Coal Production - mt", "Production (million tonnes)")
    prod_2023 = prod[prod["Year"] == 2023][["Entity", "Production (million tonnes)"]].set_index("Entity")
    merged = reserves.join(prod_2023, how="left")
    merged["R/P (years)"] = merged["Total Reserves (Mt)"] / merged["Production (million tonnes)"]
    merged = merged.reset_index().rename(columns={"index": "Country"})
    merged = merged[["Country", "Total Reserves (Mt)", "Production (million tonnes)", "R/P (years)"]]
    return merged


def make_entity_line_chart(data: pd.DataFrame, entities: list, value_field: str, title: str, y_title: str):
    filtered = data[data["Entity"].isin(entities)]
    if filtered.empty:
        return None
    chart = (
        alt.Chart(filtered)
        .mark_line(point=True)
        .encode(
            x=alt.X("Year:O", title="Year"),
            y=alt.Y(f"{value_field}:Q", title=y_title),
            color=alt.Color("Entity:N", title="Entity"),
            tooltip=["Entity", "Year", alt.Tooltip(value_field, title=y_title)],
        )
        .properties(title=title, height=400)
    )
    return chart


def make_prices_line_chart(data: pd.DataFrame, markets: list, y_title: str = "Price"):
    filtered = data[data["Market"].isin(markets)]
    if filtered.empty:
        return None
    return (
        alt.Chart(filtered)
        .mark_line(point=True)
        .encode(
            x=alt.X("Year:O", title="Year"),
            y=alt.Y("Price:Q", title=y_title),
            color=alt.Color("Market:N", title="Market"),
            tooltip=["Market", "Year", "Price"],
        )
        .properties(height=400, title="Carbon prices over time")
    )


def make_flow_heatmap(data: pd.DataFrame, value_field: str, title: str):
    if data.empty:
        return None
    chart = (
        alt.Chart(data)
        .mark_rect()
        .encode(
            x=alt.X("To:N", title="To"),
            y=alt.Y("From:N", title="From"),
            color=alt.Color(f"{value_field}:Q", title=value_field, scale=alt.Scale(scheme="blues")),
            tooltip=["From", "To", alt.Tooltip(value_field, title=value_field)],
        )
        .properties(height=500, title=title)
    )
    return chart


def make_stack_chart(data: pd.DataFrame, countries: list):
    filtered = data[(data["Country"].isin(countries))]
    if filtered.empty:
        return None
    base = (
        alt.Chart(filtered)
        .mark_bar()
        .encode(
            x=alt.X("Country:N", title="Country"),
            y=alt.Y("Value:Q", stack="zero", title="TES (EJ)"),
            color=alt.Color("Fuel:N", title="Fuel type"),
            tooltip=["Country", "Fuel", "Value"],
        )
    )
    chart = base.properties(height=420)
    return chart.properties(title="TES by fuel")


def main():
    title_col, logo_col = st.columns([4, 1])
    with title_col:
        st.title("RePath Global Energy Intelligence (GEI)")
        st.caption("Energy intelligence dashboards across TES, emissions, fuels, renewables, electricity, minerals, and more.")
    with logo_col:
        if LOGO_FILE.exists():
            st.image(str(LOGO_FILE), use_container_width=True)

    if not DATA_FILE.exists():
        st.error(f"Data file not found at {DATA_FILE}")
        st.stop()

    try:
        tes_totals = load_tes_totals()
        tes_per_capita = load_tes_per_capita()
        tes_by_fuel = load_tes_by_fuel()
        exajoule_text = load_exajoule_text()
        carbon_text = load_carbon_text()
        oil_text = load_oil_text()
        gas_text = load_gas_text()
        coal_text = load_coal_text()
        nuclear_text = load_nuclear_text()
        emissions_data = {
            label: load_country_series(sheet, value_label) for label, sheet, value_label in EMISSIONS_SERIES
        }
        prices_compliance = load_carbon_prices("Carbon Prices-Compliance Market")
        prices_voluntary = load_carbon_prices("Carbon Prices-Voluntary Market")
        oil_data = {}
        for label, sheet, value_label, loader_type in OIL_SERIES:
            if loader_type == "entity_year":
                oil_data[label] = load_country_series(sheet, value_label)
            else:
                oil_data[label] = load_country_series_year_strings(sheet, value_label)
        oil_price_data = {label: load_carbon_prices(sheet) for label, sheet in OIL_PRICE_SERIES}
        oil_flow_data = {label: load_flow_matrix(sheet, value_label) for label, sheet, value_label in OIL_FLOW_TABLES}
        gas_data = {}
        for label, sheet, value_label, loader_type in GAS_SERIES:
            if loader_type == "entity_year":
                gas_data[label] = load_country_series(sheet, value_label)
            elif loader_type == "entity_year_header1":
                gas_data[label] = load_country_series_header1(sheet, value_label)
            elif loader_type == "entity_year_strings_skip8":
                gas_data[label] = load_country_series_year_strings_skip(sheet, value_label, skip_rows=8)
            elif loader_type == "entity_source_year":
                gas_data[label] = load_entity_source_series(sheet, value_label)
            else:
                gas_data[label] = load_country_series_year_strings(sheet, value_label)
        gas_price_data = {}
        for label, sheet in GAS_PRICE_SERIES:
            try:
                gas_price_data[label] = load_carbon_prices(sheet)
            except Exception:
                gas_price_data[label] = pd.DataFrame(columns=["Year", "Market", "Price"])
        gas_flow_data = {}
        for label, sheet, value_label in GAS_FLOW_TABLES:
            try:
                flow_df = load_flow_matrix(sheet, value_label)
                # For trade movement sheets, flip origin/destination to match requested orientation.
                if "Trade movements" in label:
                    flow_df = flow_df.rename(columns={"From": "To", "To": "From"})
                gas_flow_data[label] = flow_df
            except Exception:
                gas_flow_data[label] = pd.DataFrame(columns=["From", "To", value_label])
        coal_data = {}
        for label, sheet, value_label, loader_type in COAL_SERIES:
            if loader_type == "entity_year":
                coal_data[label] = load_country_series(sheet, value_label)
        coal_price_data = {label: load_carbon_prices(sheet) for label, sheet in COAL_PRICE_SERIES}
        coal_flow_data = {label: load_flow_matrix(sheet, value_label) for label, sheet, value_label in COAL_FLOW_TABLES}
        coal_reserves = load_coal_reserves()
        coal_rp = load_coal_rp_ratio()
        nuclear_data = {label: load_country_series(sheet, value_label) for label, sheet, value_label, _ in NUCLEAR_SERIES}
        hydro_data = {label: load_country_series(sheet, value_label) for label, sheet, value_label, _ in HYDRO_SERIES}
        renewable_data = {}
        for label, sheet, value_label, loader_type in RENEWABLE_SERIES:
            if loader_type == "entity_year_int":
                renewable_data[label] = load_country_series_year_int(sheet, value_label)
            else:
                renewable_data[label] = load_country_series(sheet, value_label)
        renew_gen_source = load_renewables_gen_by_source()
        wind_tech = load_wind_tech_types()
        solar_tech = load_solar_tech_types()
        electricity_data = {}
        for label, sheet, value_label, loader_type in ELECTRICITY_SERIES:
            if loader_type == "entity_year_int":
                electricity_data[label] = load_country_series_year_int(sheet, value_label)
            else:
                electricity_data[label] = load_country_series(sheet, value_label)
        elec_gen_fuel = load_elec_generation_by_fuel()
        mineral_data = {}
        mineral_rp = {}
        for label, sheet, value_label, loader_type in MINERAL_SERIES:
            series, rp = load_mineral_series(sheet, value_label)
            mineral_data[label] = series
            mineral_rp[label] = rp
        mineral_prices = load_mineral_prices()
        mineral_text = load_mineral_text()
        project_text = load_project_text()
    except Exception as exc:
        st.error(f"Failed to load data: {exc}")
        st.stop()

    tab_instructions, tab_tes, tab_emissions, tab_oil, tab_gas, tab_coal, tab_nuclear, tab_hydro, tab_renewables, tab_electricity, tab_minerals = st.tabs(
        [
            "About RePath GEI",
            "Total Energy Supply",
            "Emission Data",
            "Global Oil Data",
            "Global Gas Data",
            "Global Coal Data",
            "Global Nuclear Energy Data",
            "Global Hydro Energy Data",
            "Global Renewable Data",
            "Global Electricity Data",
            "Global Mineral Data",
        ]
    )

    with tab_instructions:
        #st.subheader("About RePath GEI")
        if project_text:
            st.markdown(project_text)
            if LOGO_FILE.exists():
                _, col_logo = st.columns([3, 1])
                with col_logo:
                    st.image(str(LOGO_FILE), use_container_width=True)
        else:
            st.info("No instructions file found.")

    with tab_tes:
        st.subheader("Total Energy Supply (Exajoules)")
        country_options = sorted(tes_totals["Country"].unique())
        default_countries = [c for c in ["World", "China", "US", "India", "Russia"] if c in country_options][:3] or country_options[:5]
        selected_countries = st.multiselect("Select countries for TES trends", options=country_options, default=default_countries)

        tes_chart = make_line_chart(
            tes_totals,
            selected_countries,
            value_field="TES_EJ",
            title="Total Energy Supply over time",
            y_title="TES (EJ)",
        )
        if tes_chart is not None:
            st.altair_chart(tes_chart, use_container_width=True)
        else:
            st.info("Select at least one country to see the TES trend.")

        st.divider()
        st.subheader("TES by Fuel (stacked)")
        fuel_options = sorted(tes_by_fuel["Country"].unique())
        fuel_default = [c for c in selected_countries if c in fuel_options]
        if not fuel_default:
            fuel_default = fuel_options[:5]
        fuel_countries = st.multiselect(
            "Select countries for fuel mix",
            options=fuel_options,
            default=fuel_default,
        )
        stack_chart = make_stack_chart(tes_by_fuel, fuel_countries)
        if stack_chart is not None:
            st.altair_chart(stack_chart, use_container_width=True)
        else:
            st.info("Select at least one country to view the stacked bar chart.")

        st.divider()
        st.subheader("TES per Capita (Gigajoules/person)")
        per_capita_countries = st.multiselect(
            "Select countries for per capita trends",
            options=country_options,
            default=selected_countries,
            key="per_capita_country_select",
        )
        per_capita_chart = make_line_chart(
            tes_per_capita,
            per_capita_countries,
            value_field="TES_per_capita",
            title="TES per Capita over time",
            y_title="TES per Capita (GJ/person)",
        )
        if per_capita_chart is not None:
            st.altair_chart(per_capita_chart, use_container_width=True)
        else:
            st.info("Select at least one country to see the per capita trend.")

        if exajoule_text:
            st.divider()
            st.markdown(exajoule_text)

    with tab_emissions:
        st.subheader("Emission Data")
        dataset_options = [label for label, _, _ in EMISSIONS_SERIES] + [
            "Carbon Prices- Compliance Market",
            "Carbon Prices- Voluntary Market",
        ]
        selected_dataset = st.selectbox("Select dataset", options=dataset_options)

        if selected_dataset in dict((label, sheet) for label, sheet, _ in EMISSIONS_SERIES):
            value_label = dict((label, val) for label, _, val in EMISSIONS_SERIES)[selected_dataset]
            data = emissions_data[selected_dataset]
            entities = sorted(data["Entity"].unique())
            default_entities = [e for e in ["World", "China", "US", "India", "EU"] if e in entities][:3] or entities[:5]
            chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities)
            chart = make_entity_line_chart(
                data,
                chosen_entities,
                value_field=value_label,
                title=selected_dataset,
                y_title=value_label,
            )
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one entity to view the chart.")
        elif selected_dataset == "Carbon Prices- Compliance Market":
            markets = sorted(prices_compliance["Market"].unique())
            default_markets = markets[:3]
            chosen_markets = st.multiselect("Select markets", options=markets, default=default_markets)
            chart = make_prices_line_chart(prices_compliance, chosen_markets)
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one market to view prices.")
        else:
            markets = sorted(prices_voluntary["Market"].unique())
            default_markets = markets[:3]
            chosen_markets = st.multiselect("Select markets", options=markets, default=default_markets, key="voluntary_markets")
            chart = make_prices_line_chart(prices_voluntary, chosen_markets)
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one market to view prices.")

        if carbon_text:
            st.divider()
            st.markdown(carbon_text)

    with tab_oil:
        st.subheader("Global Oil Data")
        dataset_options = (
            [label for label, _, _, _ in OIL_SERIES]
            + [label for label, _ in OIL_PRICE_SERIES]
            + [label for label, _, _ in OIL_FLOW_TABLES]
        )
        selected_dataset = st.selectbox("Select oil dataset", options=dataset_options)

        if selected_dataset in oil_data:
            data = oil_data[selected_dataset]
            value_label = [val for lbl, _, val, _ in OIL_SERIES if lbl == selected_dataset][0]
            entities = sorted(data["Entity"].unique())
            default_entities = [e for e in ["World", "OPEC", "OECD", "US", "China"] if e in entities][:3] or entities[:5]
            chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities, key=f"oil-{selected_dataset}")
            chart = make_entity_line_chart(
                data,
                chosen_entities,
                value_field=value_label,
                title=selected_dataset,
                y_title=value_label,
            )
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one entity to view the chart.")
        elif selected_dataset in oil_price_data:
            data = oil_price_data[selected_dataset]
            markets = sorted(data["Market"].unique())
            default_markets = markets[:3]
            chosen_markets = st.multiselect("Select markets", options=markets, default=default_markets, key=f"price-{selected_dataset}")
            chart = make_prices_line_chart(data, chosen_markets)
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one market to view prices.")
        elif selected_dataset in oil_flow_data:
            data = oil_flow_data[selected_dataset]
            value_label = [val for lbl, _, val in OIL_FLOW_TABLES if lbl == selected_dataset][0]
            min_value = st.slider("Minimum flow to display", 0.0, float(data[value_label].max()), 0.0, step=1.0)
            filtered = data[data[value_label] >= min_value]
            chart = make_flow_heatmap(filtered, value_field=value_label, title=selected_dataset)
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("No flows match the current filter.")
        else:
            st.info("Select a dataset to visualize.")

        if oil_text:
            st.divider()
            st.markdown(oil_text)

    with tab_gas:
        st.subheader("Global Gas Data")
        gas_dataset_options = (
            [label for label, _, _, _ in GAS_SERIES]
            + [label for label, _ in GAS_PRICE_SERIES]
            + [label for label, _, _ in GAS_FLOW_TABLES]
        )
        selected_gas = st.selectbox("Select gas dataset", options=gas_dataset_options)

        if selected_gas in gas_data:
            data = gas_data[selected_gas]
            value_label = [val for lbl, _, val, _ in GAS_SERIES if lbl == selected_gas][0]
            entities = sorted(data["Entity"].unique())
            default_entities = [e for e in ["World", "OECD", "US", "China", "EU"] if e in entities][:3] or entities[:5]
            chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities, key=f"gas-{selected_gas}")
            chart = make_entity_line_chart(
                data,
                chosen_entities,
                value_field=value_label,
                title=selected_gas,
                y_title=value_label,
            )
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one entity to view the chart.")
        elif selected_gas in gas_price_data:
            data = gas_price_data[selected_gas]
            markets = sorted(data["Market"].unique())
            if not markets:
                st.info("No price data available for this selection.")
            else:
                default_markets = markets[:3]
                chosen_markets = st.multiselect(
                    "Select markets", options=markets, default=default_markets, key=f"gas-price-{selected_gas}"
                )
                chart = make_prices_line_chart(data, chosen_markets)
                if chart is not None:
                    st.altair_chart(chart, use_container_width=True)
                else:
                    st.info("Select at least one market to view prices.")
        elif selected_gas in gas_flow_data:
            data = gas_flow_data[selected_gas]
            value_label = [val for lbl, _, val in GAS_FLOW_TABLES if lbl == selected_gas][0]
            if data.empty or data[value_label].max() is None or pd.isna(data[value_label].max()):
                st.info("No flow data available for this selection.")
            else:
                max_val = float(data[value_label].max())
                min_value = st.slider("Minimum flow to display", 0.0, max_val, 0.0, step=1.0)
                filtered = data[data[value_label] >= min_value]
                chart = make_flow_heatmap(filtered, value_field=value_label, title=selected_gas)
                if chart is not None:
                    st.altair_chart(chart, use_container_width=True)
                else:
                    st.info("No flows match the current filter.")
        else:
            st.info("Select a dataset to visualize.")

        if gas_text:
            st.divider()
            st.markdown(gas_text)

    with tab_coal:
        st.subheader("Global Coal Data")
        coal_dataset_options = (
            ["Coal: Reserves (stacked)"]
            + ["Coal: Reserve to Production ratio (table)"]
            + [label for label, _, _, _ in COAL_SERIES]
            + [label for label, _ in COAL_PRICE_SERIES]
            + [label for label, _, _ in COAL_FLOW_TABLES]
        )
        selected_coal = st.selectbox("Select coal dataset", options=coal_dataset_options)

        if selected_coal == "Coal: Reserves (stacked)":
            countries = st.multiselect(
                "Select countries", options=sorted(coal_reserves["Country"].unique()), default=sorted(coal_reserves["Country"].unique())[:10]
            )
            data = coal_reserves[coal_reserves["Country"].isin(countries)]
            chart = (
                alt.Chart(data)
                .mark_bar()
                .encode(
                    x=alt.X("Country:N", title="Country"),
                    y=alt.Y("ReservesMt:Q", stack="zero", title="Reserves (million tonnes)"),
                    color=alt.Color("Type:N", title="Type"),
                    tooltip=["Country", "Type", "ReservesMt"],
                )
                .properties(height=400, title="Coal reserves by type")
            )
            st.altair_chart(chart, use_container_width=True)
        elif selected_coal == "Coal: Reserve to Production ratio (table)":
            st.dataframe(coal_rp, use_container_width=True, height=400)
        elif selected_coal in coal_data:
            data = coal_data[selected_coal]
            value_label = [val for lbl, _, val, _ in COAL_SERIES if lbl == selected_coal][0]
            entities = sorted(data["Entity"].unique())
            default_entities = [e for e in ["World", "China", "US", "India", "EU"] if e in entities][:3] or entities[:5]
            chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities, key=f"coal-{selected_coal}")
            chart = make_entity_line_chart(
                data,
                chosen_entities,
                value_field=value_label,
                title=selected_coal,
                y_title=value_label,
            )
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one entity to view the chart.")
        elif selected_coal in coal_price_data:
            data = coal_price_data[selected_coal]
            markets = sorted(data["Market"].unique())
            default_markets = markets[:3]
            chosen_markets = st.multiselect("Select markets", options=markets, default=default_markets, key=f"coal-price-{selected_coal}")
            y_title = "Price (USD/ton)" if "Coal: Mined energy resource & Uranium prices" in selected_coal else "Price"
            chart = make_prices_line_chart(data, chosen_markets, y_title=y_title)
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one market to view prices.")
        elif selected_coal in coal_flow_data:
            data = coal_flow_data[selected_coal]
            value_label = [val for lbl, _, val in COAL_FLOW_TABLES if lbl == selected_coal][0]
            min_value = st.slider("Minimum flow to display", 0.0, float(data[value_label].max()), 0.0, step=0.01)
            filtered = data[data[value_label] >= min_value]
            chart = make_flow_heatmap(filtered, value_field=value_label, title=selected_coal)
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("No flows match the current filter.")
        else:
            st.info("Select a dataset to visualize.")

        if coal_text:
            st.divider()
            st.markdown(coal_text)

    with tab_nuclear:
        st.subheader("Global Nuclear Energy Data")
        nuclear_options = [label for label, _, _, _ in NUCLEAR_SERIES]
        selected_nuclear = st.selectbox("Select nuclear dataset", options=nuclear_options)
        data = nuclear_data[selected_nuclear]
        value_label = [val for lbl, _, val, _ in NUCLEAR_SERIES if lbl == selected_nuclear][0]
        entities = sorted(data["Entity"].unique())
        default_entities = [e for e in ["World", "OECD", "US", "China", "France"] if e in entities][:3] or entities[:5]
        chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities, key=f"nuclear-{selected_nuclear}")
        chart = make_entity_line_chart(
            data,
            chosen_entities,
            value_field=value_label,
            title=selected_nuclear,
            y_title=value_label,
        )
        if chart is not None:
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("Select at least one entity to view the chart.")

        if nuclear_text:
            st.divider()
            st.markdown(nuclear_text)

    with tab_hydro:
        st.subheader("Global Hydro Energy Data")
        hydro_options = [label for label, _, _, _ in HYDRO_SERIES]
        selected_hydro = st.selectbox("Select hydro dataset", options=hydro_options)
        data = hydro_data[selected_hydro]
        value_label = [val for lbl, _, val, _ in HYDRO_SERIES if lbl == selected_hydro][0]
        entities = sorted(data["Entity"].unique())
        default_entities = [e for e in ["World", "China", "US", "Canada", "Brazil"] if e in entities][:3] or entities[:5]
        chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities, key=f"hydro-{selected_hydro}")
        chart = make_entity_line_chart(
            data,
            chosen_entities,
            value_field=value_label,
            title=selected_hydro,
            y_title=value_label,
        )
        if chart is not None:
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("Select at least one entity to view the chart.")

    with tab_electricity:
        st.subheader("Global Electricity Data")
        elec_options = (
            [label for label, _, _, _ in ELECTRICITY_SERIES]
            + ["Electricity generation by fuel - TWh (2023 and 2024)"]
        )
        selected_elec = st.selectbox("Select electricity dataset", options=elec_options)

        if selected_elec in electricity_data:
            data = electricity_data[selected_elec]
            value_label = [val for lbl, _, val, _ in ELECTRICITY_SERIES if lbl == selected_elec][0]
            entities = sorted(data["Entity"].unique())
            default_entities = [e for e in ["World", "OECD", "US", "China", "EU"] if e in entities][:3] or entities[:5]
            chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities, key=f"elec-{selected_elec}")
            chart = make_entity_line_chart(
                data,
                chosen_entities,
                value_field=value_label,
                title=selected_elec,
                y_title=value_label,
            )
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one entity to view the chart.")
        else:
            # Electricity generation by fuel stacked bars for 2023/2024
            melted = elec_gen_fuel
            years = sorted(melted["Year"].dropna().unique())
            chosen_years = st.multiselect("Select year(s)", options=years, default=years)
            filtered = melted[melted["Year"].isin(chosen_years)]
            if filtered.empty:
                st.info("No data for selected years.")
            else:
                chart = (
                    alt.Chart(filtered)
                    .mark_bar()
                    .encode(
                        x=alt.X("Entity:N", title="Entity"),
                        y=alt.Y("Value:Q", stack="zero", title="Generation (TWh)"),
                        color=alt.Color("Fuel:N", title="Fuel"),
                        column=alt.Column("Year:O", title="Year") if len(chosen_years) > 1 else alt.Undefined,
                        tooltip=["Entity", "Year", "Fuel", "Value"],
                    )
                    .properties(height=420, title="Electricity generation by fuel")
                )
                st.altair_chart(chart, use_container_width=True)

    with tab_minerals:
        st.subheader("Global Mineral Data")
        mineral_options = [label for label, _, _, _ in MINERAL_SERIES] + ["Key materials - Mineral Commodity Prices"]
        selected_mineral = st.selectbox("Select mineral dataset", options=mineral_options)

        if selected_mineral in mineral_data:
            data = mineral_data[selected_mineral]
            value_label = [val for lbl, _, val, _ in MINERAL_SERIES if lbl == selected_mineral][0]
            entities = sorted(data["Entity"].unique())
            default_entities = [e for e in ["World", "China", "Australia", "US", "Chile"] if e in entities][:3] or entities[:5]
            chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities, key=f"min-{selected_mineral}")
            chart = make_entity_line_chart(
                data,
                chosen_entities,
                value_field=value_label,
                title=selected_mineral,
                y_title=value_label,
            )
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one entity to view the chart.")

            rp = mineral_rp.get(selected_mineral)
            if rp is not None:
                st.caption("R/P ratio (years)")
                st.dataframe(rp, use_container_width=True, height=300)
        else:
            markets = sorted(mineral_prices["Commodity"].unique())
            default_markets = markets[:4]
            chosen_markets = st.multiselect("Select commodities", options=markets, default=default_markets, key="mineral-prices")
            filtered = mineral_prices[mineral_prices["Commodity"].isin(chosen_markets)]
            if filtered.empty:
                st.info("Select at least one commodity to view prices.")
            else:
                chart = (
                    alt.Chart(filtered)
                    .mark_line(point=True)
                    .encode(
                        x=alt.X("Year:O", title="Year"),
                        y=alt.Y("Price:Q", title="Price"),
                        color=alt.Color("Commodity:N", title="Commodity"),
                        tooltip=["Commodity", "Year", "Price"],
                    )
                    .properties(height=400, title="Mineral commodity prices")
                )
                st.altair_chart(chart, use_container_width=True)

        if mineral_text:
            st.divider()
            st.markdown(mineral_text)

    with tab_renewables:
        st.subheader("Global Renewable Data")
        renew_options = (
            [label for label, _, _, _ in RENEWABLE_SERIES]
            + ["Renewables - Generation by source - TWh (2022 and 2023)"]
            + ["Renewable Energy - Solar and Wind Installed capacity by type (2023 and 2024)"]
        )
        selected_renew = st.selectbox("Select renewables dataset", options=renew_options)

        if selected_renew in renewable_data:
            data = renewable_data[selected_renew]
            value_label = [val for lbl, _, val, _ in RENEWABLE_SERIES if lbl == selected_renew][0]
            entities = sorted(data["Entity"].unique())
            default_entities = [e for e in ["World", "China", "US", "EU", "India"] if e in entities][:3] or entities[:5]
            chosen_entities = st.multiselect("Select entities", options=entities, default=default_entities, key=f"renew-{selected_renew}")
            chart = make_entity_line_chart(
                data,
                chosen_entities,
                value_field=value_label,
                title=selected_renew,
                y_title=value_label,
            )
            if chart is not None:
                st.altair_chart(chart, use_container_width=True)
            else:
                st.info("Select at least one entity to view the chart.")
        elif selected_renew == "Renewables - Generation by source - TWh (2022 and 2023)":
            years = sorted(renew_gen_source["Year"].dropna().unique())
            chosen_years = st.multiselect("Select year(s)", options=years, default=years)
            filtered = renew_gen_source[renew_gen_source["Year"].isin(chosen_years)]
            if filtered.empty:
                st.info("No data for selected years.")
            else:
                chart = (
                    alt.Chart(filtered)
                    .mark_bar()
                    .encode(
                        x=alt.X("Entity:N", title="Entity"),
                        y=alt.Y("Value:Q", stack="zero", title="Generation (TWh)"),
                        color=alt.Color("Source:N", title="Source"),
                        column=alt.Column("Year:O", title="Year") if len(chosen_years) > 1 else alt.Undefined,
                        tooltip=["Entity", "Year", "Source", "Value"],
                    )
                    .properties(height=420, title="Renewables generation by source")
                )
                st.altair_chart(chart, use_container_width=True)
        else:
            # Solar & Wind tech types
            tech_choice = st.radio(
                "Select technology mix",
                options=["Solar", "Wind"],
                horizontal=True,
            )
            if tech_choice == "Solar":
                data = solar_tech
                value_field = "CapacityMW"
            else:
                data = wind_tech
                value_field = "CapacityMW"
            years = sorted(data["Year"].dropna().unique())
            chosen_years = st.multiselect("Select year(s)", options=years, default=years)
            filtered = data[data["Year"].isin(chosen_years)]
            if filtered.empty:
                st.info("No data for selected years.")
            else:
                chart = (
                    alt.Chart(filtered)
                    .mark_bar()
                    .encode(
                        x=alt.X("Entity:N", title="Entity"),
                        y=alt.Y(f"{value_field}:Q", stack="zero", title="Capacity (MW)"),
                        color=alt.Color("Type:N", title="Type"),
                        column=alt.Column("Year:O", title="Year") if len(chosen_years) > 1 else alt.Undefined,
                        tooltip=["Entity", "Year", "Type", value_field],
                    )
                    .properties(height=420, title=f"{tech_choice} capacity by technology type")
                )
                st.altair_chart(chart, use_container_width=True)


if __name__ == "__main__":
    main()
