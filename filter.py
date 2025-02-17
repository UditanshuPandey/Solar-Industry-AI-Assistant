# filter.py - Solar Energy Query Filtering Module

def is_solar_related(query):
    """Check if the query is related to solar energy."""
    solar_keywords = [
        "solar", "photovoltaic", "renewable", "solar panel", "solar energy",
        "solar power", "PV system", "net metering", "solar installation",
        "inverter", "solar efficiency", "solar cells", "solar farm",
        "solar battery", "solar thermal", "off-grid solar"
    ]
    return any(keyword in query.lower() for keyword in solar_keywords)