import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__)
    )
)

from fintrust_migration import classify_instances

portfolio, untagged = classify_instances()

print("Portfolio:", portfolio)
print("Untagged:", untagged)