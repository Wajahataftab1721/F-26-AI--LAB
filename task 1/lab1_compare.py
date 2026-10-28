from lab1_rules import check_scholarship
def run_comparison():
    case = {
        "score": 85,
        "documents_complete": True,
        "attendance": 60,
        "disciplinary_cases": 0,
    }
    rule_result, reason = check_scholarship(
        case["score"],
        case["documents_complete"],
        case["attendance"],
        case["disciplinary_cases"],
    )
    conversational_response = "The student should qualify because the score is high."
    conversational_decision = "Review"   # what the response implies
    print("AI Lab 1: Scholarship Case Comparison")
    print("Input:", case)
    print("Rule-based decision:", rule_result)
    print("Rule-based reason:", reason)
    print("Hypothetical conversational response:", conversational_response)
    print("Decision suggested by conversational response:", conversational_decision)
    agree = rule_result == conversational_decision
    print("Agreement:", "YES" if agree else "NO")
    if not agree:
        print("Explanation: the conversational-style answer focuses on the score "
              "and overlooks the attendance condition.")
if __name__ == "__main__":
    run_comparison()
