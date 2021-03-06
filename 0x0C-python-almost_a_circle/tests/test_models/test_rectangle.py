import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingRectangle(unittest.TestCase):
    """class for Test Rectangle"""
    def test1_width(self):
        """testing width value"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "hello")

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, [9, 6])

        with self.assertRaises(TypeError):
            r3 = Rectangle(4, (7, 3))

        with self.assertRaises(TypeError):
            r4 = Rectangle(5, {'k': 8})

        with self.assertRaises(ValueError):
            r5 = Rectangle(6, 0)

        with self.assertRaises(ValueError):
            r6 = Rectangle(8, -7)

        with self.assertRaises(TypeError):
            r7 = Rectangle(9, 4.5)

        with self.assertRaises(TypeError):
            r8 = Rectangle(7, float('NaN'))

        with self.assertRaises(TypeError):
            r9 = Rectangle(7, float('inf'))

        with self.assertRaises(TypeError):
            r10 = Rectangle(1, True)

        with self.assertRaises(TypeError):
            r11 = Rectangle(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r12 = Rectangle()

        with self.assertRaises(TypeError):
            r13 = Rectangle(8, 5j)

        with self.assertRaises(TypeError):
            r14 = Rectangle(7, 1e100)

    def test2_height(self):
        """ testing height value """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "hello")

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 2, [9, 6])

        with self.assertRaises(TypeError):
            r3 = Rectangle(3, 4, (7, 3))

        with self.assertRaises(TypeError):
            r4 = Rectangle(4, 5, {'k': 8})

        with self.assertRaises(ValueError):
            r6 = Rectangle(6, 8, -7)

        with self.assertRaises(TypeError):
            r7 = Rectangle(7, 9, 4.5)

        with self.assertRaises(TypeError):
            r8 = Rectangle(8, 7, float('NaN'))

        with self.assertRaises(TypeError):
            r9 = Rectangle(9, 7, float('inf'))

        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 1, True)

        with self.assertRaises(TypeError):
            r11 = Rectangle(11, 1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r12 = Rectangle()

        with self.assertRaises(TypeError):
            r13 = Rectangle(12, 8, 5j)

        with self.assertRaises(TypeError):
            r14 = Rectangle(13, 7, 1e100)

    def test3_x_err(self):
        """ testing x value """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 1, 2, "hello")

        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, [9, 6])

        with self.assertRaises(TypeError):
            r3 = Rectangle(4, 3, 4, (7, 3))

        with self.assertRaises(TypeError):
            r4 = Rectangle(5, 4, 5, {'k': 8})

        with self.assertRaises(ValueError):
            r6 = Rectangle(6, 6, 8, -7)

        with self.assertRaises(TypeError):
            r7 = Rectangle(7, 7, 9, 4.5)

        with self.assertRaises(TypeError):
            r8 = Rectangle(8, 8, 7, float('NaN'))

        with self.assertRaises(TypeError):
            r9 = Rectangle(9, 9, 7, float('inf'))

        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 10, 1, True)

        with self.assertRaises(TypeError):
            r11 = Rectangle(11, 1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r12 = Rectangle()

        with self.assertRaises(TypeError):
            r13 = Rectangle(11, 12, 8, 5j)

        with self.assertRaises(TypeError):
            r14 = Rectangle(12, 13, 7, 1e100)

    def test4_x(self):
        """ testing x value """
        rect = Rectangle(9, 8, 0)
        self.assertEqual(rect.x, 0)

    def test4_y_err(self):
        """ testing y value """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 1, 2, "hello")

        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, [9, 6])

        with self.assertRaises(TypeError):
            r3 = Rectangle(4, 3, 4, (7, 3))

        with self.assertRaises(TypeError):
            r4 = Rectangle(5, 4, 5, {'k': 8})

        with self.assertRaises(ValueError):
            r6 = Rectangle(6, 6, 8, -7)

        with self.assertRaises(TypeError):
            r7 = Rectangle(7, 7, 9, 4.5)

        with self.assertRaises(TypeError):
            r8 = Rectangle(8, 8, 7, float('NaN'))

        with self.assertRaises(TypeError):
            r9 = Rectangle(9, 9, 7, float('inf'))

        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 10, 1, True)

        with self.assertRaises(TypeError):
            r11 = Rectangle(11, 1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r12 = Rectangle()

        with self.assertRaises(TypeError):
            r13 = Rectangle(11, 12, 8, 5j)

        with self.assertRaises(TypeError):
            r14 = Rectangle(12, 13, 7, 1e100)

    def test4_y(self):
        """ test y"""
        rect = Rectangle(9, 8, 6, 0)
        self.assertEqual(rect.y, 0)

    def test5_areaRect(self):
        Base._Base__nb_objects = 0
        """ test area"""
        rect = Rectangle(4, 4)
        self.assertEqual(rect.area(), 16)

    def test6_reassign(self):
        """ test reasign values"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.x = 1
        self.assertEqual(rect.x, 1)

        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.width = 3
        self.assertEqual(rect1.width, 3)

        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.y = 0
        self.assertEqual(rect1.y, 0)

        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.height = 3
        self.assertEqual(rect1.height, 3)

    def test6_reassign_err(self):
        """ testing reassign """
        with self.assertRaises(ValueError):
            rect2 = Rectangle(1, 2, 3, 4, 5)
            rect2.width = -1

        with self.assertRaises(TypeError):
            rect3 = Rectangle(1, 2, 3, 4, 5)
            rect3.width = "hello"

        with self.assertRaises(TypeError):
            rect4 = Rectangle(1, 2, 3, 4, 5)
            rect4.width = [9, 6]

        with self.assertRaises(TypeError):
            rect5 = Rectangle(1, 2, 3, 4, 5)
            rect5.y = (7, 3)

        with self.assertRaises(TypeError):
            rect6 = Rectangle(1, 2, 3, 4, 5)
            rect6.height = {'k': 8}

        with self.assertRaises(ValueError):
            rect7 = Rectangle(1, 2, 3, 4, 5)
            rect7.height = 0

        with self.assertRaises(TypeError):
            rect8 = Rectangle(1, 2, 3, 4, 5)
            rect8.height = 4.5

        with self.assertRaises(TypeError):
            rect8 = Rectangle(1, 2, 3, 4, 5)
            rect8.height = float('NaN')

        with self.assertRaises(TypeError):
            rect9 = Rectangle(1, 2, 3, 4, 5)
            rect9.height = float('inf')

        with self.assertRaises(TypeError):
            rect9 = Rectangle(1, 2, 3, 4, 5)
            rect9.x = True

        with self.assertRaises(TypeError):
            rect10 = Rectangle(1, 2, 3, 4, 5)
            rect10.x = 5j

        with self.assertRaises(TypeError):
            rect11 = Rectangle(1, 2, 3, 4, 5)
            rect11.y = 1e100

    def test7_update(self):
        """ testing update """
        Base._Base__nb_objects = 0
        rect1 = Rectangle(7, 7, 7, 7, 7)
        self.assertEqual(str(rect1), "[Rectangle] (7) 7/7 - 7/7")

        rect2 = Rectangle(7, 7, 7, 7, 7)
        rect2.update(1, 1)
        self.assertEqual(str(rect2), "[Rectangle] (1) 7/7 - 1/7")

        rect3 = Rectangle(7, 7, 7, 7, 7)
        MyList = [1, 2, 3]
        rect3.update(*MyList)
        self.assertEqual(str(rect3), "[Rectangle] (1) 7/7 - 2/3")

        rect4 = Rectangle(7, 7, 7, 7, 7)
        MyList = [1, 2, 3, 4]
        rect4.update(*MyList)
        self.assertEqual(str(rect4), "[Rectangle] (1) 4/7 - 2/3")

        rect5 = Rectangle(7, 7, 7, 7, 7)
        MyList = []
        rect5.update(*MyList)
        self.assertEqual(str(rect5), "[Rectangle] (7) 7/7 - 7/7")

        rect6 = Rectangle(7, 7, 7, 7, 7)
        MyDict = {'width': 1, 'height': 1}
        rect6.update(**MyDict)
        self.assertEqual(str(rect6), "[Rectangle] (7) 7/7 - 1/1")

        rect7 = Rectangle(7, 7, 7, 7, 7)
        MyDict = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        rect7.update(**MyDict)
        self.assertEqual(str(rect7), "[Rectangle] (1) 1/1 - 1/1")

        rect7.update()
        self.assertEqual(str(rect7), "[Rectangle] (1) 1/1 - 1/1")

    def test7_update_err(self):
        """ testing update """
        Base._Base__nb_objects = 0

        with self.assertRaises(ValueError):
            rect8 = Rectangle(2, 2)
            rect8.update(1, -2)

        with self.assertRaises(TypeError):
            rect9 = Rectangle(2, 2)
            rect9.update(1, 2.7)

        with self.assertRaises(TypeError):
            rect10 = Rectangle(2, 2)
            rect10.update(1, float('NaN'))

        with self.assertRaises(TypeError):
            rect11 = Rectangle(2, 2)
            rect11.update(1, float('inf'))

        with self.assertRaises(TypeError):
            rect12 = Rectangle(2, 2)
            rect12.update(1, 1e100)

        with self.assertRaises(TypeError):
            rect12 = Rectangle(2, 2)
            rect12.update(1, 5j)

    def test8_str_err(self):
        """ test str"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect1 = Rectangle()
            rect1 = str(self)

        with self.assertRaises(TypeError):
            rect2 = Rectangle()
            rect2 = str(self)

    def test8_str_err(self):
        """ test str"""
        Base._Base__nb_objects = 0
        rect3 = Rectangle(1, 2)
        self.assertEqual(str(rect3), "[Rectangle] (1) 0/0 - 1/2")

        rect4 = Rectangle(1, 2, 3)
        self.assertEqual(str(rect4), "[Rectangle] (2) 3/0 - 1/2")

        rect5 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect5), "[Rectangle] (5) 3/4 - 1/2")

    def test9_1_todict(self):
        """ test to_dictionary """
        Base._Base__nb_objects = 0
        rect = Rectangle(1, 2, 3, 4, 5)
        rect1 = rect.to_dictionary()
        MyDict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        for i in MyDict:
            self.assertEqual(rect1[i], MyDict[i])

    def test10_2_todict(self):
        """ test to_dictionary """
        Base._Base__nb_objects = 0
        rect = Rectangle(1, 2)
        rect1 = rect.to_dictionary()
        MyDict = {'id': 1, 'width': 1, 'height': 2, 'x': 0, 'y': 0}
        for i in MyDict:
            self.assertEqual(rect1[i], MyDict[i])

    def test11_3_todict(self):
        """ test to_dictionary """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect = Rectangle()
            rect1 = rect.to_dictionary()

    def test12_4_todict(self):
        """ test to_dictionary """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect = Rectangle(None)
            rect1 = rect.to_dictionary()

    def test13_update_kwargs(self):
        """ test updating kwargs rectangle """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r2 = Rectangle(10, 10, 10, 10)
        r2.update(width=3)
        self.assertEqual(str(r2), "[Rectangle] (2) 10/10 - 3/10")

        r2 = Rectangle(10, 10, 10, 10)
        r2.update(x=1, height=4, width=3)
        self.assertEqual(str(r2), "[Rectangle] (7) 1/10 - 3/4")

    def test13_update_kwargs(self):
        """ test updating kwargs rectangle """
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 10, 10, 10)
            r3.update(width=0)

        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 10, 10, 10)
            r4.update(x=-1)

        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(width=4.2)

        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 10, 10, 10)
            r6.update(x=None)
