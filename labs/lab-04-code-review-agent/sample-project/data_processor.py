from typing import Any

# Intentionally flawed code for Lab 4 code review exercise


def process_records(records):
    # N+1 pattern: database-like lookup inside a loop
    results = []
    for record in records:
        # Simulated: fetching related data for each record individually
        related = fetch_related_data(record["id"])
        results.append({**record, "related": related})
    return results


def fetch_related_data(record_id):
    # Simulated expensive operation
    import time
    time.sleep(0.001)
    return {"details": f"data_for_{record_id}"}


def calculate_statistics(data: list) -> dict:
    # Loads everything into memory, no streaming
    total = sum([x["value"] for x in data])
    average = total / len(data)

    # Repeated expensive computation inside loop
    results = []
    for item in data:
        # Recalculates total on every iteration
        running_total = sum([x["value"] for x in data])
        results.append(item["value"] / running_total)

    return {"total": total, "average": average, "ratios": results}


def find_duplicates(items: list) -> list:
    # O(n²) lookup when a set would be O(n)
    duplicates = []
    seen = []
    for item in items:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.append(item)
    return duplicates


def transform_data(raw_data: Any, magic_threshold=42, magic_multiplier=3.14159):
    # Magic numbers, unclear variable names
    r = []
    for x in raw_data:
        if x > magic_threshold:
            r.append(x * magic_multiplier)
        else:
            r.append(x)
    return r


def process_file(filepath):
    # Missing error handling for file I/O
    f = open(filepath, "r")
    content = f.read()
    f.close()
    return content.split("\n")
