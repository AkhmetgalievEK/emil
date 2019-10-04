import graph as g


window_width = 640
window_height = 442
g.windowSize(window_width, window_height)
g.canvasSize(window_width, window_height)

picture_width = 600
pen_width_0 = 0
pen_width_1 = 1


g.penSize(pen_width_0)

width_line_of_sky = 187
sky_upper_left_point_x = 20
sky_upper_left_point_y = 20
sky_bottom_right_point_x = sky_upper_left_point_x + picture_width
sky_bottom_right_point_y = sky_upper_left_point_y + width_line_of_sky
sky_color = '#94ffff'
g.brushColor(sky_color)
g.rectangle(sky_upper_left_point_x, sky_upper_left_point_y, 
            sky_bottom_right_point_x, sky_bottom_right_point_y)

width_line_of_sea = 91
sea_upper_left_point_x = sky_upper_left_point_x
sea_upper_left_point_y = sky_bottom_right_point_y
sea_bottom_right_point_x = sky_bottom_right_point_x
sea_bottom_right_point_y = sea_upper_left_point_y + width_line_of_sea
sea_color = '#4c00ff'
g.brushColor(sea_color)
g.rectangle(sea_upper_left_point_x, sea_upper_left_point_y, 
            sea_bottom_right_point_x, sea_bottom_right_point_y)

width_line_of_beach = 124
beach_upper_left_point_x = sea_upper_left_point_x
beach_upper_left_point_y = sea_bottom_right_point_y
beach_bottom_right_point_x = sea_bottom_right_point_x
beach_bottom_right_point_y = beach_upper_left_point_y + width_line_of_beach
beach_color = '#ede900'
g.brushColor('#ede900')
g.rectangle(beach_upper_left_point_x, beach_upper_left_point_y,
            beach_bottom_right_point_x, beach_bottom_right_point_y)


center_of_sun_x = 553
center_of_sun_y = 77
radius_of_sun = 38
sun_color = 'yellow'
g.brushColor(sun_color)
g.circle(center_of_sun_x, center_of_sun_y, radius_of_sun)


g.penSize(pen_width_1)
cloud_color = 'white'
g.brushColor(cloud_color)
radius_of_cloud = 14
step_of_clouds = 3 / 2 * radius_of_cloud


center_of_cloud_1_x = 152
center_of_cloud_1_y = 73
number_of_clouds_1 = 2
for i in range(number_of_clouds_1):
    g.circle(center_of_cloud_1_x, center_of_cloud_1_y, radius_of_cloud)
    center_of_cloud_1_x += step_of_clouds

center_of_cloud_2_x = 138
center_of_cloud_2_y = 84
number_of_clouds_2 = 3
for i in range(number_of_clouds_2):
    g.circle(center_of_cloud_2_x, center_of_cloud_2_y, radius_of_cloud)
    center_of_cloud_2_x += step_of_clouds

g.circle(center_of_cloud_1_x, center_of_cloud_1_y, radius_of_cloud)
g.circle(center_of_cloud_2_x, center_of_cloud_2_y, radius_of_cloud)


umbrella_base_x = 112
umbrella_base_y = 403
umbrella_stick_length = 120
umbrella_stick_width = 6
umbrella_triangle_base = 138 
umbrella_triangle_height = 33

umbrella_triangle_left_angle_x = umbrella_base_x - umbrella_triangle_base / 2 
umbrella_triangle_left_angle_y = umbrella_base_y - umbrella_stick_length

umbrella_triangle_right_angle_x = umbrella_triangle_left_angle_x + umbrella_triangle_base
umbrella_triangle_right_angle_y = umbrella_triangle_left_angle_y

umbrella_top_angle_x = umbrella_base_x
umbrella_top_angle_y = umbrella_triangle_left_angle_y - umbrella_triangle_height

g.penSize(umbrella_stick_width)
umbrella_color = '#c56200'
g.penColor(umbrella_color)
g.line(umbrella_base_x, umbrella_base_y, 
       umbrella_base_x, umbrella_triangle_left_angle_y)

g.penSize(pen_width_1)
g.penColor('black')

g.brushColor('#f66347')
g.polygon([(umbrella_triangle_left_angle_x, umbrella_triangle_left_angle_y),
           (umbrella_triangle_right_angle_x, umbrella_triangle_right_angle_y),
           (umbrella_top_angle_x, umbrella_top_angle_y)])

