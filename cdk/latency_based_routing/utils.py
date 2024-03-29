import os

from latency_based_routing.constants import MASTER_REGION


def is_master_region() -> bool:
    return os.getenv('REGION').lower() == MASTER_REGION
