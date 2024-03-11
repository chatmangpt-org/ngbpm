# ngbpm/api.py
import asyncio
import inspect
import logging
from typing import Type
import importlib

import coloredlogs
from fastapi import FastAPI, Depends
from pydantic import BaseModel

from dspygen.rdddy.abstract_message import MessageFactory
from dspygen.rdddy.actor_system import ActorSystem
from ngbpm.rddd.aggregates.activity_execution_aggregate import ActivityExecutionAggregate
from ngbpm.rddd.aggregates.partner_interaction_aggregate import PartnerInteractionAggregate
from ngbpm.rddd.aggregates.process_execution_aggregate import ProcessExecutionAggregate
from ngbpm.rddd.aggregates.process_instance_aggregate import ProcessInstanceAggregate
# Assuming ActorSystem is defined in actor_system.py and needs to be a singleton

actor_system: ActorSystem | None = None


async def get_actor_system() -> ActorSystem:
    global actor_system
    if actor_system is None:
        # Initialize your ActorSystem with any required configuration
        asyncio.set_event_loop(asyncio.new_event_loop())

        actor_system = ActorSystem(loop=asyncio.get_event_loop())

        # Assuming you have actor_of method properly implemented to create or retrieve actors
        activity_execution_aggregate = await actor_system.actor_of(ActivityExecutionAggregate)
        partner_interaction_aggregate = await actor_system.actor_of(PartnerInteractionAggregate)
        process_execution_aggregate = await actor_system.actor_of(ProcessExecutionAggregate)
        process_instance_aggregate = await actor_system.actor_of(ProcessInstanceAggregate)

    return actor_system


app = FastAPI()


@app.on_event("startup")
def startup_event() -> None:
    """Run API startup events."""
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                '()': 'coloredlogs.ColoredFormatter',
                'format': '%(levelname)s %(message)s',
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    })

    # Dynamically create routes for each message class
    create_routes_for_message_classes()


def create_routes_for_message_classes():
    """Create FastAPI routes for each message class in the messages module."""
    messages_module = importlib.import_module('ngbpm.rddd.messages')
    for name, obj in inspect.getmembers(messages_module, inspect.isclass):
        if issubclass(obj, BaseModel) and obj is not BaseModel:
            create_route_for_message_class(obj)


def create_route_for_message_class(message_class: Type[BaseModel]):
    """Create a FastAPI route for a specific message class."""
    @app.post(f"/{message_class.__name__.lower()}/", response_model=message_class)
    async def generic_route(message: message_class, actor_system: ActorSystem = Depends(get_actor_system)) -> message_class:
        print(f"Received {message_class.__name__}: {message}")

        message_inst = MessageFactory.create_message(message.model_dump())
        await actor_system.publish(message_inst)

        await asyncio.sleep(1)

        return message

@app.get("/")
def read_root() -> str:
    """Read root."""
    return "Welcome to ngbpm API"
