from dspygen.rdddy.abstract_command import AbstractCommand
from dspygen.rdddy.abstract_event import AbstractEvent


# ActivityExecutionAggregate Commands and Events
class ActivityStartCommand(AbstractCommand):
    task_id: str
    parameters: dict


class ActivityStartedEvent(AbstractEvent):
    task_id: str
    status: str = "started"


class ActivityCompleteCommand(AbstractCommand):
    task_id: str
    outcome: dict


class ActivityCompletedEvent(AbstractEvent):
    task_id: str
    status: str = "completed"


# PartnerInteractionAggregate Commands and Events


class InvokePartnerServiceCommand(AbstractCommand):
    service_name: str
    parameters: dict


class PartnerServiceInvokedEvent(AbstractEvent):
    service_name: str
    status: str = "invoked"


class ReceivePartnerDataCommand(AbstractCommand):
    service_name: str
    data: dict


class PartnerDataReceivedEvent(AbstractEvent):
    service_name: str
    status: str = "data_received"


# ProcessExecutionAggregate Commands and Events


class ProcessStartCommand(AbstractCommand):
    process_id: str


class ProcessStartedEvent(AbstractEvent):
    process_id: str
    status: str = "started"


class ProcessStopCommand(AbstractCommand):
    process_id: str


class ProcessStoppedEvent(AbstractEvent):
    process_id: str
    status: str = "stopped"


# ProcessInstanceAggregate Commands


class SaveProcessInstanceCommand(AbstractCommand):
    process_id: str
    instance_data: dict


class LoadProcessInstanceCommand(AbstractCommand):
    process_id: str
