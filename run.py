import pytest
import os
import shutil
import time


def run_tests():
    report_dir = "./allure-results"
    html_report = "./allure-report"

    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)
        print(f"clean: {report_dir}")

    args = [
        "-vs",
        "--env=dev",
        "--alluredir", report_dir,
        "--reruns", "2",
        "--reruns-delay", "5",
        "-n", "auto",
        "tests/"
    ]

    print(f"🚀 start conducting the tests... time: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # --- 3. 调用 Pytest 执行 ---
    # 这里的 pytest.main() 等同于在命令行输入 pytest [args]
    exit_code = pytest.main(args)

    # --- 4. 自动生成 HTML 可视化报告 ---
    # 执行完后，利用系统命令自动生成静态报告文件夹 (可选)
    print("📊 Test execution complete, generating Allure report....")
    os.system(f"allure generate {report_dir} -o {html_report} --clean")

    print(f"✅ The report has been generated: {html_report}/index.html")
    return exit_code

if __name__ == "__main__":
    run_tests()
