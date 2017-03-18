#this is the test suite for "Luftrobot". This should be an extension of robot simulator.
import unittest

from luftrobot_simulator import Luftrobot, NORTH, EAST, SOUTH, WEST


class RobotTests(unittest.TestCase):

    def test_init(self):
        luftrobot = Luftrobot()
        self.assertEqual((0, 0, 0), luftrobot.coordinates)
        self.assertEqual(NORTH, luftrobot.bearing)

    def test_setup(self):
        luftrobot = Luftrobot(SOUTH, -1, 1, 0)
        self.assertEqual((-1, 1,0), luftrobot.coordinates)
        self.assertEqual(SOUTH, luftrobot.bearing)

    def test_turn_right(self):
        luftrobot = Luftrobot()
        for direction in [EAST, SOUTH, WEST, NORTH]:
            luftrobot.turn_right()
            self.assertEqual(luftrobot.bearing, direction)

    def test_turn_left(self):
        luftrobot = Luftrobot()
        for direction in [WEST, SOUTH, EAST, NORTH]:
            luftrobot.turn_left()
            self.assertEqual(luftrobot.bearing, direction)

    def test_advance_positive_north(self):
        luftrobot = Luftrobot(NORTH, 0, 0,0)
        luftrobot.advance()
        self.assertEqual((0, 1,0), luftrobot.coordinates)
        self.assertEqual(NORTH, luftrobot.bearing)

    def test_advance_positive_east(self):
        luftrobot = Luftrobot(EAST, 0, 0,0)
        luftrobot.advance()
        self.assertEqual((1, 0,0), luftrobot.coordinates)
        self.assertEqual(EAST, luftrobot.bearing)

    def test_advance_negative_south(self):
        luftrobot = Luftrobot(SOUTH, 0, 0,0)
        luftrobot.advance()
        self.assertEqual((0,-1,0), luftrobot.coordinates)
        self.assertEqual(SOUTH, luftrobot.bearing)
    
    def test_goback_negative_north(self):
        luftrobot = Luftrobot(0,0,0)
        luftrobot.goback()
        self.assertEqual((0,-1,0), luftrobot.coordinates)
        self.assertEqual(NORTH, luftrobot.bearing)  

    #def test_altitude(self): #see if luftrobot has given altitude
    def test_ascend(self):
        luftrobot = Luftrobot()
        luftrobot.ascend()
        self.assertEqual((0, 0, 1), luftrobot.coordinates)

    def test_descend(self):
        luftrobot = Luftrobot(NORTH, 0,0,1)
        luftrobot.descend()
        self.assertEqual((0, 0, 0), luftrobot.coordinates)

    def test_warp(self):
        luftrobot = Luftrobot(NORTH, 0, 0,0)
        luftrobot.warp(5)
        self.assertEqual((0,5,0), luftrobot.coordinates)

    def test_warp_east(self):
        luftrobot = Luftrobot(EAST,0 ,0 ,0)
        luftrobot.warp(5)
        self.assertEqual((5,0,0), luftrobot.coordinates)

    def test_simulate_prog1a(self): 
    #Robot moves and then flies up (U) thrice and down (D) once
        luftrobot = Luftrobot()
        luftrobot.simulate("LAARALAUUUD")
        self.assertEqual((-3,1,2), luftrobot.coordinates)
        self.assertEqual(WEST,luftrobot.bearing)

    def test_simulate_prog1b(self): #Simple case, robot don't fly. 
        luftrobot = Luftrobot(NORTH, 0, 0,0)
        luftrobot.simulate("LAAARALA")
        self.assertEqual((-3, 1,0), luftrobot.coordinates)
        self.assertEqual(WEST, luftrobot.bearing)

    def test_simulate_prog1c(self): #Robot ordered to descend into the ground
        luftrobot = Luftrobot()
        luftrobot.simulate("LAARALAD")
        #error handling must occur, and the Robot coordinates must not go into the ground
        #self.assertRaises(ValueError, msg="FYI, I CAN'T DESCEND INTO GROUND, IDIOT")
        self.assertEqual((-3,1,0), luftrobot.coordinates) 
        

    def test_simulate_prog1d(self): #Robot goes backward (B)
        luftrobot = Luftrobot()
        luftrobot.simulate("LAAARALAB") #the robot goes backward (B)
        self.assertEqual((-4,1,0), luftrobot.coordinates)
        self.assertEqual(WEST,luftrobot.bearing)

    




if __name__ == '__main__':
    unittest.main()
