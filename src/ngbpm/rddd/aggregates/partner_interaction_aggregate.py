from dspygen.rdddy.abstract_aggregate import AbstractAggregate
from ngbpm.rddd.messages import *


class PartnerInteractionAggregate(AbstractAggregate):
    async def handle_invoke_partner_service(self, command: InvokePartnerServiceCommand):
        print("Invoking partner service...")
        # Implement partner service invocation logic here
        await self.publish(PartnerServiceInvokedEvent(service_name=command.service_name, content="Partner service invoked"))

    async def handle_receive_partner_data(self, command: ReceivePartnerDataCommand):
        print("Receiving data from partner...")
        # Implement logic for handling data received from a partner here
        await self.publish(PartnerDataReceivedEvent(service_name=command.service_name, content="Data received from partner"))
