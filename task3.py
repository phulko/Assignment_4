def analyze_method(data):
    report = {}

    for items in data:

        method = items["method"]
        error = items["error"]
        time_ms = items["time_ms"]

        if method not in report:
            report[method] = {
                "max_error": error,
                "total_time_ms": time_ms,
                "iterations": 1
            }
        else:
            if error > report[method]["max_error"]:
                report[method]["max_error"] = error

            report[method]["total_time_ms"] += time_ms
            report[method]["iterations"] += 1

    return report

experiments_data = [
    {"method": "Euler",
     "iteration": 1,
     "error": 0.15,
     "time_ms": 1.2
     },
    {"method": "Runge-Kutta",
     "iteration": 1,
     "error": 0.01,
     "time_ms": 3.5},
    {"method": "Euler",
     "iteration": 2,
     "error": 0.18,
     "time_ms": 1.3
     },
    {"method": "Runge-Kutta",
     "iteration": 2,
     "error": 0.008,
     "time_ms": 3.6
     },
    {"method": "Euler",
     "iteration": 3,
     "error": 0.22,
     "time_ms": 1.2
     },
    {"method": "Newton",
     "iteration": 1,
     "error": 0.05,
     "time_ms": 2.1
     },
    {"method": "CHECK",
     "iteration": 1,
     "error": 0.1,
     "time_ms": 1
     },
    {"method": "CHECK",
     "iteration": 5,
     "error": 0.01,
     "time_ms": 1.2
     },
]
report = analyze_method(experiments_data)
#print(report)

for method in report:
    print(f"Method: {method}")
    print(f"  Max error: {report[method]['max_error']}")
    print(f"  Total time (ms): {report[method]['total_time_ms']}")
    print(f"  Iterations: {report[method]['iterations']}")