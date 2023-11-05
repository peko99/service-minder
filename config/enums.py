# Copyright 2023 Marin Pejcin

from enum import Enum


class FuelTypeEnum(str, Enum):
    DIESEL = "diesel"
    PETROL = "petrol"
    LPG = "lpg"
    ELECTRIC = "electric"
    HYBRID = "hybrid"


class ExpenseCategoryEnum(str, Enum):
    SERVICE = "service"
    REGISTRATION = "registration"
    FINE = "fine"
    OTHER = "other"


class FineCategoryEnum(str, Enum):
    PARKING = "parking"
    SPEEDING = "speeding"
    SEATBELT = "seatbelt"
    DUI = "dui"
    PHONE = "phone"
    RED_LIGHT = "red light"
    OTHER = "other"


class PartsCategoryEnum(str, Enum):
    FLUIDS = "fluids"
    FILTERS = "filters"
    TIRES = "tires"
    WHEELS = "wheels"
    BRAKES = "brakes"
    SPARK_PLUGS = "spark plugs"
    WIPERS = "wipers"
    ENGINE = "engine"
    SUSPENSION = "suspension"
    GEARBOX = "gearbox"
    ELECTRICS = "electrics"
    TOWING = "towing"
    OTHER = "other"
