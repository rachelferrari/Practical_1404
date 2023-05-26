from silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
print(silver_taxi)
another_silver_taxi = SilverServiceTaxi("Silver Taxi", 200, 2)
another_silver_taxi.drive(18)  # 18km trip in a Silver Service Taxi
print(f"${another_silver_taxi.get_fare():.2f}")
