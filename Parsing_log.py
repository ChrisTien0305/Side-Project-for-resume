# Created by Chris Tien
import os
import pandas as pd

root_folder = r'XXXXXXXX'  # 資料夾的根目錄路徑
summary_lines = []
summary_margin = []
summary_result = []

for root, dirs, files in os.walk(root_folder):
    for file_name in files:
        if file_name.endswith('.SUMMARY'):
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                # 取出需要的行數
                selected_lines = [lines[i - 1].strip() for i in [1, 3, 4, 5, 6]]
                summary_lines.append(selected_lines)

                # 取出 DIMM Margin
                found = False
                temp_margin = []
                for line in lines:
                    if found:
                        temp_margin.append(line)
                    if "DIMM margin values:" in line:
                        found = True
                    if found and len(temp_margin) == 18:
                        break
                summary_margin.append(temp_margin)
                
                # 取出 DIMM Result
                for line in lines:
                    if "FINAL_RESULT:" in line: 
                        summary_result.append(line.strip())
                        break


# 轉換為 DataFrame
df = pd.DataFrame(summary_lines)

# 將 summary_margin 轉換為 DataFrame
df_margin = pd.DataFrame([' '.join(lines) for lines in summary_margin])

# 將 summary_result 轉換為 DataFrame
df_result = pd.DataFrame(summary_result)

# 將三個 DataFrame 串聯
result = pd.concat([df, df_margin, df_result], ignore_index=True, axis=1)

# 創建 Excel 文件
file_name = 'Parsing.xlsx'
result.to_excel(file_name, index=False)
