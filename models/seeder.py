from building import Building
from floor import Floor
from bin import Bin
from direction import Direction

def seed():
    ##
    # CREATE DIRECTIONS
    ##
    # Bedford bin directions
    dir_b_lib_sub = Direction(step = 1, message = 'Towards the elevator opposite of the <strong>Printing Room</strong> is a trash can').put()
    dir_b_lib_main = Direction(step = 1, message = 'Under the stairs by the <strong>Printing Room</strong> is recycling and trash cans').put()

    ##
    # CREATE BINS
    ##
    bin_b_lib_sub = Bin(directions = [dir_b_lib_sub]).put()
    bin_b_lib_main = Bin(directions = [dir_b_lib_main]).put()

    ##
    # CREATE FLOORS
    ##
    floor_ab1_sub = Floor(name = 'Sub', bins = []).put()
    floor_ab1_main = Floor(name = 'Main', bins = []).put()
    floor_ab1_2 = Floor(name = '2nd', bins = []).put()
    floor_ab1_3 = Floor(name = '3rd', bins = []).put()
    floor_ab1_4 = Floor(name = '4th', bins = []).put()
    floor_ab1_5 = Floor(name = '5th', bins = []).put()
    ab1_floors = [
        floor_ab1_sub,
        floor_ab1_main,
        floor_ab1_2,
        floor_ab1_3,
        floor_ab1_4,
        floor_ab1_5
    ]

    floor_b_lib_sub  = Floor(name = 'Library Sub', bins = [
        bin_b_lib_sub
    ]).put()
    floor_b_lib_main = Floor(name = 'Library Main', bins = [
        bin_b_lib_main
    ]).put()
    floor_b_lib_2 = Floor(name = 'Library 2nd', bins = []).put()
    floor_b_1 = Floor(name = '1st', bins = []).put()
    floor_b_2 = Floor(name = '2nd', bins = []).put()
    bedford_floors = [
        floor_b_lib_sub,
        floor_b_lib_main,
        floor_b_lib_2,
        floor_b_1,
        floor_b_2
    ]

    ##
    # CREATE BUILDINGS
    ##
    building_ab1 = Building(street_number = 1638, name = 'AB-1', image = '', floors = ab1_floors).put()
    building_bedford = Building(street_number = 1650, name = 'Bedford', image = '', floors = bedford_floors).put()
