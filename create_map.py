import folium
from folium.plugins import MiniMap
from folium.plugins import MousePosition

# Create a base map centered on a location at Kuala Lumpur
m = folium.Map(location=[3.13900300, 101.68685500], zoom_start=12, control_scale=True)

folium.plugins.Geocoder().add_to(m)

folium.plugins.Fullscreen(
    position="topright",
    title="Expand",
    title_cancel="Exit",
    force_separate_button=True,
).add_to(m)

MiniMap().add_to(m)

MousePosition().add_to(m)

landmarks = {
    "KLCC": [3.15916, 101.71366],
    "Batu Caves": [3.238, 101.682],
}

# Add markers with hardcoded coordinates
for name, coords in landmarks.items():
    folium.Marker(
        coords,
        popup=name,
        icon=folium.Icon(color='purple', icon='info-sign')
    ).add_to(m)

folium.Marker([3.215, 101.727],
              popup="TARUMT",
                icon=folium.Icon(
                    icon_color='#3C711E',
                    icon='university',
                    prefix='fa'),  # note fa prefix flag to use Font Awesome
                ).add_to(m)

# Add different tile layers
folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google Satellite',
    name='Google Satellite'
).add_to(m)

folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
    attr='Google Terrain',
    name='Google Terrain'
).add_to(m)

folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
    attr='Google Hybrid',
    name='Google Hybrid'
).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map
m.save('map.html') 