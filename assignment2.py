# Assignment 1: Design Your Own Class

# 🔹 Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# 🔹 Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery
        self.is_on = False

    # Method to turn phone on
    def power_on(self):
        self.is_on = True
        return f"{self.brand} {self.model} is now ON 🔋"
    
    # Method to turn phone off
    def power_off(self):
        self.is_on = False
        return f"{self.brand} {self.model} is now OFF ❌"
    
    # Method to take a picture
    def take_photo(self):
        if self.is_on:
            return f"📸 Photo taken with {self.brand} {self.model}!"
        else:
            return f"⚠️ Cannot take photo, {self.model} is OFF."
    
    # Encapsulation Example (Private battery update)
    def __update_battery(self, usage):
        self.battery -= usage
        if self.battery < 0:
            self.battery = 0
    
    # Public method to simulate usage
    def use_phone(self, hours):
        self.__update_battery(hours * 10)
        return f"{self.model} used for {hours} hours, battery at {self.battery}%."


# 🔹 Polymorphism Example (different device types)
class Tablet(Device):
    def device_info(self):
        return f"Tablet: {self.brand} {self.model} - Bigger Screen 📺"


# --- Testing the Classes ---
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S22", "256GB", 100)
    tablet1 = Tablet("Apple", "iPad Pro")

    print(phone1.device_info())
    print(phone1.power_on())
    print(phone1.take_photo())
    print(phone1.use_phone(3))
    print(phone1.power_off())

    print(tablet1.device_info())  # Polymorphism: different behavior
