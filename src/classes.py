from enum import Enum

class InvestorProfile(Enum):

    CONSERVATIVE = "CONSERVATIVE"
    MODERATE = "MODERATE"
    AGGRESIVE = "AGGRESIVE"

    def investment_distribution(self):
        match self:
            case InvestorProfile.CONSERVATIVE:
                profile_distribuition = {"Fixed Income": 0.75, "Equities": 0.10, "International": 0.10, "Cryptocurrencies": 0.05}
            case InvestorProfile.MODERATE:
                profile_distribuition = {"Fixed Income": 0.45, "Equities": 0.25, "International": 0.20, "Cryptocurrencies": 0.05}
            case InvestorProfile.AGGRESIVE:
                profile_distribuition = {"Fixed Income": 0.05, "Equities": 0.55, "International": 0.25, "Cryptocurrencies": 0.15}
        
        return profile_distribuition

class Asset():
    
    def __init__(self, ticker, acquisition_value, asset_type, num_shares, actual_value):
        self.ticker = ticker
        self.asset_type = asset_type
        self.acquisition_value = acquisition_value
        self.num_shares = num_shares
        self.actual_value = actual_value

class Transaction():
    def __init__(self, asset_ticker, share_value, num_shares, date):
        self.asset_ticker = asset_ticker
        self.share_value = share_value
        self.num_shares = num_shares
        self.date = date

class Wallet:
    def __init__(self, balance, profile: InvestorProfile, contribution_value):
        self.balance = balance
        self.profile = profile
        self.contribution_value = contribution_value
        self.assets_hold = {}
        self.history = []
    
    def add_asset(self, asset: Asset):
        self.assets_hold[asset.ticker] = asset
    
    def add_transaction(self, transaction: Transaction):
        self.history.append(transaction)
    
    def get_total_value(self):
        total = 0
        for asset in self.assets_hold.values():
            if asset.actual_value:
                total += asset.actual_value * asset.num_shares
        return total
