from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, name: str, unit: str):
        self.name = name
        self.unit = unit

    @abstractmethod
    def read(self) -> float:
        pass


class TemperatureSensor(Sensor):
    def __init__(self):
        super().__init__(name="temperature", unit="°C")

    def read(self) -> float:
        return round(random.uniform(-10, 35), 1)


class HumiditySensor(Sensor):
    def __init__(self):
        super().__init__(name="humidity", unit="%")

    def read(self) -> float:
        return round(random.uniform(20, 95), 1)


class WeatherStation:
    def __init__(self, city: str):
        self.city = city
        self.__sensors: list[Sensor] = []

    def add_sensor(self, sensor: Sensor) -> None:
        if not isinstance(sensor, Sensor):
            raise TypeError("sensor має бути екземпляром Sensor або його нащадка")

        self.__sensors.append(sensor)

    def __define_condition(self, temperature: float, humidity: float) -> str:
        if humidity >= 80 and temperature > 0:
            return "волого, можлива мряка"
        if temperature <= 0:
            return "морозно"
        if temperature <= 10:
            return "прохолодно"
        if temperature >= 28 and humidity >= 60:
            return "спекотно і волого"
        if temperature >= 28:
            return "спекотно"
        if 18 <= temperature <= 27 and humidity < 75:
            return "комфортно"

        return "мінлива погода"

    def report(self) -> dict:
        temperature_c = None
        humidity_percent = None

        for sensor in self.__sensors:
            value = sensor.read()

            if sensor.name == "temperature":
                temperature_c = value
            elif sensor.name == "humidity":
                humidity_percent = value

        if temperature_c is None:
            raise ValueError("Не додано датчик температури")

        if humidity_percent is None:
            raise ValueError("Не додано датчик вологості")

        condition = self.__define_condition(temperature_c, humidity_percent)

        return {
            "city": self.city,
            "temperature_c": temperature_c,
            "humidity_percent": humidity_percent,
            "condition": condition
        }


def get_weather(city: str) -> dict:
    station = WeatherStation(city)
    station.add_sensor(TemperatureSensor())
    station.add_sensor(HumiditySensor())

    return station.report()