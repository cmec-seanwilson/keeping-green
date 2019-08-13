from building import Building
from floor import Floor

def seed():
    # Create buildings
    building_ab1 = Building(street_number = 1653, name = 'AB1', image = '')
    buidling_bedford = Building(street_number = 1650, name = 'Bedford', image = '')

    # Create floors
    floor_ab1_sub = Floor(name = 'Sub', building_ab1)
    floor_ab1_main = Floor(name = 'Main', building_ab1)
    floor_ab1_2 = Floor(name = '2nd', building_ab1)
    floor_ab1_3 = Floor(name = '3rd', building_ab1)
    floor_ab1_4 = Floor(name = '4th', building_ab1)
    floor_ab1_5 = Floor(name = '5th', building_ab1)

    floor_b_sub  = Floor(name = 'Library Sub Floor', buidling_bedford)
    floor_b_main = Floor(name = 'Library Main Floor', buidling_bedford)
    floor_b_2 = Floor(name = 'Library 2nd Floor', buidling_bedford)
    # floor_b_