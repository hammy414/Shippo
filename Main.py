#By Josh Sternfeld
#Potential TSE - Shippo
#10/22/2022

from pickle import FALSE
import shippo_secrets
import shippo
test_key = shippo_secrets.test_api_key
# print(test_key)
shippo.config.api_key = test_key

#####################################
#Edit this below informtion for your shipment
address_from = {
    "name": "Shawn Ippotle",
    "street1": "215 Clayton St.",
    "city": "San Francisco",
    "state": "CA",
    "zip": "94117",
    "country": "US"
}

address_to = {
    "name": "Mr Hippo",
    "street1": "Broadway 1",
    "city": "New York",
    "state": "NY",
    "zip": "10007",
    "country": "US"
}

parcel = {
    "length": "5",
    "width": "5",
    "height": "5",
    "distance_unit": "in",
    "weight": "2",
    "mass_unit": "lb"
}

#Tool class that contains the different shippo api calls
class tool():

    def create_shipment(address_from, address_to, parcel):
        shipment = shippo.Shipment.create(
        address_from = address_from,
        address_to = address_to,
        parcels = [parcel],)
        return shipment
    
    def retrieve_shipment(shipment_object_id):
        retrieve = shippo.Shipment.retrieve(shipment_object_id)
        return retrieve

    def retrieve_rates(rates_object_id):
        rates = shippo.Shipment.get_rates(rates_object_id)
        return rates

    def retrieve_address(object_id, is_shipment=False):
        if is_shipment:
            retrieve = shippo.Shipment.retrieve(object_id)
            addressfrom = retrieve["address_from"]
            addressto = retrieve["address_to"]
            return addressfrom, addressto
        else:
            address = shippo.Address.retrieve(object_id)
            return address
    
    def retrieve_parcel(object_id, is_shipment=False):
        if is_shipment:
            retrieve = shippo.Shipment.retrieve(object_id)
            parcel = retrieve["parcels"]
            return parcel
        else:
            address = shippo.Parcel.retrieve(object_id)
            return address
            
#The api print statements for the above functions
print(tool.create_shipment(address_from, address_to, parcel))
print(tool.retrieve_shipment("d10a872b9a6d4aa3875348c077bebd44"))
print(tool.retrieve_rates("d10a872b9a6d4aa3875348c077bebd44"))
print(tool.retrieve_address("d10a872b9a6d4aa3875348c077bebd44", True))
print(tool.retrieve_address("1d8ffe53e86d4483a69a6a9d2f9a2f69"))
print(tool.retrieve_parcel("b801ce4917534021820d7f101700d002"))
print(tool.retrieve_parcel("d10a872b9a6d4aa3875348c077bebd44", True))