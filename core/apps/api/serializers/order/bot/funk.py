

def create_google_maps_link(latitude, longitude, zoom=16, map_service="yandex"):
    """
    Given latitude and longitude, this function returns a URL link to either Google Maps or Yandex Maps.

    Parameters:
    latitude (float): Latitude of the location.
    longitude (float): Longitude of the location.
    map_service (str): Map service to use ('google' or 'yandex'). Default is 'google'.

    Returns:
    str: URL link to the map service showing the specified location.
    """
    if map_service == 'google':
        return f"https://www.google.com/maps?q={latitude},{longitude}"
    elif map_service == 'yandex':
        return f"https://yandex.com/maps/?pt={longitude},{latitude}&z=14&l=map"
    else:
        return "Invalid map service specified. Use 'google' or 'yandex'."
