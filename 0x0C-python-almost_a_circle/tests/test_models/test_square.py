import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingSquare(unittest.TestCase):
    """class for Test Square"""
    def test1_size(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s1 = Square("hello")

        with self.assertRaises(TypeError):
            s2 = Square([9, 6])

        with self.assertRaises(TypeError):
            s3 = Square((7, 3))

        with self.assertRaises(TypeError):
            s4 = Square({'k': 8})

        with self.assertRaises(ValueError):
            s5 = Square(0)

        with self.assertRaises(ValueError):
            s6 = Square(-7)

        with self.assertRaises(TypeError):
            s7 = Square(4.5)

        with self.assertRaises(TypeError):
            s8 = Square(float('NaN'))

        with self.assertRaises(TypeError):
            s9 = Square(float('inf'))

        with self.assertRaises(TypeError):
            s10 = Square(True)

        with self.assertRaises(TypeError):
            s11 = Square(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            s12 = Square()

        with self.assertRaises(TypeError):
            s13 = Square(5j)

        with self.assertRaises(TypeError):
            s14 = Square(1e100)

    def test2_x_err(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s1 = Square(2, "hello")

        with self.assertRaises(TypeError):
            s2 = Square(2, [9, 6])

        with self.assertRaises(TypeError):
            s3 = Square(4, (7, 3))

        with self.assertRaises(TypeError):
            s4 = Square(4, {'k': 8})

        with self.assertRaises(ValueError):
            s5 = Square(6, -7)

        with self.assertRaises(TypeError):
            s6 = Square(2, 4.5)

        with self.assertRaises(TypeError):
            s7 = Square(4, float('NaN'))

        with self.assertRaises(TypeError):
            s8 = Square(6, float('inf'))

        with self.assertRaises(TypeError):
            s9 = Square(4, True)

        with self.assertRaises(TypeError):
            s10 = Square(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            s12 = Square(2, 5j)

        with self.assertRaises(TypeError):
            s13 = Square(2, 1e100)

    def test2_x(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        s11 = Square(9, 0)
        self.assertEqual(s11.x, 0)

    def test3_y_err(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s1 = Square(2, 3, "hello")

        with self.assertRaises(TypeError):
            s2 = Square(2, 3, [9, 6])

        with self.assertRaises(TypeError):
            s3 = Square(4, 3, (7, 3))

        with self.assertRaises(TypeError):
            s4 = Square(4, 3, {'k': 8})

        with self.assertRaises(ValueError):
            s5 = Square(6, 3, -7)

        with self.assertRaises(TypeError):
            s6 = Square(2, 3, 4.5)

        with self.assertRaises(TypeError):
            s7 = Square(4, 3, float('NaN'))

        with self.assertRaises(TypeError):
            s8 = Square(6, 3, float('inf'))

        with self.assertRaises(TypeError):
            s9 = Square(4, 3, True)

        with self.assertRaises(TypeError):
            s10 = Square(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            s12 = Square(2, 2, 5j)

        with self.assertRaises(TypeError):
            s13 = Square(2, 3, 1e100)

    def test3_y(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        s11 = Square(9, 3, 0)
        self.assertEqual(s11.y, 0)

    def test4_area(self):
        """Test area Square"""
        Base._Base__nb_objects = 0
        sq = Square(4, 4)
        self.assertEqual(sq.area(), 16)

    def test5_reassign(self):
        """ test reasign values"""
        Base._Base__nb_objects = 0
        rect = Square(1, 2, 3, 4)
        rect.x = 1
        self.assertEqual(rect.x, 1)

        rect1 = Square(1, 2, 3, 4)
        rect1.size = 5
        self.assertEqual(rect1.size, 5)

        rect1 = Square(1, 2, 3, 4)
        rect1.x = 0
        self.assertEqual(rect1.x, 0)

    def test5_reassign_err(self):
        """ test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            rect2 = Square(1, 2, 3, 4)
            rect2.size = -1

        with self.assertRaises(TypeError):
            rect3 = Square(1, 2, 3, 4)
            rect3.size = "hello"

        with self.assertRaises(TypeError):
            rect4 = Square(1, 2, 3, 4)
            rect4.size = [9, 6]

        with self.assertRaises(TypeError):
            rect5 = Square(1, 2, 3, 4)
            rect5.y = (7, 3)

        with self.assertRaises(TypeError):
            rect6 = Square(1, 2, 3, 4)
            rect6.size = {'k': 8}

        with self.assertRaises(ValueError):
            rect7 = Square(1, 2, 3, 4)
            rect7.size = 0

        with self.assertRaises(TypeError):
            rect8 = Square(1, 2, 3, 4)
            rect8.size = 4.5

        with self.assertRaises(TypeError):
            rect8 = Square(1, 2, 3, 4)
            rect8.size = float('NaN')

        with self.assertRaises(TypeError):
            rect9 = Square(1, 2, 3, 4)
            rect9.size = float('inf')

        with self.assertRaises(TypeError):
            rect9 = Square(1, 2, 3, 4)
            rect9.x = True

        with self.assertRaises(TypeError):
            rect10 = Square(1, 2, 3, 4)
            rect10.x = 5j

        with self.assertRaises(TypeError):
            rect11 = Square(1, 2, 3, 4)
            rect11.y = 1e100

    def test6_update(self):
        """ testing update """
        Base._Base__nb_objects = 0
        rect1 = Square(7, 7, 7, 7)
        self.assertEqual(str(rect1), "[Square] (7) 7/7 - 7")

        rect2 = Square(7, 7, 7, 7)
        rect2.update(1, 1)
        self.assertEqual(str(rect2), "[Square] (1) 7/7 - 1")

        rect3 = Square(7, 7, 7, 7)
        MyList = [1, 2, 3]
        rect3.update(*MyList)
        self.assertEqual(str(rect3), "[Square] (1) 3/7 - 2")

        rect4 = Square(7, 7, 7, 7)
        MyList = [1, 2, 3, 4]
        rect4.update(*MyList)
        self.assertEqual(str(rect4), "[Square] (1) 3/4 - 2")

        rect5 = Square(7, 7, 7, 7)
        MyList = []
        rect5.update(*MyList)
        self.assertEqual(str(rect5), "[Square] (7) 7/7 - 7")

        rect6 = Square(7, 7, 7, 7)
        MyDict = {'width': 1, 'height': 1}
        rect6.update(**MyDict)
        self.assertEqual(str(rect6), "[Square] (7) 7/7 - 7")

        rect7 = Square(7, 7, 7, 7)
        MyDict = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        rect7.update(**MyDict)
        self.assertEqual(str(rect7), "[Square] (1) 1/1 - 7")

        rect7.update()
        self.assertEqual(str(rect7), "[Square] (1) 1/1 - 7")

    def test6_update_err(self):
        """ testing update """
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            rect8 = Square(2, 2)
            rect8.update(1, -2)

        with self.assertRaises(TypeError):
            rect9 = Square(2, 2)
            rect9.update(1, 2.7)

        with self.assertRaises(TypeError):
            rect10 = Square(2, 2)
            rect10.update(1, float('NaN'))

        with self.assertRaises(TypeError):
            rect11 = Square(2, 2)
            rect11.update(1, float('inf'))

        with self.assertRaises(TypeError):
            rect12 = Square(2, 2)
            rect12.update(1, 1e100)

        with self.assertRaises(TypeError):
            rect12 = Square(2, 2)
            rect12.update(1, 5j)

    def test7_str_err(self):
        """ test str"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect1 = Square()
            rect1 = str(self)

        with self.assertRaises(TypeError):
            rect2 = Square()
            rect2 = str(self)

    def test7_str(self):
        """ test str"""
        Base._Base__nb_objects = 0
        rect3 = Square(1, 2)
        self.assertEqual(str(rect3), "[Square] (1) 2/0 - 1")

        rect4 = Square(1, 2, 3)
        self.assertEqual(str(rect4), "[Square] (2) 2/3 - 1")

        rect5 = Square(1, 2, 3, 4)
        self.assertEqual(str(rect5), "[Square] (4) 2/3 - 1")

    def test8_update_kwargs(self):
        """ test updating kwargs square """
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10, 10)
        r1.update(size=1)
        self.assertEqual(str(r1), "[Square] (10) 10/10 - 1")

        r2 = Square(10, 10, 10, 10)
        r2.update(size=3)
        self.assertEqual(str(r2), "[Square] (10) 10/10 - 3")

        r2 = Square(10, 10, 10, 10)
        r2.update(x=1, sizet=4)
        self.assertEqual(str(r2), "[Square] (10) 1/10 - 10")

    def test8_update_kwargs_err(self):
        """ test updating kwargs square """
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Square(10, 10, 10, 10)
            r3.update(size=0)

        with self.assertRaises(ValueError):
            r4 = Square(10, 10, 10, 10)
            r4.update(x=-1)

        with self.assertRaises(TypeError):
            r5 = Square(10, 10, 10, 10)
            r5.update(size=4.2)

        with self.assertRaises(TypeError):
            r6 = Square(10, 10, 10, 10)
            r6.update(x=None)

    def test9_Sq_todict(self):
        """Square test to_dictionary 1"""
        sq = Square(1, 2, 3, 4)
        sq1 = sq.to_dictionary()
        MyDict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        for i in MyDict:
            self.assertEqual(sq1[i], MyDict[i])

    def test10_Sq_todict(self):
        """Square test to_dictionary 2"""
        sq = Square(1)
        sq1 = sq.to_dictionary()
        MyDict = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        for i in MyDict:
            self.assertEqual(sq1[i], MyDict[i])

    def test11_Sq_todict(self):
        """Square test to_dictionary 3"""
        with self.assertRaises(TypeError):
            sq = Square()
            sq1 = sq.to_dictionary()

    def test12_Sq_todict(self):
        """Square test to_dictionary 4"""
        with self.assertRaises(TypeError):
            sq = Square(None)
            sq1 = sq.to_dictionary()

    def test13_json_to_file8(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        Square.save_to_file(None)
        with open("Square.json") as myfile:
            self.assertEqual("[]", myfile.read())
