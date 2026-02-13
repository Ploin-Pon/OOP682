from abc import ABC, abstractmethod
from typing import List

# Interface (Contract)
class ILogSource(ABC):
    
    @abstractmethod
    def get_logs(self) -> List[str]:
        pass