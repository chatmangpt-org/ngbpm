from dspygen.rdddy.abstract_aggregate import AbstractAggregate
from ngbpm.rddd.messages import *


class ActivityExecutionAggregate(AbstractAggregate):
    async def handle_activity_start(self, command: ActivityStartCommand):
        print("Starting activity...")
        # Implement activity start logic here
        await self.publish(ActivityStartedEvent(task_id=command.task_id, content="Activity started"))

    async def handle_activity_complete(self, command: ActivityCompleteCommand):
        print("Completing activity...")
        # Implement activity completion logic here
        await self.publish(ActivityCompletedEvent(task_id=command.task_id, content="Activity completed"))
