from typing import Any, Optional, Sequence, Tuple

from django.db.models import Model
from django.http import HttpRequest, HttpResponse
from django.test import testcases
from django.test.client import Client as DjangoClient, ClientHandler, RequestFactory as DjangoRequestFactory
from rest_framework.compat import requests

def force_authenticate(request: HttpRequest, user: Optional[Model] = ..., token: Optional[Any] = ...) -> None: ...

class RequestsClient(requests.Session): ...

class APIRequestFactory(DjangoRequestFactory):
    renderer_classes_list: Sequence[str] = ...
    default_format: str = ...
    def __init__(self, enforce_csrf_checks: bool = ..., **defaults: Any) -> None: ...
    def _encode_data(
        self, data: Optional[Any], format: Optional[str] = ..., content_type: Optional[str] = ...
    ) -> Tuple[bytes, str]: ...

class ForceAuthClientHandler(ClientHandler):
    def __init__(self, *args: Any, **kwargs: Any): ...
    def get_response(self, request: HttpRequest) -> HttpResponse: ...

class APIClient(APIRequestFactory, DjangoClient):  # type: ignore
    def credentials(self, **kwargs: Any): ...
    def force_authenticate(self, user: Optional[Model] = ..., token: Optional[Any] = ...) -> None: ...

class APITransactionTestCase(testcases.TransactionTestCase): ...
class APITestCase(testcases.TestCase): ...
class APISimpleTestCase(testcases.SimpleTestCase): ...
class APILiveServerTestCase(testcases.LiveServerTestCase): ...
class URLPatternsTestCase(testcases.SimpleTestCase): ...