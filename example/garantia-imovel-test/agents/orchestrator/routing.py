FLOW_ORDER = [
    "registry_fetcher",
    "lienability_analyzer",
    "market_price_researcher",
    "guarantee_decider",
    "critic",
]


def route_next(current_node: str) -> str:
    index = FLOW_ORDER.index(current_node)

    if index == len(FLOW_ORDER) - 1:
        return "end"

    return FLOW_ORDER[index + 1]
