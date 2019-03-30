import folium

# Create map object
m=folium.Map(location=[43.7001114, -79.416297], zoom_start=12)

#Global tooltip
tooltip = 'Discarded Needles'

# Create markers
folium.Marker([43.6578577,-79.4001602],
    popup='<strong>Potential Heroin Use</strong>',
    tooltip=tooltip).add_to(m)

folium.Marker([43.6578577,-79.4201602],
    popup='<strong>Methamphetamine User</strong>',
    tooltip='Individual seen smoking from glass pipe',
    icon=folium.Icon(color='purple')).add_to(m)

folium.Marker([43.6878577,-79.3999999],
    popup='<strong>Broken Bottles (public Drinking)</strong>',
    tooltip='loud noise and sound of shattered glass observed',
    icon=folium.Icon(color='red', icon='leaf')).add_to(m)

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
m.save('map.html')