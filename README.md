# GPT Trading Strategy Comparison

A comprehensive trading strategy comparison tool that evaluates 4 LLM-based strategies against 3 traditional strategies using separate Alpaca paper trading portfolios.

## Overview

This system compares 7 different trading strategies:

**LLM-Based Strategies (4):**
- ChatGPT (GPT-4) with thinking & research mode
- DeepSeek Reasoner with enhanced reasoning
- Claude Sonnet with analytical capabilities  
- Gemini Pro with multimodal analysis

**Traditional Strategies (3):**
- Pure Momentum Strategy
- Pure Mean Reversion Strategy
- Random Strategy (Sharpe ratio weighted)

Each strategy operates with its own dedicated Alpaca paper trading portfolio for independent performance tracking and comparison.

## Key Features

- **Separate Portfolios**: Each strategy gets its own Alpaca paper trading account
- **Weekly Rebalancing**: Automated weekly portfolio rebalancing on Fridays
- **Russell 3000 Universe**: All trades constrained to Russell 3000 stocks
- **Risk Management**: Comprehensive risk controls with stop losses and position sizing
- **Performance Analysis**: Real-time performance tracking and comparison
- **Short-term Focus**: Optimized for short-term returns (few weeks max holding)

## Architecture

```
src/
├── strategies/          # Trading strategies
│   ├── base.py         # Base strategy interface
│   ├── llm_strategies/ # LLM-based strategies
│   └── traditional/    # Traditional strategies
├── portfolio/          # Portfolio management
├── brokers/           # Alpaca integration & multi-portfolio management
├── data/              # Data providers & Russell 3000 universe
├── analysis/          # Performance analysis & comparison
└── utils/             # Configuration & utilities
```

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -e .
   ```

2. **Configuration**:
   ```bash
   # Create sample configuration
   python -m src.main --create-config
   
   # Edit config/config.json with your API keys:
   # - OpenAI API key for ChatGPT
   # - DeepSeek API key  
   # - Anthropic API key for Claude
   # - Google AI API key for Gemini
   # - 7 separate Alpaca paper trading API keys (one per strategy)
   ```

3. **Run the System**:
   ```bash
   # Start the comparison system
   python -m src.main --config config/config.json
   
   # Or use the installed command
   gpt-trading --config config/config.json
   ```

## Strategy Details

### LLM Strategies
Each LLM strategy generates 5-10 stock recommendations with:
- Stock ticker (Russell 3000 only)
- Buy quantity based on risk characteristics
- Stop loss condition (10% to 30%, min 1 vol)
- Profit taking condition (2x stop loss)
- Max holding period (few weeks)
- Re-evaluation schedule

### Traditional Strategies  
- **Momentum**: Identifies stocks with strong price momentum across multiple timeframes
- **Mean Reversion**: Finds oversold stocks likely to bounce back to historical mean
- **Random**: Baseline strategy with Sharpe ratio weighted random selection

### Risk Management
- Position sizing based on volatility and risk characteristics
- Stop loss: 10% minimum, 1 volatility to 30% maximum
- Profit taking: Always 2x stop loss distance
- Weekly rebalancing with short-term holding focus

## Multi-Portfolio Architecture

Each strategy operates independently with:
- Dedicated Alpaca paper trading account
- Separate $100,000 starting capital
- Independent trade execution
- Isolated performance tracking
- Real-time position management

## Performance Tracking

The system provides comprehensive analysis:
- Real-time performance metrics
- Risk-adjusted returns (Sharpe, Sortino, Calmar ratios)
- Drawdown analysis
- Win/loss statistics  
- Strategy comparison and ranking
- Daily and weekly reports

## Usage Examples

```bash
# Run all strategies
gpt-trading

# Run specific strategies only
gpt-trading --strategies chatgpt momentum random_sharpe

# Dry run mode (simulation)
gpt-trading --dry-run

# Analysis mode
gpt-trading --mode analyze
```

## Configuration

Key configuration sections:
- `llm_strategies`: API keys, models, and parameters for each LLM
- `alpaca_credentials`: Separate API credentials for each strategy portfolio
- `risk_management`: Stop loss, position sizing, and risk limits
- `scheduling`: Rebalancing frequency and timing

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/

# Type checking
mypy src/
```

## Important Notes

⚠️ **Paper Trading Only**: This system is designed for paper trading evaluation only. Real money trading requires additional safeguards and testing.

⚠️ **API Keys Required**: You need valid API keys for all LLM providers and 7 separate Alpaca paper trading accounts.

⚠️ **Short-term Focus**: Strategies are optimized for short-term returns with weekly rebalancing. Not suitable for long-term investing.

## License

This project is for educational and research purposes only.