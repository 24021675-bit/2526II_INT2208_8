def classify_triangle(a, b, c):
    """
    Module phân tích và trả về loại tam giác dựa trên độ dài 3 cạnh.
    """
    # 1. Ràng buộc dữ liệu: phải là số nguyên (int)
    # Trong Python, True/False cũng thuộc kiểu int nên cần check kỹ bằng type()
    if type(a) is not int or type(b) is not int or type(c) is not int:
        return "Invalid Input"

    # 2. Ràng buộc miền giá trị: từ 1 đến 100
    if not (1 <= a <= 100) or not (1 <= b <= 100) or not (1 <= c <= 100):
        return "Invalid Input"

    # 3. Kiểm tra bất đẳng thức tam giác
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a Triangle"

    # 4. Phân loại tam giác hợp lệ
    if a == b and b == c:
        return "Equilateral"  # Tam giác đều
    elif a == b or b == c or a == c:
        return "Isosceles"    # Tam giác cân
    else:
        return "Scalene"      # Tam giác thường


# ==============================================================================
# PHẦN CHỨNG MINH: CHẠY TỰ ĐỘNG TOÀN BỘ CÁC TEST CASES GỘP CHUNG
# ==============================================================================

test_cases = [
    # Nhóm biên lỗi ngoài khoảng [1, 100] hoặc sai kiểu dữ liệu
    {"id": "TC01", "a": 0, "b": 50, "c": 50, "expected": "Invalid Input"},
    {"id": "TC02", "a": 50, "b": 101, "c": 50, "expected": "Invalid Input"},
    {"id": "TC03", "a": 50, "b": 50, "c": -5, "expected": "Invalid Input"},
    {"id": "TC04", "a": 5.5, "b": 5, "c": 5, "expected": "Invalid Input"},
    
    # Nhóm vi phạm bất đẳng thức tam giác
    {"id": "TC05", "a": 1, "b": 2, "c": 3, "expected": "Not a Triangle"},
    {"id": "TC06", "a": 5, "b": 1, "c": 2, "expected": "Not a Triangle"},
    
    # Nhóm hợp lệ - Tam giác đều (Equilateral)
    {"id": "TC07", "a": 1, "b": 1, "c": 1, "expected": "Equilateral"},
    {"id": "TC08", "a": 100, "b": 100, "c": 100, "expected": "Equilateral"},
    
    # Nhóm hợp lệ - Tam giác cân (Isosceles)
    {"id": "TC09", "a": 5, "b": 5, "c": 3, "expected": "Isosceles"},
    {"id": "TC10", "a": 5, "b": 3, "c": 5, "expected": "Isosceles"},
    {"id": "TC11", "a": 3, "b": 5, "c": 5, "expected": "Isosceles"},
    
    # Nhóm hợp lệ - Tam giác thường (Scalene)
    {"id": "TC12", "a": 3, "b": 4, "c": 5, "expected": "Scalene"}
]

def run_triangle_tests():
    # In tiêu đề bảng kết quả
    print(f"{'Test ID':<9} {'Tham số đầu vào (a, b, c)':<25} {'Kỳ vọng (Expected)':<18} {'Thực tế (Actual)':<18} {'Trạng thái'}")
    print("-" * 88)
    
    all_passed = True
    
    for tc in test_cases:
        actual = classify_triangle(tc["a"], tc["b"], tc["c"])
        is_passed = (actual == tc["expected"])
        status = "✅ PASSED" if is_passed else "❌ FAILED"
        
        if not is_passed:
            all_passed = False
            
        inputs_str = f"({tc['a']}, {tc['b']}, {tc['c']})"
        print(f"{tc['id']:<9} {inputs_str:<25} {tc['expected']:<18} {actual:<18} {status}")
        
    print("-" * 88)
    
    if all_passed:
        print("🎉 CHỨNG MINH THÀNH CÔNG: Toàn bộ 12/12 Test Cases phân loại Tam giác đã PASSED!")
    else:
        print("⚠️ CẢNH BÁO: Phát hiện kịch bản test bị lỗi!")

# Chạy trực tiếp bộ test khi run file này
if __name__ == "__main__":
    run_triangle_tests()