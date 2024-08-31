from kafka import KafkaProducer
import json

producer = KafkaProducer(value_serializer=lambda v:json.dumps(v).encode('utf-8'))
transid = 102

while True:
    user_input = input("Do you want add a transaction? (press 'n' to stop): ")
    if user_input == 'n':
        print("Stropping transaction")
        break
    else:
        atm_choice = int(input("Which ATM do you want to transact in? 1 or 2 "))
        if (atm_choice == 1 or atm_choice == 2):
            producer.send('bankbranch', {'atmid': atm_choice, 'transid': transid})
            producer.flush()
            transid += 1
        else:
            print("Invalid number!")
            continue

producer.close()