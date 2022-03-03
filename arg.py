from transformers import TrainingArguments
from dataclasses import field, dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class CustomTrainingArguments(TrainingArguments):
  alpha: float = field(default=0.25)
  gamma: float = field(default=2)