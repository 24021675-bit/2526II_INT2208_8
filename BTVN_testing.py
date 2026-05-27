def loan_approval_system(age: int, income: float, credit_score: int, employment: str) -> str:
    # 1. Kiểm tra ràng buộc dữ liệu đầu vào (Data Validation)
    if not isinstance(age, int) or not (18 <= age <= 65):
        return "Invalid Input"
    
    if not isinstance(income, (int, float)) or not (5.0 <= round(income, 1) <= 500.0):
        return "Invalid Input"
        
    if not isinstance(credit_score, int) or not (300 <= credit_score <= 850):
        return "Invalid Input"
        
    if employment not in ["C", "F"]:
        return "Invalid Input"

    # Làm tròn income đến 1 chữ số thập phân theo yêu cầu đề bài
    income = round(income, 1)

    # 2. Phân loại rủi ro tín dụng (Risk Classification)
    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    # 3. Thực thi Logic Nghiệp vụ quyết định khoản vay
    if risk == "High":
        return "REJECT"

    if income < 15.0:
        if employment == "C" and risk == "Low":
            return "MANUAL REVIEW"
        else:
            return "REJECT"
    else:  # income >= 15.0
        if risk in ["Low", "Medium"]:
            if employment == "C":
                return "APPROVE"
            elif employment == "F":
                return "MANUAL REVIEW"
                
    return "REJECT"  # Dự phòng bảo mật logic


# ==============================================================================
# HỆ THỐNG KIỂM THỬ TỰ ĐỘNG (PROVING THE TESTS PASS)
# ==============================================================================

test_cases = [
    {"id": "TC01", "age": 17, "income": 20.0, "credit_score": 750, "employment": "C", "expected": "Invalid Input"},
    {"id": "TC02", "age": 66, "income": 20.0, "credit_score": 750, "employment": "C", "expected": "Invalid Input"},
    {"id": "TC03", "age": 30, "income": 4.9,  "credit_score": 750, "employment": "C", "expected": "Invalid Input"},
    {"id": "TC04", "age": 30, "income": 500.1,"credit_score": 750, "employment": "C", "expected": "Invalid Input"},
    {"id": "TC05", "age": 30, "income": 20.0, "credit_score": 299, "employment": "C", "expected": "Invalid Input"},
    {"id": "TC06", "age": 30, "income": 20.0, "credit_score": 851, "employment": "C", "expected": "Invalid Input"},
    {"id": "TC07", "age": 30, "income": 20.0, "credit_score": 750, "employment": "X", "expected": "Invalid Input"},
    
    {"id": "TC08", "age": 18, "income": 500.0,"credit_score": 300, "employment": "C", "expected": "REJECT"},
    {"id": "TC09", "age": 65, "income": 15.0, "credit_score": 500, "employment": "F", "expected": "REJECT"},
    {"id": "TC10", "age": 30, "income": 15.0, "credit_score": 501, "employment": "C", "expected": "APPROVE"},
    {"id": "TC11", "age": 30, "income": 100.0,"credit_score": 850, "employment": "C", "expected": "APPROVE"},
    {"id": "TC12", "age": 30, "income": 25.0, "credit_score": 700, "employment": "F", "expected": "MANUAL REVIEW"},
    {"id": "TC13", "age": 30, "income": 25.0, "credit_score": 701, "employment": "F", "expected": "MANUAL REVIEW"},
    {"id": "TC14", "age": 30, "income": 14.9, "credit_score": 750, "employment": "C", "expected": "MANUAL REVIEW"},
    {"id": "TC15", "age": 30, "income": 5.0,  "credit_score": 750, "employment": "F", "expected": "REJECT"},
    {"id": "TC16", "age": 30, "income": 10.0, "credit_score": 600, "employment": "C", "expected": "REJECT"},
]

def run_tests():
    print(f"{'Test ID':<10}{'Input Parameters':<45}{'Expected':<18}{'Actual':<18}{'Status'}")
    print("-" * 100)
    
    all_passed = True
    for tc in test_cases:
        actual = loan_approval_system(tc["age"], tc["income"], tc["credit_score"], tc["employment"])
        status = "✅ PASSED" if actual == tc["expected"] else "❌ FAILED"
        if actual != tc["expected"]:
            all_passed = False
            
        inputs_str = f"({tc['age']}, {tc['income']}, {tc['credit_score']}, '{tc['employment']}')"
        print(f"{tc['id']:<10}{inputs_str:<45}{tc['expected']:<18}{actual:<18}{status}")
        
    print("-" * 100)
    if all_passed:
        print(" Toàn bộ 16/16 Test Cases đã Pass!")
    else:
        print("Có test case bị lỗi. Vui lòng kiểm tra lại logic.")

# Thực thi test
run_tests()