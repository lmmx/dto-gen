# generated by datamodel-codegen:
#   filename:  schema.yaml
#   timestamp: 2023-06-03T11:35:47+00:00

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional, Union

Reference = dict[str, str]


@dataclass
class Contact(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None


@dataclass
class License(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    name: str
    url: Optional[str] = None


@dataclass
class ServerVariable(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    default: str
    enum: Optional[list[str]] = None
    description: Optional[str] = None


class Type(Enum):
    array = 'array'
    boolean = 'boolean'
    integer = 'integer'
    number = 'number'
    object = 'object'
    string = 'string'


@dataclass
class Discriminator(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    propertyName: str
    mapping: Optional[dict[str, str]] = None


@dataclass
class XML(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    name: Optional[str] = None
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = False
    wrapped: Optional[bool] = False


@dataclass
class Example(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    summary: Optional[str] = None
    description: Optional[str] = None
    value: Optional[Any] = None
    externalValue: Optional[str] = None


class Style(Enum):
    simple = 'simple'


SecurityRequirement = Optional[dict[str, list[str]]]


@dataclass
class ExternalDocumentation(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    url: str
    description: Optional[str] = None


ExampleXORExamples = Any


@dataclass
class SchemaXORContentItem(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    pass


SchemaXORContent = Union[Any, SchemaXORContentItem]


class In(Enum):
    path = 'path'


class Style1(Enum):
    matrix = 'matrix'
    label = 'label'
    simple = 'simple'


class Required(Enum):
    bool_True = True


@dataclass
class ParameterLocationItem(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    required: Required
    in_: Optional[In] = None
    style: Optional[Style1] = 'simple'


class In1(Enum):
    query = 'query'


class Style2(Enum):
    form = 'form'
    spaceDelimited = 'spaceDelimited'
    pipeDelimited = 'pipeDelimited'
    deepObject = 'deepObject'


@dataclass
class ParameterLocationItem1(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    in_: Optional[In1] = None
    style: Optional[Style2] = 'form'


class In2(Enum):
    header = 'header'


class Style3(Enum):
    simple = 'simple'


@dataclass
class ParameterLocationItem2(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    in_: Optional[In2] = None
    style: Optional[Style3] = 'simple'


class In3(Enum):
    cookie = 'cookie'


class Style4(Enum):
    form = 'form'


@dataclass
class ParameterLocationItem3(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    in_: Optional[In3] = None
    style: Optional[Style4] = 'form'


ParameterLocation = Union[
    ParameterLocationItem,
    ParameterLocationItem1,
    ParameterLocationItem2,
    ParameterLocationItem3,
]


class Type1(Enum):
    apiKey = 'apiKey'


class In4(Enum):
    header = 'header'
    query = 'query'
    cookie = 'cookie'


@dataclass
class APIKeySecurityScheme(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    type: Type1
    name: str
    in_: In4
    description: Optional[str] = None


@dataclass
class HTTPSecuritySchemeItem(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    scheme: Optional[str] = None


@dataclass
class HTTPSecuritySchemeItem1(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    scheme: Optional[Any] = None


class Type2(Enum):
    http = 'http'


@dataclass
class HTTPSecurityScheme1(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True
(HTTPSecuritySchemeItem)
    scheme: str
    type: Type2
    bearerFormat: Optional[str] = None
    description: Optional[str] = None


@dataclass
class HTTPSecurityScheme2(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True
(HTTPSecuritySchemeItem1)
    scheme: str
    type: Type2
    bearerFormat: Optional[str] = None
    description: Optional[str] = None


HTTPSecurityScheme = Union[HTTPSecurityScheme1, HTTPSecurityScheme2]


class Type4(Enum):
    oauth2 = 'oauth2'


class Type5(Enum):
    openIdConnect = 'openIdConnect'


@dataclass
class OpenIdConnectSecurityScheme(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    type: Type5
    openIdConnectUrl: str
    description: Optional[str] = None


@dataclass
class ImplicitOAuthFlow(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    authorizationUrl: str
    scopes: dict[str, str]
    refreshUrl: Optional[str] = None


@dataclass
class PasswordOAuthFlow(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    tokenUrl: str
    scopes: dict[str, str]
    refreshUrl: Optional[str] = None


@dataclass
class ClientCredentialsFlow(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    tokenUrl: str
    scopes: dict[str, str]
    refreshUrl: Optional[str] = None


@dataclass
class AuthorizationCodeOAuthFlow(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    authorizationUrl: str
    tokenUrl: str
    scopes: dict[str, str]
    refreshUrl: Optional[str] = None


Callback = dict[str, Any]


class Style5(Enum):
    form = 'form'
    spaceDelimited = 'spaceDelimited'
    pipeDelimited = 'pipeDelimited'
    deepObject = 'deepObject'


@dataclass
class Info(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    title: str
    version: str
    description: Optional[str] = None
    termsOfService: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None


@dataclass
class Server(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    url: str
    description: Optional[str] = None
    variables: Optional[dict[str, ServerVariable]] = None


@dataclass
class Schema(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    title: Optional[str] = None
    multipleOf: Optional[float] = None
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[bool] = False
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[bool] = False
    maxLength: Optional[int] = None
    minLength: Optional[int] = 0
    pattern: Optional[str] = None
    maxItems: Optional[int] = None
    minItems: Optional[int] = 0
    uniqueItems: Optional[bool] = False
    maxProperties: Optional[int] = None
    minProperties: Optional[int] = 0
    required: Optional[list[str]] = None
    enum: Optional[list] = None
    type: Optional[Type] = None
    not_: Optional[Union[Schema, Reference]] = None
    allOf: Optional[list[Union[Schema, Reference]]] = None
    oneOf: Optional[list[Union[Schema, Reference]]] = None
    anyOf: Optional[list[Union[Schema, Reference]]] = None
    items: Optional[Union[Schema, Reference]] = None
    properties: Optional[dict[str, Union[Schema, Reference]]] = None
    additionalProperties: Optional[Union[Schema, Reference, bool]] = True
    description: Optional[str] = None
    format: Optional[str] = None
    default: Optional[Any] = None
    nullable: Optional[bool] = False
    discriminator: Optional[Discriminator] = None
    readOnly: Optional[bool] = False
    writeOnly: Optional[bool] = False
    example: Optional[Any] = None
    externalDocs: Optional[ExternalDocumentation] = None
    deprecated: Optional[bool] = False
    xml: Optional[XML] = None


@dataclass
class Tag(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    name: str
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None


@dataclass
class OAuthFlows(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    implicit: Optional[ImplicitOAuthFlow] = None
    password: Optional[PasswordOAuthFlow] = None
    clientCredentials: Optional[ClientCredentialsFlow] = None
    authorizationCode: Optional[AuthorizationCodeOAuthFlow] = None


@dataclass
class Link(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    operationId: Optional[str] = None
    operationRef: Optional[str] = None
    parameters: Optional[dict[str, Any]] = None
    requestBody: Optional[Any] = None
    description: Optional[str] = None
    server: Optional[Server] = None


@dataclass
class OAuth2SecurityScheme(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    type: Type4
    flows: OAuthFlows
    description: Optional[str] = None


SecurityScheme = Union[
    APIKeySecurityScheme,
    HTTPSecurityScheme,
    OAuth2SecurityScheme,
    OpenIdConnectSecurityScheme,
]


@dataclass
class Model(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    openapi: str
    info: Info
    paths: Paths
    externalDocs: Optional[ExternalDocumentation] = None
    servers: Optional[list[Server]] = None
    security: Optional[list[SecurityRequirement]] = None
    tags: Optional[list[Tag]] = None
    components: Optional[Components] = None


@dataclass
class Components(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    schemas: Optional[dict[str, Union[Schema, Reference]]] = None
    responses: Optional[dict[str, Union[Reference, Response]]] = None
    parameters: Optional[dict[str, Union[Reference, Parameter]]] = None
    examples: Optional[dict[str, Union[Reference, Example]]] = None
    requestBodies: Optional[dict[str, Union[Reference, RequestBody]]] = None
    headers: Optional[dict[str, Union[Reference, Header]]] = None
    securitySchemes: Optional[dict[str, Union[Reference, SecurityScheme]]] = None
    links: Optional[dict[str, Union[Reference, Link]]] = None
    callbacks: Optional[dict[str, Union[Reference, Callback]]] = None


@dataclass
class Response(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    description: str
    headers: Optional[dict[str, Union[Header, Reference]]] = None
    content: Optional[dict[str, MediaType]] = None
    links: Optional[dict[str, Union[Link, Reference]]] = None


@dataclass
class MediaType(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    schema_: Optional[Union[Schema, Reference]] = None
    example: Optional[Any] = None
    examples: Optional[dict[str, Union[Example, Reference]]] = None
    encoding: Optional[dict[str, Encoding]] = None


@dataclass
class Header(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    description: Optional[str] = None
    required: Optional[bool] = False
    deprecated: Optional[bool] = False
    allowEmptyValue: Optional[bool] = False
    style: Optional[Style] = 'simple'
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = False
    schema_: Optional[Union[Schema, Reference]] = None
    content: Optional[dict[str, MediaType]] = None
    example: Optional[Any] = None
    examples: Optional[dict[str, Union[Example, Reference]]] = None


Paths = Union[dict[str, PathItem], dict[str, Any]]


@dataclass
class PathItem(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    field_ref: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
    trace: Optional[Operation] = None
    servers: Optional[list[Server]] = None
    parameters: Optional[list[Union[Parameter, Reference]]] = None


@dataclass
class Operation(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    responses: Responses
    tags: Optional[list[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None
    operationId: Optional[str] = None
    parameters: Optional[list[Union[Parameter, Reference]]] = None
    requestBody: Optional[Union[RequestBody, Reference]] = None
    callbacks: Optional[dict[str, Union[Callback, Reference]]] = None
    deprecated: Optional[bool] = False
    security: Optional[list[SecurityRequirement]] = None
    servers: Optional[list[Server]] = None


@dataclass
class Responses(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    default: Optional[Union[Response, Reference]] = None


@dataclass
class Parameter(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    name: str
    in_: str
    description: Optional[str] = None
    required: Optional[bool] = False
    deprecated: Optional[bool] = False
    allowEmptyValue: Optional[bool] = False
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = False
    schema_: Optional[Union[Schema, Reference]] = None
    content: Optional[dict[str, MediaType]] = None
    example: Optional[Any] = None
    examples: Optional[dict[str, Union[Example, Reference]]] = None


@dataclass
class RequestBody(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    content: dict[str, MediaType]
    description: Optional[str] = None
    required: Optional[bool] = False


@dataclass
class Encoding(JSONWizard):
    class Meta(JSONWizard.Meta):
        recursive_classes = True

    contentType: Optional[str] = None
    headers: Optional[dict[str, Union[Header, Reference]]] = None
    style: Optional[Style5] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = False
