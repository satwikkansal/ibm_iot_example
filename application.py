import wiotp.sdk.application


CLOUDANT_CREDS = {
  "apikey": "your_api_key_here",
  "host": "eeca8e52-1774-4698-93d1-cafa434762ac-bluemix.cloudantnosqldb.appdomain.cloud",
  "password": "your_pwd_here",
  "port": 443,
  "username": "your_username_here"
}

SERVICE_BINDING = {
    "name": "any-binding-name",
    "description": "Test Cloudant Binding",
    "type": "cloudant",
    "credentials": CLOUDANT_CREDS
}

ANDROID_DEVICE_TYPE = "Android"
GATEWAY_DEVICE_TYPE = "raspi"
STATUS_EVENT_TYPE = "status"


def get_application_client(config_file_path):
    config = wiotp.sdk.application.parseConfigFile(config_file_path)
    app_client = wiotp.sdk.application.ApplicationClient(config)
    return app_client


def create_cloudant_connections(client, service_binding):
    # Bind application to the Cloudant DB
    cloudant_service = client.serviceBindings.create(service_binding)

    # Create the connector
    connector = client.dsc.create(
        name="connector_1", type="cloudant", serviceId=cloudant_service.id, timezone="UTC",
        description="Data connector", enabled=True
    )

    # Create a destination under the connector
    destination_1 = connector.destinations.create(name="sensor-data", bucketInterval="DAY")

    # Create a rule under the connector, that routes all Android status events to the destination
    connector.rules.createEventRule(
        name="status_events", destinationName=destination_1.name, typeId=ANDROID_DEVICE_TYPE, eventId=STATUS_EVENT_TYPE,
        description="Send android status events", enabled=True
    )

    # Create another destination under the connector
    destination_2 = connector.destinations.create(name="gateway-data", bucketInterval="DAY")

    # Create a rule under the connector, that routes all raspi status events to the destination
    connector.rules.createEventRule(
        name="status_events", destinationName=destination_2.name, typeId=GATEWAY_DEVICE_TYPE, eventId=STATUS_EVENT_TYPE,
        description="Gateway status events", enabled=True)


def send_reset_command(client, type, id):
    data = {'reset': True}
    client.publishCommand(type, id, "reset", "json", data)


app_client = get_gateway_cilent("app_config.yml")
app_client.connect()

# Call the functions like this
# send_reset_command(app_client, 'raspi', 'raspi-1')

