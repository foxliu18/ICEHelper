import sys

import pandas as pd
import os
from datetime import datetime

class ReadExcelUtil:
    file_name = "/Users/liu/Code/PycharmProjects/ICEHelper/data/input.xlsx"
    def __init__(self):
        self.df_out_dict = {}
        self.df = None
        print("init readExcelUtil")


    def set_file_name(self, file_name):
        if file_name != "":
            self.file_name = file_name
            return True
        else:
            return False

    from typing import Optional
    import pandas as pd

    def open_file(self, sheet_name: str = "") -> Optional[pd.DataFrame]:
        try:
            self.df = pd.read_excel(
                self.file_name,
                sheet_name=sheet_name if sheet_name else 0,  # 空字符串时读取第一个sheet
                engine='openpyxl'  # 明确指定解析引擎
            )
            return self.df
        except FileNotFoundError:
            print(f"Error: File {self.file_name} not found")
            return None
        except ValueError as e:
            if "Worksheet named" in str(e):
                print(f"Error: Sheet '{sheet_name}' not found in {self.file_name}")
            else:
                print(f"Excel read error: {str(e)}")
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None

    def filter_excel(self, filter_list, filter_type):
        # 参数有效性校验
        if filter_type not in {0, 1, 2}:
            raise ValueError("filter_type 必须是 0(前缀)/1(包含)/2(后缀)")

        # 预处理过滤器列表
        filter_list = list(set(filter_list))
        if not filter_list:
            return None

        # 初始化结果容器
        self.df_out_dict.clear()
        for item in filter_list:
            self.df_out_dict[item] = pd.DataFrame()
        self.df_out_dict['first_col'] = pd.DataFrame()
        self.df_out_dict['first_col'] = pd.DataFrame({
            self.df.columns[0] : self.df[self.df.columns[0]].to_numpy()
        })
        # 列驱动处理逻辑
        for col in self.df.columns:
            for item in filter_list:
                match = False
                if filter_type == 0 and col.startswith(item):
                    match = True
                elif filter_type == 1 and item in col:
                    match = True
                elif filter_type == 2 and col.endswith(item):
                    match = True

                if match:
                    # 保持索引对齐的列添加方式
                    self.df_out_dict[item] = pd.concat([
                        self.df_out_dict[item],
                        self.df[[col]]
                    ], axis=1)

        return self.df_out_dict

    def write_to_excel(self, filter_list, is_split):
        """将处理后的数据写入Excel文件

        Args:
            filter_list (list): 需要处理的筛选键列表，决定输出哪些数据
            is_split (bool): 拆分模式标志，True表示按不同键拆分到多个文件，False表示合并到单个文件

        Returns:
            tuple: (执行状态, 结果消息, 输出路径)
            状态为布尔值表示成功与否，消息字符串描述详细信息，输出路径为最终文件存放目录
        """
        # 生成日期格式的目录名
        now = datetime.now()
        date_str = now.strftime("%Y%m%d")

        # 构造输出路径（兼容不同操作系统）
        base_dir = os.path.dirname(self.file_name)
        out_dir = os.path.join(base_dir, "out", date_str)

        # 创建输出目录（包含存在性检查）
        try:
            os.makedirs(out_dir, exist_ok=True)
        except OSError as e:
            return False, f"目录创建失败：{str(e)}", out_dir

        new_df = self.df_out_dict.copy()
        first_col_df = new_df['first_col']
        if is_split:
            # 拆分模式：每个键单独生成文件

            # 显式获取列名
            col_name = self.df.columns[0]
            for item in filter_list:
                df = new_df.get(item)
                df.insert(0, col_name, first_col_df[col_name].to_numpy())
                if df is not None:
                    # 文件名特殊字符过滤处理
                    safe_item = "".join(c for c in item if c not in r'\/:*?"<>|')
                    file_path = os.path.join(out_dir, f"{safe_item}.xlsx")
                    df.to_excel(file_path, index=False)
        else:
            # 合并模式前置检查
            if not filter_list:
                return False, "筛选列表为空", out_dir

            # 获取基准数据表
            first_key = filter_list[0]
            first_df = new_df.get(first_key)
            if first_df is None:
                return False, f"无效的键：{first_key}", out_dir
            max_index = 0
            for item in filter_list:
                df = new_df.get(item)
                if df is not None and len(df.columns) > max_index:
                    max_index = len(df.columns)

            # 显式获取列名
            col_name = first_col_df.columns[0]
            # 直接构建DataFrame避免多次内存分配
            out = pd.DataFrame({
                col_name: first_col_df[col_name].to_numpy()  # 使用更现代的to_numpy()
            })

            try:
                for col_idx in range(max_index):
                    for item in filter_list:
                        df = new_df.get(item)
                        if df is None or col_idx >= len(df.columns):
                            continue
                        col_name = df.columns[col_idx]
                        out[col_name] = df.iloc[:, col_idx].values
            except Exception as e:
                return False, f"数据合并失败：{str(e)}", out_dir

            # 生成合并文件
            safe_name = ''.join(item+"_" for item in filter_list if item is not None)
            file_path = os.path.join(out_dir, safe_name + "out_bind.xlsx")
            out.to_excel(file_path, index=False)

        return True, "输出成功", out_dir




