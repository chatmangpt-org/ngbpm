from dspygen.rdddy.abstract_aggregate import AbstractAggregate
from ngbpm.rddd.messages import *


class ProcessInstanceAggregate(AbstractAggregate):
    async def handle_save_process_instance(self, command: SaveProcessInstanceCommand):
        print("Saving process instance...")
        # Implement process instance saving logic here
        # No event is necessarily published here, but one could be if the system needs to react to this action

    async def handle_load_process_instance(self, command: LoadProcessInstanceCommand):
        print("Loading process instance...")
        # Implement process instance loading logic here
        # Similar to save, loading might not publish an event unless system needs to react to the loading action
