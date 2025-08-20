"""
LLM Extractor - A systematic approach to structured data extraction from unstructured text.

This package provides tools to define questions, validate responses, and extract
structured data using Large Language Models.
"""

from .models import Question, ExtractionResult, LLMConfig, AnswerType, DBConfig
from .extract import extract_data
from .prompt_builder import build_prompt
from .llm_client import get_llm_response, parse_llm_json_response, LLMClientError
from .validator import validate_answer
from .processor import format_for_db, format_for_target_tables, create_summary_stats, process_query

__version__ = "0.0.1"
__author__ = "Cooper Richason"

# Define public API
__all__ = [
    # Core data models
    "Question",
    "ExtractionResult", 
    "LLMConfig",
    "AnswerType",
    "DBConfig",
    
    # Main extraction functions
    "extract_data",
    
    # Individual components (for advanced usage)
    "build_prompt",
    "get_llm_response",
    "parse_llm_json_response",
    "validate_answer",
    "format_for_db",
    "format_for_target_tables",
    "create_summary_stats",
    "process_query",
    
    # Exceptions
    "LLMClientError"
]

# Convenience imports for common use cases
def create_question(id: str, text: str, answer_type: str, **kwargs) -> Question:
    """
    Convenience function to create a Question object.
    
    Args:
        id: Unique identifier for the question
        text: The question text
        answer_type: Type of answer expected ('boolean', 'enum', 'integer', etc.)
        target_table: Database table to store the answer
        target_field: Database field to store the answer
        **kwargs: Additional constraints and options
        
    Returns:
        Question object
    """
    return Question(
        id=id,
        text=text,
        answer_type=AnswerType(answer_type),
        answer_config=kwargs
    )