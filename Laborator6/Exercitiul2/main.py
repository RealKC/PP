class BaseClass:
    num_base_calls = 0

    def call_me(self, caller):
        print("Apel metoda din BaseClass, caller=", caller)
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self, caller):
        print("Apel metoda din LeftSubclass, caller=", caller)
        # super().call_me("LeftSubclass")
        BaseClass.call_me(self, "LeftSubclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self, caller):
        print("Apel metoda din RightSubclass, caller=", caller)
        # super().call_me("RightSubclass")
        BaseClass.call_me(self, "RightSubclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self, caller):
        print("Apel metoda din Subclass, caller=", caller)
        # super().call_me("Subclass")
        BaseClass.call_me(self, "Subclass")
        # super().call_me("Subclass")
        BaseClass.call_me(self, "Subclass")
        self.num_sub_calls += 1


# Using super().call_me() ends up calling both LeftSubclass.call_me() and RightSubclass.call_me()
# BaseClass.call_me() only calls that method

if __name__ == '__main__':
    subclass_instance = Subclass()
    print(Subclass.__mro__)
    subclass_instance.call_me("__main__")
    print(subclass_instance.num_sub_calls,
          subclass_instance.num_left_calls,
          subclass_instance.num_right_calls,
          subclass_instance.num_base_calls)
