"""
Campus Delivery Project -- Starter Scaffold
==============================================

This file gives you two things:

  1. load_data()          -- reads the three CSV files
  2. check_solution()     -- an INDEPENDENT checker: tells you whether
                              your delivery plan is legal, and what it
                              costs. Run this constantly while you work.

It does NOT tell you how to solve the problem. That's your team's job.
You've learned linear/binary search, sorting, heaps, BSTs, hash tables,
graph traversal, Dijkstra, MSTs, dynamic programming, and greedy
algorithms this semester -- which of those you use, and how you combine
them, is a design decision your team makes and defends in your report.

Some teams might reach for a hash table plus a priority queue plus
Dijkstra. Others might combine Dijkstra with dynamic programming on a
small subset. Others might do something we haven't listed. All of
these are legitimate starting points -- there is no single intended
answer.


THE PROBLEM
-------------
A delivery agent starts at the depot (see DATASET_GUIDE.txt), carries
out a list of delivery requests, and returns to the depot. Each
request means: go to its pickup building, then go to its dropoff
building. The agent can carry several items at once, up to the weight
limit. Your job is to decide the ORDER in which to do everything, to
keep total travel cost as low as possible.


YOUR SOLUTION FORMAT
-----------------------
Return a plan as a list of stops, like this:

    plan = [
        {"building": "B16", "action": "start"},
        {"building": "B04", "action": "pickup",  "request_id": "R01"},
        {"building": "B05", "action": "dropoff", "request_id": "R01"},
        {"building": "B16", "action": "end"},
    ]

Rules:
  - The plan must start and end at the depot.
  - Every request must be picked up once and dropped off once, dropoff
    after pickup.
  - Total weight carried at once must never exceed capacity.

You don't need to use directly-connected buildings for consecutive
stops -- check_solution() assumes you walk the shortest path between
whatever stops you choose, and computes that cost for you. You are
choosing the ORDER of stops, not the individual footpaths.
"""

import csv
import heapq


# ---------------------------------------------------------------------
# Loading the data
# ---------------------------------------------------------------------

def load_data(building_file="buildings.csv", pathway_file="pathways.csv",
              delivery_file="deliveries.csv"):
    """Read the three CSV files. Returns (buildings, pathways, deliveries),
    each a list of dicts."""
    with open(building_file, newline="") as f:
        buildings = list(csv.DictReader(f))
    with open(pathway_file, newline="") as f:
        pathways = list(csv.DictReader(f))
        for p in pathways:
            p["distance_m"] = float(p["distance_m"])
            p["time_s"] = float(p["time_s"])
    with open(delivery_file, newline="") as f:
        deliveries = list(csv.DictReader(f))
        for d in deliveries:
            d["size_kg"] = float(d["size_kg"])
    return buildings, pathways, deliveries


# ---------------------------------------------------------------------
# Independent cost model, used by check_solution().
# You'll likely want your own faster version inside your solver --
# this one favors clarity.
# ---------------------------------------------------------------------

def _shortest_costs(pathways, buildings):
    graph = {b["building_id"]: [] for b in buildings}
    for p in pathways:
        graph[p["building_a"]].append((p["building_b"], p["distance_m"]))
        graph[p["building_b"]].append((p["building_a"], p["distance_m"]))

    costs = {}
    for source in graph:
        dist = {source: 0}
        queue = [(0, source)]
        seen = set()
        while queue:
            d, node = heapq.heappop(queue)
            if node in seen:
                continue
            seen.add(node)
            for neighbour, w in graph[node]:
                nd = d + w
                if neighbour not in dist or nd < dist[neighbour]:
                    dist[neighbour] = nd
                    heapq.heappush(queue, (nd, neighbour))
        costs[source] = dist
    return costs


# ---------------------------------------------------------------------
# check_solution -- do not modify. This is what we use for grading and
# for comparing results across teams, so use the SAME function you're
# handed rather than a lookalike you wrote yourself.
# ---------------------------------------------------------------------

