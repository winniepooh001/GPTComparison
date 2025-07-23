"""
Configuration management for the GPT trading comparison system.

This module handles loading, validation, and management of system
configuration including API keys, strategy parameters, and system settings.
"""

import json
import os
from typing import Dict, Any, Optional, List
from pathlib import Path
import logging
from dataclasses import dataclass, asdict

logger = logging.getLogger(__name__)


@dataclass
class LLMConfig:
    """Configuration for LLM strategies."""
    api_key: str
    model: str
    enable_thinking: bool = True
    enable_research: bool = True
    max_recommendations: int = 8
    temperature: float = 0.1


@dataclass  
class AlpacaConfig:
    """Configuration for Alpaca trading."""
    api_key: str
    secret_key: str
    paper_trading: bool = True
    data_feed: str = 'iex'


@dataclass
class StrategyConfig:
    """Configuration for traditional strategies."""
    enabled: bool = True
    parameters: Dict[str, Any] = None


class ConfigManager:
    """
    Configuration manager for the trading system.
    
    Handles loading, validation, and access to all system configuration
    including API credentials, strategy parameters, and system settings.
    """
    
    def __init__(self, config_path: str = "config/config.json"):
        """
        Initialize configuration manager.
        
        Args:
            config_path: Path to configuration file
        """
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.load_config()
    
    def load_config(self) -> None:
        """Load configuration from file."""
        pass
    
    def save_config(self) -> None:
        """Save current configuration to file."""
        pass
    
    def get_llm_config(self, provider: str) -> LLMConfig:
        """
        Get LLM configuration for a provider.
        
        Args:
            provider: LLM provider name ('chatgpt', 'claude', etc.)
            
        Returns:
            LLMConfig object
        """
        pass
    
    def get_alpaca_config(self, strategy_name: str) -> AlpacaConfig:
        """
        Get Alpaca configuration for a strategy.
        
        Args:
            strategy_name: Strategy name
            
        Returns:
            AlpacaConfig object
        """
        pass
    
    def get_strategy_config(self, strategy_name: str) -> StrategyConfig:
        """
        Get configuration for a traditional strategy.
        
        Args:
            strategy_name: Strategy name
            
        Returns:
            StrategyConfig object
        """
        pass
    
    def get_system_config(self) -> Dict[str, Any]:
        """
        Get system-level configuration.
        
        Returns:
            System configuration dictionary
        """
        pass
    
    def validate_config(self) -> Dict[str, List[str]]:
        """
        Validate configuration completeness and correctness.
        
        Returns:
            Dictionary with validation errors by section
        """
        pass
    
    def create_default_config(self) -> Dict[str, Any]:
        """
        Create default configuration template.
        
        Returns:
            Default configuration dictionary
        """
        pass
    
    def update_config(self, section: str, updates: Dict[str, Any]) -> None:
        """
        Update configuration section.
        
        Args:
            section: Configuration section to update
            updates: Updates to apply
        """
        pass
    
    def get_all_alpaca_credentials(self) -> Dict[str, Dict[str, str]]:
        """
        Get all Alpaca credentials for multi-portfolio setup.
        
        Returns:
            Dictionary mapping strategy names to credentials
        """
        pass