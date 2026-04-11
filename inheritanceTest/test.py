class Test:

    test_number = 2

    def test_value(self):
        print(self.test_number)


print(Test.test_number)
obj1 = Test()
obj1.test_value()
print(obj1.test_number)
obj2 = Test()
obj2.test_value()

Test.test_number = 4
obj1.test_number = 16
# print(Test.test_number)
# obj1 = Test()
# obj1.test_value()

# obj2 = Test()
# obj2.test_value()

print(obj1.test_number)
print(Test.test_number)
print(obj2.test_number)