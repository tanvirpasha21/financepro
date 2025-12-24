from dataclasses import dataclass

@dataclass
class NetWorthInput:
    cash: float
    income: float
    expenses: float
    debt: float
    apr: float
    payment: float
    months: int
    boost: bool = False

@dataclass
class DebtInput:
    principal: float
    annual_interest: float
    monthly_payment: float
    years: int

@dataclass
class BehaviourInput:
    spending_score: int
    saving_score: int
    investment_score: int

@dataclass
class Profile:
    cash: float
    income: float
    fixed_expenses: float
    variable_expenses: float
    debt: float
    apr: float

