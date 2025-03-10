from dataclasses import dataclass, field
from enum import Enum
from typing import ForwardRef, Optional


@dataclass
class Dependency:
    """
    :ivar value:
    :ivar requirement_id: @requirementId: Short ID of the requirement,
        as defined in the specification, e.g. CSIP1, CSIPSTR5.
    :ivar url: @URL: Direct URL to the requirement text in the
        specification.
    """

    class Meta:
        name = "dependency"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    requirement_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requirementId",
            "type": "Attribute",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Description:
    class Meta:
        name = "description"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class ErrorLevel(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class Id:
    class Meta:
        name = "id"

    requirement_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requirementId",
            "type": "Attribute",
            "required": True,
        },
    )
    specification: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Message:
    class Meta:
        name = "message"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class PackageIsImplemented(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"


class PackageIsValid(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"


@dataclass
class Path:
    class Meta:
        name = "path"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Reference:
    """
    :ivar value:
    :ivar requirement_id: @requirementId: Short ID of the requirement,
        as defined in the specification, e.g. CSIP1, CSIPSTR5.
    :ivar url: @URL: Direct URL to the requirement text in the
        specification.
    """

    class Meta:
        name = "reference"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    requirement_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "requirementId",
            "type": "Attribute",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Attribute",
            "required": True,
        },
    )


class RequirementTextCardinality(Enum):
    VALUE_0_1 = "0..1"
    VALUE_0_N = "0..n"
    VALUE_1_1 = "1..1"
    VALUE_1_N = "1..n"


class RequirementTextLevel(Enum):
    MUST = "MUST"
    SHOULD = "SHOULD"
    MAY = "MAY"


class TestCaseTestable(Enum):
    FALSE = "FALSE"
    TRUE = "TRUE"
    UNKNOWN = "UNKNOWN"
    PARTIAL = "PARTIAL"


@dataclass
class Dependencies:
    class Meta:
        name = "dependencies"

    dependency: list[Dependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Error:
    class Meta:
        name = "error"

    message: Optional[Message] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    level: Optional[ErrorLevel] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Package:
    """
    :ivar path:
    :ivar description:
    :ivar is_valid: The isValid attribute should be set TRUE for corpus
        packages that shouldn't generate any validation messages,
        including WARNING or INFO messages. The attribute is
        inappropriately named but changing it would break too many
        existing test cases.
    :ivar is_implemented: The isImplemented attribute should be set
        FALSE for corpus packages that are defined in the test case but
        not implemented as a package. The attribute is optional and
        defaults to TRUE.
    :ivar name:
    """

    class Meta:
        name = "package"

    path: Optional[Path] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    is_valid: Optional[PackageIsValid] = field(
        default=None,
        metadata={
            "name": "isValid",
            "type": "Attribute",
            "required": True,
        },
    )
    is_implemented: PackageIsImplemented = field(
        default=PackageIsImplemented.FALSE,
        metadata={
            "name": "isImplemented",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class References:
    class Meta:
        name = "references"

    reference: list[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class RequirementText:
    class Meta:
        name = "requirementText"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "name",
                    "type": ForwardRef("RequirementText.Name"),
                },
                {
                    "name": "location",
                    "type": ForwardRef("RequirementText.Location"),
                },
                {
                    "name": "description",
                    "type": ForwardRef("RequirementText.Description"),
                },
                {
                    "name": "cardinality",
                    "type": RequirementTextCardinality,
                },
                {
                    "name": "level",
                    "type": RequirementTextLevel,
                },
            ),
        },
    )

    @dataclass
    class Name:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Location:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Description:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class CorpusPackages:
    class Meta:
        name = "corpusPackages"

    package: list[Package] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Rule:
    class Meta:
        name = "rule"

    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    error: Optional[Error] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    corpus_packages: Optional[CorpusPackages] = field(
        default=None,
        metadata={
            "name": "corpusPackages",
            "type": "Element",
            "required": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Rules:
    class Meta:
        name = "rules"

    rule: list[Rule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class TestCase:
    class Meta:
        name = "testCase"

    id: Optional[Id] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    references: Optional[References] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    requirement_text: Optional[RequirementText] = field(
        default=None,
        metadata={
            "name": "requirementText",
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    dependencies: Optional[Dependencies] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    rules: Optional[Rules] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    testable: Optional[TestCaseTestable] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
