from pydantic import BaseModel, PositiveInt, FiniteFloat, PositiveFloat, NonNegativeInt
from typing import Optional
from typing_extensions import Literal
import datetime as dt

class EspecificacoesCasa(BaseModel):
    """
    The data model that represents the necessary specifications of a house for the algorithm to predict the estimated price.

    Attributes:
        host_listings_count (PositiveInt): The number of houses the host has.
        latitude (FiniteFloat): The latitude of the house location.
        longitude (FiniteFloat): The longitude of the house location.
        accommodates (PositiveInt): The number of guests the house can accommodate.
        bathrooms (PositiveInt): The number of bathrooms in the house.
        bedrooms (PositiveInt): The number of bedrooms in the house.
        beds (PositiveInt): The number of beds in the house.
        extra_people (NonNegativeInt): The number of additional people allowed beyond the standard accommodates.
        minimum_nights (PositiveInt): The minimum number of nights required for a stay.
        n_amenities (PositiveInt): The number of amenities provided in the house.
        room_type_Entire_home_apt (Literal[1, 0]): Whether the entire home or apartment is offered (1 for yes, 0 for no).
        host_is_superhost (Optional[Literal[0, 1]]): Whether the host is a superhost (1 for yes, 0 for no). Defaults to 0.
        instant_bookable (Optional[Literal[0, 1]]): Whether the listing is instantly bookable (1 for yes, 0 for no). Defaults to 1.
        ano (Optional[PositiveInt]): The year the listing is relevant to. Defaults to the current year.
        mes (Optional[PositiveInt]): The month the listing is relevant to. Defaults to the current month.
        property_type_Apartment (Optional[Literal[1, 0]]): Whether the property type is an apartment (1 for yes, 0 for no). Defaults to 0.
        property_type_Bed_and_breakfast (Optional[Literal[1, 0]]): Whether the property type is a bed and breakfast (1 for yes, 0 for no). Defaults to 0.
        property_type_Condominium (Optional[Literal[1, 0]]): Whether the property type is a condominium (1 for yes, 0 for no). Defaults to 0.
        property_type_Guest_suite (Optional[Literal[1, 0]]): Whether the property type is a guest suite (1 for yes, 0 for no). Defaults to 0.
        property_type_Guesthouse (Optional[Literal[1, 0]]): Whether the property type is a guesthouse (1 for yes, 0 for no). Defaults to 0.
        property_type_Hostel (Optional[Literal[1, 0]]): Whether the property type is a hostel (1 for yes, 0 for no). Defaults to 0.
        property_type_House (Optional[Literal[1, 0]]): Whether the property type is a house (1 for yes, 0 for no). Defaults to 0.
        property_type_Loft (Optional[Literal[1, 0]]): Whether the property type is a loft (1 for yes, 0 for no). Defaults to 0.
        property_type_Outros (Optional[Literal[1, 0]]): Whether the property type is categorized as "Other" (1 for yes, 0 for no). Defaults to 0.
        property_type_Serviced_apartment (Optional[Literal[1, 0]]): Whether the property type is a serviced apartment (1 for yes, 0 for no). Defaults to 0.
        room_type_Hotel_room (Optional[Literal[1, 0]]): Whether the room type is a hotel room (1 for yes, 0 for no). Defaults to 0.
        room_type_Private_room (Optional[Literal[1, 0]]): Whether the room type is a private room (1 for yes, 0 for no). Defaults to 0.
        room_type_Shared_room (Optional[Literal[1, 0]]): Whether the room type is a shared room (1 for yes, 0 for no). Defaults to 0.
        cancellation_policy_flexible (Optional[Literal[1, 0]]): Whether the cancellation policy is flexible (1 for yes, 0 for no). Defaults to 0.
        cancellation_policy_moderate (Optional[Literal[1, 0]]): Whether the cancellation policy is moderate (1 for yes, 0 for no). Defaults to 0.
        cancellation_policy_strict (Optional[Literal[1, 0]]): Whether the cancellation policy is strict (1 for yes, 0 for no). Defaults to 0.
        cancellation_policy_strict_14_with_grace_period (Optional[Literal[1, 0]]): Whether the cancellation policy is strict with a 14-day grace period (1 for yes, 0 for no). Defaults to 0.
    """

    host_listings_count: PositiveInt
    latitude: FiniteFloat
    longitude: FiniteFloat
    accommodates: PositiveInt
    bathrooms: PositiveInt
    bedrooms: PositiveInt
    beds: PositiveInt
    extra_people: NonNegativeInt
    minimum_nights: PositiveInt
    n_amenities: PositiveInt
    room_type_Entire_home_apt: Literal[1, 0]
    host_is_superhost: Optional[Literal[0, 1]] = 0
    instant_bookable: Optional[Literal[0, 1]] = 1
    ano: Optional[PositiveInt] = dt.datetime.now().year
    mes: Optional[PositiveInt] = dt.datetime.now().month
    property_type_Apartment: Optional[Literal[1, 0]] = 0
    property_type_Bed_and_breakfast: Optional[Literal[1, 0]] = 0
    property_type_Condominium: Optional[Literal[1, 0]] = 0
    property_type_Guest_suite: Optional[Literal[1, 0]] = 0
    property_type_Guesthouse: Optional[Literal[1, 0]] = 0
    property_type_Hostel: Optional[Literal[1, 0]] = 0
    property_type_House: Optional[Literal[1, 0]] = 0
    property_type_Loft: Optional[Literal[1, 0]] = 0
    property_type_Outros: Optional[Literal[1, 0]] = 0
    property_type_Serviced_apartment: Optional[Literal[1, 0]] = 0
    room_type_Hotel_room: Optional[Literal[1, 0]] = 0
    room_type_Private_room: Optional[Literal[1, 0]] = 0
    room_type_Shared_room: Optional[Literal[1, 0]] = 0
    cancellation_policy_flexible: Optional[Literal[1, 0]] = 0
    cancellation_policy_moderate: Optional[Literal[1, 0]] = 0
    cancellation_policy_strict: Optional[Literal[1, 0]] = 0
    cancellation_policy_strict_14_with_grace_period: Optional[Literal[1, 0]] = 0


class EspecificacoesCasaResponse(BaseModel):
    """
    Response model for returning the predicted price and the input data.

    Attributes:
        preco_estimado (PositiveFloat): The estimated price of the property.
    """

    preco_estimado: PositiveFloat
