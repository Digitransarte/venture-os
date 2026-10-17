"""Pure, dependency-free SaaS unit economics scenario calculations.

All money values are *user-entered EUR, excluding VAT*; no provider price is
hardcoded or retrieved. A projection is never recorded as actual revenue.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil, isfinite


@dataclass(frozen=True)
class Scenario:
    paying_accounts: int = 0
    subscription_price_eur_ex_vat: float = 0.0
    ai_calls_per_account: int = 0
    input_tokens_per_call: int = 0
    output_tokens_per_call: int = 0
    input_eur_per_million_tokens: float = 0.0
    output_eur_per_million_tokens: float = 0.0
    other_ai_tools_eur_per_account: float = 0.0
    storage_eur_per_account: float = 0.0
    support_minutes_per_account: float = 0.0
    support_hourly_eur: float = 0.0
    payment_percent: float = 0.0
    payment_fixed_eur_per_account: float = 0.0
    monthly_hosting_eur: float = 0.0
    monthly_backup_monitoring_eur: float = 0.0
    monthly_other_fixed_eur: float = 0.0


def simulate(s: Scenario) -> dict:
    """Monthly what-if, without guessing API costs, subscriptions or usage.

    Result is an estimate excluding VAT, customer acquisition, income/corporate
    taxes and one-off development costs unless the user has included them in
    the explicit cost inputs.
    """
    for field, value in vars(s).items():
        if isinstance(value, bool) or not isinstance(value, (float, int)):
            raise ValueError(f"{field} must be numeric")
        if not isfinite(value) or value < 0:
            raise ValueError(f"{field} must be finite and non-negative")
        if field in ("paying_accounts", "ai_calls_per_account",
                     "input_tokens_per_call", "output_tokens_per_call") and not isinstance(value, int):
            raise ValueError(f"{field} must be an integer")
    if s.payment_percent > 100:
        raise ValueError("payment_percent cannot exceed 100")
    ai_tokens_eur_per_account = s.ai_calls_per_account * (
        s.input_tokens_per_call * s.input_eur_per_million_tokens / 1_000_000
        + s.output_tokens_per_call * s.output_eur_per_million_tokens / 1_000_000
    )
    ai_eur_per_account = ai_tokens_eur_per_account + s.other_ai_tools_eur_per_account
    support_eur_per_account = s.support_minutes_per_account / 60 * s.support_hourly_eur
    payment_eur_per_account = (s.subscription_price_eur_ex_vat * s.payment_percent / 100
                               + s.payment_fixed_eur_per_account)
    variable_eur_per_account = (ai_eur_per_account + s.storage_eur_per_account
                                + support_eur_per_account + payment_eur_per_account)
    monthly_fixed = (s.monthly_hosting_eur + s.monthly_backup_monitoring_eur
                     + s.monthly_other_fixed_eur)
    revenue = s.paying_accounts * s.subscription_price_eur_ex_vat
    variable_total = s.paying_accounts * variable_eur_per_account
    total_cost = variable_total + monthly_fixed
    contribution_per_account = s.subscription_price_eur_ex_vat - variable_eur_per_account
    break_even_accounts = ceil(monthly_fixed / contribution_per_account) if contribution_per_account > 0 else None
    if monthly_fixed == 0 and contribution_per_account > 0:
        break_even_accounts = 0
    return {
        "revenue_eur": revenue,
        "ai_eur_per_account": ai_eur_per_account,
        "ai_tokens_eur_per_account": ai_tokens_eur_per_account,
        "support_eur_per_account": support_eur_per_account,
        "payment_eur_per_account": payment_eur_per_account,
        "variable_eur_per_account": variable_eur_per_account,
        "variable_eur_total": variable_total,
        "fixed_eur_total": monthly_fixed,
        "total_cost_eur": total_cost,
        "contribution_eur_per_account": contribution_per_account,
        "operating_result_eur": revenue - total_cost,
        "break_even_accounts": break_even_accounts,
        "estimate_only": True,
    }
