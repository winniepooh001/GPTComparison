"""
Base strategy interface for all trading strategies in the comparison tool.

This module defines the abstract base class that all trading strategies must implement,
ensuring consistent interfaces for LLM-based and traditional strategies.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta
from enum import Enum


class PositionAction(Enum):
    """Actions that can be taken on a position."""
    HOLD = "hold"
    SELL = "sell"
    INCREASE = "increase"
    DECREASE = "decrease"


@dataclass
class TradingRecommendation:
    """
    Standardized format for trading recommendations across all strategies.
    
    Attributes:
        ticker: Stock symbol (must be in Russell 3000)
        action: BUY, SELL, or HOLD
        quantity: Number of shares
        confidence: Strategy confidence (0-1)
        stop_loss_condition: Stop loss trigger (percentage or absolute price)
        profit_taking_condition: Profit taking trigger (percentage or absolute price)
        max_holding_period: Maximum time to hold position (in days)
        re_evaluation_date: When to re-evaluate this recommendation
        reasoning: Strategy-specific reasoning for the recommendation
    """
    ticker: str
    action: str  # 'BUY', 'SELL', 'HOLD'
    quantity: int
    confidence: float
    stop_loss_condition: str
    profit_taking_condition: str
    max_holding_period: int
    re_evaluation_date: datetime
    reasoning: Optional[str] = None


@dataclass
class PositionEvaluation:
    """
    Result of evaluating an existing position.
    
    Attributes:
        ticker: Stock symbol
        current_quantity: Current shares held
        recommended_action: What to do with the position
        target_quantity: New target quantity (if changing position)
        trigger_reason: Why this action is recommended
        urgency: How urgent this action is (0-1, 1 being immediate)
    """
    ticker: str
    current_quantity: int
    recommended_action: PositionAction
    target_quantity: int
    trigger_reason: str
    urgency: float


@dataclass
class RiskParameters:
    """
    Risk management parameters for a strategy.
    
    Attributes:
        max_position_size: Maximum position size as % of portfolio
        stop_loss_min: Minimum stop loss percentage (e.g., 0.10 for 10%)
        stop_loss_max: Maximum stop loss percentage (e.g., 0.30 for 30%)
        profit_multiplier: Profit taking as multiple of stop loss (e.g., 2.0)
        max_portfolio_exposure: Maximum total exposure as % of portfolio
        volatility_lookback: Days to look back for volatility calculation
    """
    max_position_size: float = 0.10
    stop_loss_min: float = 0.10
    stop_loss_max: float = 0.30
    profit_multiplier: float = 2.0
    max_portfolio_exposure: float = 0.95
    volatility_lookback: int = 20


class BaseStrategy(ABC):
    """
    Abstract base class for all trading strategies.
    
    This class defines the interface that all strategies must implement,
    whether they are LLM-based or traditional algorithmic strategies.
    """
    
    def __init__(self, name: str, risk_params: RiskParameters = None):
        """
        Initialize the strategy.
        
        Args:
            name: Unique identifier for this strategy
            risk_params: Risk management parameters (uses defaults if None)
        """
        self.name = name
        self.risk_params = risk_params or RiskParameters()
        self.last_rebalance = None
        self.performance_history = []
    
    @abstractmethod
    def generate_recommendations(
        self, 
        universe: List[str], 
        market_data: Dict[str, Any],
        current_positions: Dict[str, int],
        portfolio_value: float
    ) -> List[TradingRecommendation]:
        """
        Generate trading recommendations for the next period.
        
        This is the core method that each strategy must implement. It should
        analyze the market data and current positions to generate a list of
        trading recommendations.
        
        Args:
            universe: List of stock tickers available for trading (Russell 3000)
            market_data: Dictionary containing market data (prices, volumes, etc.)
            current_positions: Current holdings {ticker: quantity}
            portfolio_value: Current total portfolio value
            
        Returns:
            List of TradingRecommendation objects
            
        Raises:
            NotImplementedError: Must be implemented by subclasses
        """
        pass
    
    @abstractmethod
    def evaluate_positions(
        self,
        current_positions: Dict[str, int],
        market_data: Dict[str, Any],
        portfolio_value: float
    ) -> List[PositionEvaluation]:
        """
        Evaluate existing positions for stop-loss, profit-taking, or rebalancing.
        
        This method checks current positions against the strategy's rules
        to determine if any positions should be modified or closed.
        
        Args:
            current_positions: Current holdings {ticker: quantity}
            market_data: Current market data
            portfolio_value: Current total portfolio value
            
        Returns:
            List of PositionEvaluation objects with recommended actions
            
        Raises:
            NotImplementedError: Must be implemented by subclasses
        """
        pass
    
    def calculate_position_size(
        self, 
        ticker: str, 
        price: float, 
        portfolio_value: float,
        volatility: Optional[float] = None
    ) -> int:
        """
        Calculate appropriate position size based on risk parameters.
        
        Args:
            ticker: Stock symbol
            price: Current stock price
            portfolio_value: Total portfolio value
            volatility: Stock volatility (if available)
            
        Returns:
            Number of shares to buy
        """
        pass
    
    def calculate_stop_loss(
        self, 
        entry_price: float, 
        volatility: Optional[float] = None
    ) -> float:
        """
        Calculate stop loss price based on risk parameters.
        
        Args:
            entry_price: Price at which position was entered
            volatility: Stock volatility (if available)
            
        Returns:
            Stop loss price
        """
        pass
    
    def calculate_profit_target(self, entry_price: float, stop_loss: float) -> float:
        """
        Calculate profit taking price (always 2x stop loss).
        
        Args:
            entry_price: Price at which position was entered
            stop_loss: Stop loss price
            
        Returns:
            Profit target price
        """
        pass
    
    def get_strategy_info(self) -> Dict[str, Any]:
        """
        Get metadata about this strategy.
        
        Returns:
            Dictionary containing strategy information
        """
        pass
    
    def update_performance(self, metrics: Dict[str, float]) -> None:
        """
        Update strategy performance history.
        
        Args:
            metrics: Performance metrics for the period
        """
        pass