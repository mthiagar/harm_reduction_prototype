import folium
import pandas as pd

from folium.plugins import HeatMap


def generateBaseMap(default_location=[43.7001114, -79.416297], default_zoom_start=12):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map


df_locations = pd.read_csv('traffic_signals.csv', header=1 )
df_locations['count']=1

# Create map object
m = generateBaseMap()

HeatMap(data=df_locations[['Latitude', 'Longitude', 'count']].groupby(['Latitude', 'Longitude']).sum().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(m)
ClinicIcon = folium.features.CustomIcon('icons/clinic-medical-solid.svg.png', icon_size=(25, 25))
HospitalIcon = folium.features.CustomIcon('icons/h-square-solid.svg.png', icon_size=(25, 25))
JointIcon = folium.features.CustomIcon('icons/joint-solid.svg.png', icon_size=(25, 25))
SmokingIcon = folium.features.CustomIcon('icons/smoking-solid.svg.png', icon_size=(25, 25))
SyringeIcon = folium.features.CustomIcon('icons/syringe-solid.png', icon_size=(25, 25))
BottleIcon = folium.features.CustomIcon('icons/wine-bottle-solid.svg.png', icon_size=(25, 25))

#Global tooltip
tooltip = 'Discarded Needles'

# Create markers

folium.Marker([43.6564426,-79.3796788],
              popup='<strong>277 Victoria Street</strong>',
              tooltip="The Works Needle Exchange Program",
icon=ClinicIcon).add_to(m),

folium.Marker([43.6578577,-79.4201602],
    popup='<strong>Methamphetamine User</strong>',
    tooltip='Individual seen smoking from glass pipe',
    icon=JointIcon).add_to(m)

folium.Marker([43.6878577,-79.3999999],
    popup='<strong>Broken Bottles (public Drinking)</strong>',
    tooltip='loud noise and sound of shattered glass observed',
    icon=SmokingIcon
    ).add_to(m)

# Cicle Marker
folium.CircleMarker(
    location=[43.6425512,-79.3871549],
    radius=50,
    popup='High Drug Activity',
    color='red',
    fill=True,
    fill_color='#428bca'
).add_to(m)


#generate map
m.save('index.html')