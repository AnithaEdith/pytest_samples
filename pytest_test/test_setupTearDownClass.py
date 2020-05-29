class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass!")

    @classmethod
    def teardown_class(cls):
        print("TearDown TestClass!")

    def setup_method(self, method):
        if method == self.test1:
            print("\n setting up test1!")
        elif method == self.test2:
            print("\n setting up test2!")
        else:
            print("\n setting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\n Tearing Down  test1!")
        elif method == self.test2:
            print("\n Tearing Down test2!")
        else:
            print("\n Tearing Down unknown test!")

    def test1(self):
        print("Executing test1")
        assert True


    def test2(self):
        print("Executing test2")
        assert True