from dspygen.rdddy.actor_system import ActorSystem
from ngbpm.rddd.aggregates.activity_execution_aggregate import ActivityExecutionAggregate
from ngbpm.rddd.aggregates.partner_interaction_aggregate import PartnerInteractionAggregate
from ngbpm.rddd.aggregates.process_execution_aggregate import ProcessExecutionAggregate
from ngbpm.rddd.aggregates.process_instance_aggregate import ProcessInstanceAggregate
from ngbpm.rddd.messages import *


async def main():
    actor_system = ActorSystem()

    # Assuming you have actor_of method properly implemented to create or retrieve actors
    activity_execution_aggregate = await actor_system.actor_of(ActivityExecutionAggregate)
    partner_interaction_aggregate = await actor_system.actor_of(PartnerInteractionAggregate)
    process_execution_aggregate = await actor_system.actor_of(ProcessExecutionAggregate)
    process_instance_aggregate = await actor_system.actor_of(ProcessInstanceAggregate)

    # Publish commands relevant to each aggregate
    # Note: The actual handling logic inside each aggregate and the publishing mechanism within the actor system need to be implemented accordingly
    # await actor_system.publish(ActivityStartCommand(task_id="task_1", parameters={"key": "value"}))
    # await actor_system.publish(InvokePartnerServiceCommand(service_name="PartnerService", parameters={"param": "value"}))
    # await actor_system.publish(ProcessStartCommand(process_id="process_1"))
    await actor_system.publish(SaveProcessInstanceCommand(process_id="process_1", instance_data={"data": "value"}))

    # Allow some time for the actor system to process the commands
    await asyncio.sleep(1)  # Adjust the sleep time based on your system's responsiveness

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
