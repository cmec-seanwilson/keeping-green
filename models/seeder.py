from building import Building
from floor import Floor
from bin import Bin
from direction import Direction
from hotspot import HotSpot

def seed():
    ##
    # CREATE DIRECTIONS
    ##
    # Bedford bin directions
    dir_b_lib = Direction(step = 1, message = '<strong>Heads up:</strong> No food or drink is allowed in the library').put()
    dir_b_lib_sub = Direction(step = 1, message = 'Towards the elevator opposite of the <strong>Printing Room</strong> is a trash can').put()
    dir_b_lib_main = Direction(step = 1, message = 'Under the stairs by the <strong>Printing Room</strong> is recycling and trash cans').put()
    dir_b_lib_2 = Direction(step = 1, message = 'By the <strong>glass entrance</strong>, in the north-west corner are bins').put()
    dir_b_main = Direction(step = 1, message = 'Inside <strong>Starbucks</strong> and under the steps are bins').put()
    dir_b_main_2 = Direction(step = 2, message = 'If you\'re in the middle of the main floor there are bins at the entrance or <strong>Auditorium</strong>').put()
    dir_b_2_1 = Direction(step = 1, message = 'Adjacent to the <strong>Language Lab</strong> are bins').put()
    dir_b_2_2 = Direction(step = 1, message = 'There is a bin between the stairs leading down near the entrance of the <strong>Computer Lab</strong>').put()
    dir_ab1_main_front = Direction(step = 1, message = 'There are recycling and trash bins behind the <strong>Security Desk</strog> under the steps leading to the <strong>Cafeteria</strong>').put()
    dir_ab1_main_middle = Direction(step = 1, message = 'If you\'re in the middle of the main floor, walk towards the entrance or walk towards the <strong>Auditorium</strong>').put()
    dir_ab1_sub_1_1 = Direction(step = 1, message = 'If you\'re facing the stairs, between the <strong>Public Safety</strong> room and the stairs leading to the main floor are bins on your left or right if you\'re facing the <strong>Public Safety</strong> room').put()
    dir_ab1_sub_2_1 = Direction(step = 1, message = 'There is a bin adjacent to class <strong>C09</strong>').put()
    dir_ab1_2_1 = Direction(step=1, message = 'Near the <strong>Main Elevator</strong>, there are bins in the cafeteria').put()
    dir_ab1_2_2 = Direction(step = 1, message = 'There is bin walking opposite from the cafeteria under the <strong>Nurse</strong> sign').put()
    dir_ab1_2_3= Direction(step= 1, message = 'There are multiple bins in a line separate by a small distance from each other if you\'re walking from the <strong>Elevator</strong> to the <strong>West</strong>').put()
    dir_ab1_3= Direction(step= 1, message = 'There are multiple bins in a line separate by a small distance from each other if you\'re walking from the <strong>Elevator</strong> to the <strong>West</strong>').put()
    dir_ab1_4 = Direction(step = 1, message = 'There are multiple bins in a line separate by a small distance from each other if you\'re walking from the <strong>Elevator</strong> to the <strong>West</strong>').put()
    dir_ab1_5= Direction(step = 1, message = 'There are multiple bins in a line separate by a small distance from each other if you\'re walking from the <strong>Elevator</strong> to the <strong>West</strong>').put()

    ##
    # CREATE BINS
    ##
    bin_b_lib_sub = Bin(directions = [dir_b_lib, dir_b_lib_sub]).put()
    bin_b_lib_main = Bin(directions = [dir_b_lib, dir_b_lib_main]).put()
    bin_b_lib_2 = Bin(directions = [dir_b_lib_2]).put()
    bin_b_main = Bin(directions = [dir_b_main, dir_b_main_2]).put()
    bin_b_2 = Bin(directions = [dir_b_2_1, dir_b_2_2]).put()
    bin_ab1_main_front = Bin(directions = [dir_ab1_main_front]).put()
    bin_ab1_main_middle = Bin(directions = [dir_ab1_main_middle]).put()
    bin_ab1_sub_1 = Bin(directions = [dir_ab1_sub_1_1]).put()
    bin_ab1_sub_2 = Bin(directions = [dir_ab1_sub_2_1])
    bin_ab1_2 = Bin(directions = [dir_ab1_2_1]).put()
    bin_ab1_2_2 = Bin(directions = [dir_ab1_2_2]).put()
    bin_ab1_2_3 = Bin(directions = [dir_ab1_2_3]).put()
    bin_ab1_3 = Bin(directions = [dir_ab1_3]).put()
    bin_ab1_4 = Bin(directions = [dir_ab1_4]).put()
    bin_ab1_5 = Bin(directions = [dir_ab1_5]).put()

    ##
    # CREATE HOTSPOTS
    ##
    floor_ab1_main_hotspot_1 = HotSpot(pitch = 8, yaw = 230).put()
    floor_ab1_main_hotspot_2 = HotSpot(pitch = 6, yaw = 120).put()

    ##
    # CREATE FLOORS
    ##
    floor_ab1_sub = Floor(name = 'Sub', bins = [
        bin_ab1_sub_1_1,
        bin_ab1_sub_2_1
    ]).put()
    floor_ab1_main = Floor(name = 'Main', bins = [
        bin_ab1_main_front,
        bin_ab1_main_middle
    ], hotspots = [
        floor_ab1_main_hotspot_1,
        floor_ab1_main_hotspot_2
    ]).put()
    floor_ab1_2 = Floor(name = '2nd', bins = [
        bin_ab1_2,
        bin_ab1_2_2,
        bin_ab1_2_3
    ]).put()
    floor_ab1_3 = Floor(name = '3rd', bins = [
        bin_ab1_3
    ]).put()
    floor_ab1_4 = Floor(name = '4th', bins = [
        bin_ab1_4
    ]).put()
    floor_ab1_5 = Floor(name = '5th', bins = [
        bin_ab1_5
    ]).put()
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
    floor_b_lib_2 = Floor(name = 'Library 2nd', bins = [
        bin_b_lib_sub
    ]).put()
    floor_b_1 = Floor(name = '1st', bins = [
        bin_b_main
    ]).put()
    floor_b_2 = Floor(name = '2nd', bins = [
        bin_b_2
    ]).put()
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
