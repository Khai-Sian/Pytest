#import pytest

# @pytest.fixture(scope='class')
# def fix_apple():
    
#     nums = [1, 2, 3]
#     list_obj = []

#     for num in nums:
#         list_obj.append(apple(num))

#     return list_obj


class apple:
    def __init__(self, value):
        self.a = value

    def __init__(self):
        print("Parent Constructor")

class BaseFunc():

    def __init__(self):
        print("Hello")

    def do_something(self):
        print("BaseFunc -  Doing Something")

    def look_something(self, value):
        print("BaseFunc - Looking Something")

class BaseElementValidator(BaseFunc):

    # def __init__(self, value):
    #     self.a = value

    def test_only(self, fix_apple):
        print("Base - only")
        
        super().do_something()

        for apple in fix_apple:
            assert apple.a > 0

    def test_RequiredAttributes(self):
        print("Base - test_RequiredAttributes")
        assert True == True

    def test_OptionalAttributes(self):
        print("Base - test_OptionalAttributes")
        assert 0 == 0

class Test_XmlEv(BaseElementValidator):

    def test_RequiredAttributes(self, fix_apple):
        print("Child - test_RequiredAttributes")

        for apple in fix_apple:
            assert apple.a > 0

    def test_OptionalAttributes(self, fix_apple):
        print("Child - test_OptionalAttributes")
        
        for apple in fix_apple:
            assert apple.a > 0

# import pytest

# class House:
#     def is_habitable(self):
#         print("\nHouse - is_habitable")
#         return True

#     def is_on_the_ground(self):
#         print("House - is_on_the_ground")
#         return True


# class TreeHouse(House):
#     def is_on_the_ground(self):
#         print("TreeHouse - is_on_the_ground")
#         return False

# @pytest.fixture(scope='class')
# def house():
#     print("Return House")
#     return House()


# @pytest.fixture(scope='class')
# def tree_house():
#     print("Return TreeHouse")
#     return TreeHouse()

# class TestHouse:
#     def test_habitability(self, house):
#         print("Test - house.is_habitable")
#         assert house.is_habitable()

#     def test_groundedness(self, house):
#         print("Test - house.is_on_the_ground")
#         assert house.is_on_the_ground()


# class TestTreeHouse(TestHouse):
    
#     @pytest.fixture
#     def house(self, tree_house):
#         return tree_house

    
#     def test_groundedness(self, house):
#         print("Test - tree_house.is_on_the_ground")
#         assert not house.is_on_the_ground()

# class TestTreeHouse(TestHouse):

#     @pytest.fixture
#     def house(self, tree_house):
#         return tree_house

#     def test_groundedness(self, house):
#         assert not house.is_on_the_ground()