import wiotp.sdk.application

config = wiotp.sdk.application.parseConfigFile("app_config.yml")
app_client = wiotp.sdk.application.ApplicationClient(config)

cloudant_creds = {
  "apikey": "your_api_key_here",
  "host": "eeca8e52-1774-4698-93d1-cafa434762ac-bluemix.cloudantnosqldb.appdomain.cloud",
  "password": "your_pwd_here",
  "port": 443,
  "username": "your_username_here"
}

service_binding = {
    "name": "any-binding-name",
    "description": "Test Cloudant Binding",
    "type": "cloudant",
    "credentials": cloudant_creds
}

# Bind application to the cloudant DB
cloudant_service = app_client.serviceBindings.create(service_binding)

# Create the connector
connector = app_client.dsc.create(
    name="connector_1", type="cloudant", serviceId=cloudant_service.id, timezone="UTC",
    description="Data connector", enabled=True
)

# Create a destination under the connector
destination_1 = connector.destinations.create(name="sensor-data", bucketInterval="DAY")

# Create a rule under the connector, that routes all Android status events to the destination
rule_1 = connector.rules.createEventRule(
    name="status_events", destinationName=destination_1.name, typeId="Android", eventId="status",
    description="Send android status events", enabled=True
)

# Create another destination under the connector
destination_2 = connector.destinations.create(name="gateway-data", bucketInterval="DAY")

# Create a rule under the connector, that routes all raspi status events to the destination
rule_2 = connector.rules.createEventRule(
    name="status_events", destinationName=destination_2.name, typeId="raspi", eventId="status",
    description="Gateway status events", enabled=True
)