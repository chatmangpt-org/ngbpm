from dspygen.rdddy.abstract_aggregate import AbstractAggregate
from ngbpm.rddd.messages import *


class ProcessExecutionAggregate(AbstractAggregate):
    async def handle_process_start(self, command: ProcessStartCommand):
        print(f"Starting process {command.process_id}...")
        # Logic for starting a process
        await self.publish(ProcessStartedEvent(process_id=command.process_id))

    async def handle_process_stop(self, command: ProcessStopCommand):
        print(f"Stopping process {command.process_id}...")
        # Logic for stopping a process
        await self.publish(ProcessStoppedEvent(process_id=command.process_id))
