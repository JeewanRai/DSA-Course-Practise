class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None  # You can initialize any instance variable here
        return cls._instance

# Example usage:
singleton1 = Singleton()
singleton1.value = "Hello from singleton1"

singleton2 = Singleton()
singleton2.value = "Hello from singleton2"

# Both singleton1 and singleton2 still refer to the same instance
print(singleton1.value)  # Outputs: Hello from singleton2
print(singleton2.value)  # Outputs: Hello from singleton2
