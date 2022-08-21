from dataclasses import dataclass


@dataclass
class OperationResult:
    is_failed: bool
    message: str
    stack_trace: str
