import enum


class TransactionEnum(enum.Enum):
    replenishment = "replenishment"
    purchase = "purchase"
    withdrawal = "withdrawal"
