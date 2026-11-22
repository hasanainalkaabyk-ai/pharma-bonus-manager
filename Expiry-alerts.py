from dataclasses import dataclass
from datetime import date

@dataclass
class BatchItem:
item_name: str
supplier_name: str
total_units: int
bonus_units: int
expiry_date: date

@property
def bonus_ratio_percent(self) -> float:
    if self.total_units <= 0:
        return 0.0
    return round((self.bonus_units / self.total_units) * 100.0, 1)
def get_expiring_batches(
batches: list[BatchItem],
days_threshold: int = 90,
today: date | None = None,
) -> list[dict]:
"""
Return batches expiring within days_threshold days, sorted by urgency.
"""
ref_date = today or date.today()
alerts = []

for batch in batches:
    days_remaining = (batch.expiry_date - ref_date).days
    if days_remaining <= days_threshold:
        if days_remaining < 0:
            status = "EXPIRED"
        elif days_remaining <= 30:
            status = "CRITICAL"
        else:
            status = "WARNING"

        alerts.append(
            {
                "item_name": batch.item_name,
                "supplier_name": batch.supplier_name,
                "days_remaining": days_remaining,
                "status": status,
                "total_units": batch.total_units,
                "bonus_ratio_percent": batch.bonus_ratio_percent,
            }
        )

alerts.sort(key=lambda x: x["days_remaining"])
return alerts
if name == "main":
sample_batches = [
BatchItem(
item_name="Amoxicillin 500mg Cap",
supplier_name="Al-Noor Pharma",
total_units=120,
bonus_units=20,
expiry_date=date(2026, 12, 15),
),
BatchItem(
item_name="Vitamin D3 Drops",
supplier_name="MedSupply Co.",
total_units=60,
bonus_units=10,
expiry_date=date(2027, 4, 10),
),
]

for alert in get_expiring_batches(sample_batches, days_threshold=90, today=date(2026, 11, 22)):
    print(alert)
