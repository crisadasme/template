from nameko.testing.services import worker_factory

from src.hello_service import GreetingService


def test_conversion_service():
    # create worker with mock dependencies
    service = worker_factory(GreetingService)

    assert service.hello(name="Cris") == "Hello World, Cris!"