def check_solution(buildings, pathways, deliveries, plan,
                    depot="B16", capacity=15.0):
    """
    Check whether `plan` is a legal delivery plan, and score it.

    Returns a dict:
        {
          "valid": bool,
          "errors": [str, ...],
          "total_distance_m": number,
          "requests_delivered": int,
          "requests_total": int,
        }
    """
    errors = []
    costs = _shortest_costs(pathways, buildings)
    valid_buildings = set(costs)
    requests = {d["request_id"]: d for d in deliveries}

    if not plan or plan[0].get("building") != depot or plan[0].get("action") != "start":
        errors.append("plan must start at the depot with action 'start'")
    if not plan or plan[-1].get("building") != depot or plan[-1].get("action") != "end":
        errors.append("plan must end at the depot with action 'end'")

    picked_up, dropped_off = set(), set()
    onboard = 0.0
    total_distance = 0.0

    for i, stop in enumerate(plan):
        building = stop.get("building")
        action = stop.get("action")

        if building not in valid_buildings:
            errors.append(f"stop {i}: unknown building {building!r}")
            continue

        if i > 0:
            prev = plan[i - 1]["building"]
            if prev in valid_buildings:
                leg = costs[prev].get(building)
                if leg is None:
                    errors.append(f"stop {i}: no route from {prev} to {building}")
                else:
                    total_distance += leg

        request_id = stop.get("request_id")

        if action == "pickup":
            if request_id not in requests:
                errors.append(f"stop {i}: unknown request {request_id!r}")
                continue
            if request_id in picked_up:
                errors.append(f"request {request_id} picked up more than once")
            if requests[request_id]["pickup"] != building:
                errors.append(f"request {request_id} picked up at the wrong building")
            picked_up.add(request_id)
            onboard += requests[request_id]["size_kg"]
            if onboard > capacity + 1e-9:
                errors.append(f"stop {i}: over capacity ({onboard:.1f} kg > {capacity} kg)")

        elif action == "dropoff":
            if request_id not in requests:
                errors.append(f"stop {i}: unknown request {request_id!r}")
                continue
            if request_id not in picked_up:
                errors.append(f"request {request_id} dropped off before pickup")
            if request_id in dropped_off:
                errors.append(f"request {request_id} dropped off more than once")
            if requests[request_id]["dropoff"] != building:
                errors.append(f"request {request_id} dropped off at the wrong building")
            dropped_off.add(request_id)
            onboard -= requests[request_id]["size_kg"]

        elif action not in ("start", "end"):
            errors.append(f"stop {i}: unknown action {action!r}")

    missing = set(requests) - dropped_off
    if missing:
        errors.append(f"{len(missing)} request(s) never delivered: {sorted(missing)[:5]}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "total_distance_m": round(total_distance, 1),
        "requests_delivered": len(dropped_off),
        "requests_total": len(requests),
    }


def print_report(result, label=""):
    """Pretty-print a check_solution() result. Put this in your report."""
    print(f"--- {label} ---" if label else "---")
    print(f"valid:               {result['valid']}")
    if not result["valid"]:
        for e in result["errors"][:6]:
            print(f"    - {e}")
    print(f"total distance:      {result['total_distance_m']} m")
    print(f"requests delivered:  {result['requests_delivered']} / {result['requests_total']}")


# ---------------------------------------------------------------------
# YOUR WORK STARTS HERE
# ---------------------------------------------------------------------

def solve(buildings, pathways, deliveries, depot="B16", capacity=15.0):
    """
    Produce a delivery plan (see SOLUTION FORMAT above).

    Before writing code, discuss as a team:
      - What do you need to look up repeatedly, and how will you store
        it so those lookups are fast?
      - How will you decide what order to visit things in?
      - How will you decide which requests to carry together, given
        the capacity limit?
    """
    raise NotImplementedError("Design and implement your solver here.")


if __name__ == "__main__":
    buildings, pathways, deliveries = load_data()

    for label, n in [("SMALL", 8), ("MEDIUM", 16), ("FULL", 30)]:
        subset = deliveries[:n]
        plan = solve(buildings, pathways, subset)
        result = check_solution(buildings, pathways, subset, plan)
        print_report(result, label=f"{label} (n={n})")
