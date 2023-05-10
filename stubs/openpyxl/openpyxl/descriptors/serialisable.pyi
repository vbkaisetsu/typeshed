from _typeshed import Incomplete

from openpyxl.descriptors import MetaSerialisable

KEYWORDS: Incomplete
seq_types: Incomplete

class Serialisable(metaclass=MetaSerialisable):
    __attrs__: Incomplete
    __nested__: Incomplete
    __elements__: Incomplete
    __namespaced__: Incomplete
    idx_base: int
    @property
    # TODO: needs overrides in many sub-classes
    # @abstractmethod
    def tagname(self) -> str: ...
    namespace: Incomplete
    @classmethod
    def from_tree(cls, node): ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...
    def __iter__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self) -> int: ...
    def __add__(self, other): ...
    def __copy__(self): ...