number_of_needle = 6
needle_base_point_x = umbrella_triangle_left_angle_x
step_needle = umbrella_triangle_base / 7
for i in range(number_of_needle):
    needle_base_point_x += step_needle
    g.line(umbrella_top_angle_x, umbrella_top_angle_y, 
           needle_base_point_x, umbrella_triangle_left_angle_y)
    

ship_bow_x = 581
ship_bow_y = 221

ship_keel_x = ship_bow_x - 65
ship_keel_y = ship_bow_y + 28 

ship_stern_top_x = ship_bow_x - 209
ship_stern_top_y = ship_bow_y

ship_stern_bottom_x = ship_stern_top_x
ship_stern_bottom_y = ship_keel_y 

ship_color = '#df6f0d'
g.penColor(ship_color)
g.brushColor(ship_color)
g.polygon([(ship_bow_x, ship_bow_y),
           (ship_keel_x, ship_keel_y),
           (ship_stern_bottom_x, ship_stern_bottom_y), 
           (ship_stern_top_x, ship_stern_top_y)])

ship_stern_radius = ship_stern_bottom_y - ship_stern_top_y
g.circle(ship_stern_top_x, ship_stern_top_y, ship_stern_radius)

fill_1_top_left_point_x = ship_stern_top_x - ship_stern_radius 
fill_1_top_left_point_y = sea_upper_left_point_y 
fill_1_bottom_right_point_x = ship_stern_top_x + ship_stern_radius
fill_1_bottom_right_point_y = ship_stern_top_y - 1
g.penColor(sea_color)
g.brushColor(sea_color)
g.rectangle(fill_1_top_left_point_x, fill_1_top_left_point_y,
             fill_1_bottom_right_point_x, fill_1_bottom_right_point_y)

fill_2_top_left_point_x = ship_stern_top_x - ship_stern_radius
fill_2_top_left_point_y = ship_stern_top_y - ship_stern_radius
fill_2_bottom_right_point_x = ship_stern_top_x + ship_stern_radius
fill_2_bottom_right_point_y = sea_upper_left_point_y - 1
g.penColor(sky_color)
g.brushColor(sky_color)
g.rectangle(fill_2_top_left_point_x, fill_2_top_left_point_y,
             fill_2_bottom_right_point_x, fill_2_bottom_right_point_y)

g.penColor(sea_color)
g.penSize(pen_width_1)
g.line(ship_stern_top_x, ship_stern_top_y, ship_stern_bottom_x, ship_stern_bottom_y)
g.line(ship_keel_x, ship_bow_y, ship_keel_x, ship_keel_y)


ship_porthole_center_x = ship_bow_x - 50
ship_porthole_center_y = ship_bow_y + 11
ship_porthole_radius = 7
porthole_pen_width = 3
g.penSize(porthole_pen_width)
g.penColor('black')
portole_color = 'white'
g.brushColor(portole_color)
g.circle(ship_porthole_center_x, ship_porthole_center_y, ship_porthole_radius)


mast_base_x = ship_bow_x - 150
mast_base_y = ship_bow_y 
mast_hight = 96
mast_width = 6

g.penSize(mast_width)
mast_color = 'black'
g.penColor(mast_color)
g.line(mast_base_x, mast_base_y, mast_base_x, mast_base_y - mast_hight)


sail_top_mount_x = mast_base_x
sail_top_mount_y = mast_base_y - mast_hight
sail_bottom_mount_x = mast_base_x
sail_bottom_mount_y = mast_base_y
sail_left_edge_x = ship_bow_x - 134
sail_left_edge_y = (sail_top_mount_y + sail_bottom_mount_y) / 2
sail_right_edge_x = ship_bow_x - 96
sail_right_edge_y = sail_left_edge_y

g.penSize(pen_width_1)
g.penColor('black')
sail_color = '#c9c094'
g.brushColor(sail_color)
g.polygon([(sail_top_mount_x, sail_top_mount_y),
           (sail_left_edge_x, sail_left_edge_y), 
           (sail_right_edge_x, sail_right_edge_y)])
g.polygon([(sail_bottom_mount_x, sail_bottom_mount_y), 
           (sail_left_edge_x, sail_left_edge_y),
           (sail_right_edge_x, sail_right_edge_y)])


g.run()





